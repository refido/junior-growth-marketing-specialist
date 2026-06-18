from __future__ import annotations

import argparse
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence
from urllib.parse import parse_qs, urlparse

import yt_dlp
from pydantic import BaseModel, Field, HttpUrl
from youtube_transcript_api import (
    CouldNotRetrieveTranscript,
    NoTranscriptFound,
    TranscriptsDisabled,
    YouTubeTranscriptApi,
)

LOGGER = logging.getLogger(__name__)
DEFAULT_LIMIT = 5
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = PROJECT_ROOT / "research" / "youtube-transcripts"


class ChannelVideo(BaseModel):
    channel_name: str = Field(..., min_length=1)
    channel_url: HttpUrl
    video_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    video_url: HttpUrl
    publish_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")


class TranscriptDocument(BaseModel):
    video_title: str = Field(..., min_length=1)
    channel_name: str = Field(..., min_length=1)
    video_url: HttpUrl
    publish_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")
    transcript_text: str = Field(..., min_length=1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect transcripts from the latest YouTube videos for a set of channels.",
    )
    parser.add_argument(
        "channel_urls",
        nargs="+",
        help="One or more YouTube channel URLs.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_ROOT,
        help=f"Directory where Markdown transcripts will be saved. Default: {OUTPUT_ROOT}",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help="Number of latest videos to collect per channel. Default: 5",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
        help="Logging level. Default: INFO",
    )
    return parser


def sanitize_path_segment(value: str) -> str:
    cleaned = re.sub(r"[^\w\- ]+", "", value, flags=re.UNICODE).strip()
    cleaned = re.sub(r"[\s_]+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned)
    return cleaned.lower() or "unknown"


def normalize_publish_date(value: str | None) -> str:
    if not value:
        return "unknown-date"
    try:
        return datetime.strptime(value, "%Y%m%d").date().isoformat()
    except ValueError:
        return value


def extract_video_id(url: str) -> str:
    parsed = urlparse(url)
    if parsed.hostname in {"youtu.be"}:
        return parsed.path.lstrip("/")

    query = parse_qs(parsed.query)
    if "v" in query and query["v"]:
        return query["v"][0]

    parts = [part for part in parsed.path.split("/") if part]
    if "shorts" in parts:
        short_index = parts.index("shorts")
        if short_index + 1 < len(parts):
            return parts[short_index + 1]

    if parts:
        return parts[-1]

    raise ValueError(f"Unable to extract video id from URL: {url}")


def make_video_url(video_id_or_url: str) -> str:
    if video_id_or_url.startswith("http://") or video_id_or_url.startswith("https://"):
        return video_id_or_url
    return f"https://www.youtube.com/watch?v={video_id_or_url}"


def get_channel_videos(
    channel_url: str, limit: int = DEFAULT_LIMIT
) -> list[ChannelVideo]:
    """
    Retrieve the latest videos for a channel using yt-dlp.
    """

    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "skip_download": True,
        "playlistend": limit,
        "noplaylist": False,
    }

    LOGGER.info("Fetching latest %s videos from channel: %s", limit, channel_url)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        channel_info = ydl.extract_info(channel_url, download=False)

    if not channel_info:
        return []

    channel_name = (
        channel_info.get("channel")
        or channel_info.get("uploader")
        or channel_info.get("title")
        or "unknown-channel"
    )

    entries = channel_info.get("entries") or []
    videos: list[ChannelVideo] = []

    for entry in entries[:limit]:
        if not entry:
            continue

        entry_url = entry.get("url") or entry.get("webpage_url") or entry.get("id")
        if not entry_url:
            LOGGER.warning("Skipping entry without URL for channel %s", channel_name)
            continue

        full_video_url = make_video_url(entry_url)
        video_id = entry.get("id") or extract_video_id(full_video_url)

        with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True}) as ydl:
            video_info = ydl.extract_info(full_video_url, download=False)

        if not video_info:
            LOGGER.warning("Skipping video with no metadata: %s", full_video_url)
            continue

        title = video_info.get("title") or entry.get("title") or video_id
        publish_date = normalize_publish_date(
            video_info.get("upload_date") or entry.get("upload_date")
        )
        canonical_url = video_info.get("webpage_url") or full_video_url
        resolved_channel = (
            video_info.get("channel") or video_info.get("uploader") or channel_name
        )

        videos.append(
            ChannelVideo(
                channel_name=resolved_channel,
                channel_url=channel_url,
                video_id=video_id,
                title=title,
                video_url=canonical_url,
                publish_date=publish_date,
            )
        )

    return videos


def get_transcript(video_id: str) -> str | None:
    """
    Fetch the transcript text for a YouTube video.
    """

    api = YouTubeTranscriptApi()
    try:
        fetched = api.fetch(video_id)
    except (CouldNotRetrieveTranscript, TranscriptsDisabled, NoTranscriptFound):
        LOGGER.info("Transcript unavailable for video id: %s", video_id)
        return None

    snippets = [
        snippet.text.strip() for snippet in fetched.snippets if snippet.text.strip()
    ]
    transcript_text = "\n\n".join(snippets).strip()
    return transcript_text or None


def build_markdown(document: TranscriptDocument) -> str:
    return "\n".join(
        [
            f"# {document.video_title}",
            "",
            f"- Channel: {document.channel_name}",
            f"- Video URL: {document.video_url}",
            f"- Publish date: {document.publish_date}",
            "",
            "## Transcript",
            "",
            document.transcript_text,
            "",
        ]
    )


def save_transcript(document: TranscriptDocument, output_root: Path) -> Path:
    """
    Save a transcript document as Markdown.
    """

    channel_dir = output_root / sanitize_path_segment(document.channel_name)
    channel_dir.mkdir(parents=True, exist_ok=True)

    file_stem = f"{document.publish_date}-{sanitize_path_segment(document.video_title)}"
    output_path = channel_dir / f"{file_stem}.md"

    if output_path.exists():
        output_path = (
            channel_dir / f"{file_stem}-{extract_video_id(str(document.video_url))}.md"
        )

    output_path.write_text(build_markdown(document), encoding="utf-8")
    LOGGER.info("Saved transcript: %s", output_path)
    return output_path


def collect_transcripts(
    channel_urls: Sequence[str], output_dir: Path, limit: int
) -> list[Path]:
    saved_files: list[Path] = []

    for channel_url in channel_urls:
        videos = get_channel_videos(channel_url, limit=limit)
        LOGGER.info("Retrieved %d candidate videos from %s", len(videos), channel_url)

        for video in videos:
            transcript_text = get_transcript(video.video_id)
            if not transcript_text:
                LOGGER.info(
                    "Skipping %s because no transcript was found", video.video_url
                )
                continue

            document = TranscriptDocument(
                video_title=video.title,
                channel_name=video.channel_name,
                video_url=video.video_url,
                publish_date=video.publish_date,
                transcript_text=transcript_text,
            )
            saved_files.append(save_transcript(document, output_dir))

    return saved_files


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    saved_files = collect_transcripts(
        args.channel_urls, output_dir=output_dir, limit=args.limit
    )
    LOGGER.info("Completed transcript collection. Saved %d files.", len(saved_files))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

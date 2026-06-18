from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pydantic import BaseModel, Field, HttpUrl

LOGGER = logging.getLogger(__name__)


class SourceEntry(BaseModel):
    name: str = Field(..., min_length=1)
    url: HttpUrl


class ResearchSources(BaseModel):
    youtube: list[SourceEntry] = Field(default_factory=list)
    linkedin: list[SourceEntry] = Field(default_factory=list)


_SECTION_RE = re.compile(r"^(youtube|linkedin):\s*$")
_ITEM_RE = re.compile(r"^\s*-\s+name:\s*(.+?)\s*$")
_URL_RE = re.compile(r"^\s+url:\s*(.+?)\s*$")


def default_sources_file(project_root: Path) -> Path:
    return project_root / "research" / "sources.yaml"


def parse_sources_yaml(text: str) -> ResearchSources:
    current_section: str | None = None
    current_item: dict[str, str] | None = None
    collected: dict[str, list[dict[str, str]]] = {"youtube": [], "linkedin": []}

    for raw_line in text.splitlines():
        line = raw_line.rstrip()

        if not line or line.lstrip().startswith("#"):
            continue

        section_match = _SECTION_RE.match(line)
        if section_match:
            current_section = section_match.group(1)
            current_item = None
            continue

        item_match = _ITEM_RE.match(line)
        if item_match and current_section:
            current_item = {"name": item_match.group(1).strip()}
            collected[current_section].append(current_item)
            continue

        url_match = _URL_RE.match(line)
        if url_match and current_section and current_item is not None:
            current_item["url"] = url_match.group(1).strip()

    return ResearchSources(
        youtube=[
            SourceEntry.model_validate(item)
            for item in collected["youtube"]
            if item.get("name") and item.get("url")
        ],
        linkedin=[
            SourceEntry.model_validate(item)
            for item in collected["linkedin"]
            if item.get("name") and item.get("url")
        ],
    )


def load_research_sources(source_file: Path) -> ResearchSources:
    if not source_file.exists():
        LOGGER.warning("Sources file not found: %s", source_file)
        return ResearchSources()

    return parse_sources_yaml(source_file.read_text(encoding="utf-8"))


def select_source_urls(entries: Iterable[SourceEntry]) -> list[str]:
    return [str(entry.url) for entry in entries]

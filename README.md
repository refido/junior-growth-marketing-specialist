# YouTube Content Strategy for B2B SaaS

This repository is a research workspace for studying how SaaS founders, marketers, and content operators use YouTube and LinkedIn to generate pipeline, build trust, and create brand awareness.

## Goal

Understand how leading SaaS marketers use YouTube and LinkedIn to generate pipeline and brand awareness.

The research is focused on practical B2B SaaS content strategy, not general creator growth. The goal is to identify patterns that can later support a real playbook for founder-led content, YouTube strategy, SaaS demand generation, and LinkedIn distribution.

## Research questions

- What content formats work?
- How often do experts publish?
- What topics generate engagement?
- How does YouTube support SaaS growth?
- How do LinkedIn and YouTube work together in a B2B SaaS buyer journey?
- What tactics are repeated across multiple experts?
- Where do experts disagree?
- Is the collected material strong enough to support a real playbook later?

## Data collected

The project currently contains:

- 94 YouTube transcript files from SaaS, AI, marketing, and YouTube strategy channels.
- 10 LinkedIn post bundles from selected experts.
- A source list for YouTube and LinkedIn targets in `youtube-b2b-saas-research/research/sources.yaml`.
- A Markdown copy of the source list in `youtube-b2b-saas-research/research/sources.md`.
- A synthesis document in `youtube-b2b-saas-research/research/synthesis.md`.
- Collection scripts and project tooling under `youtube-b2b-saas-research/scripts`.

The YouTube transcripts are stored by channel under:

```text
youtube-b2b-saas-research/research/youtube-transcripts/
```

The LinkedIn post collections are stored by expert under:

```text
youtube-b2b-saas-research/research/linkedin-posts/
```

## Coverage and limitations

The YouTube corpus supports publishing cadence analysis because each transcript file includes a publish date in the filename and document metadata. The current collection is close to 10 recent transcript files per selected YouTube channel, with fewer files where fewer usable transcripts were available.

The LinkedIn corpus is useful for qualitative analysis of positioning, hooks, offers, and themes. It is less complete for precise cadence or engagement analysis unless individual post dates, reactions, comments, and impressions are collected in a later pass.

This means the repository is already strong for identifying content formats, topics, channel strategy, and repeated advice. A future data pass should add view counts, likes, comments, LinkedIn reactions, and posting timestamps if the playbook needs engagement scoring.

## Why these experts were chosen

The expert list was chosen to cover the main parts of a B2B SaaS content and demand-generation system:

| Expert | Why included |
| --- | --- |
| Rob Walling | SaaS strategy, bootstrapping, positioning, retention, and durable SaaS fundamentals. |
| TK Kader | SaaS GTM, ICP, demos, demand acquisition, message-market fit, and founder-led sales systems. |
| Sam Dunning | B2B SEO, AEO, AI search, money pages, backlinks, and SaaS demand generation. |
| Samu Kovacs | YouTube strategy for SaaS companies, long-form content systems, and LinkedIn-to-YouTube workflows. |
| Braden Ricchini | B2B YouTube packaging, outlier topics, hooks, scripts, and booked-call generation from small channels. |
| Jonathan Rintala | Organic inbound, webinars, free tools, Reddit, build-in-public, and lean SaaS GTM. |
| Nathan Latka | SaaS operator interviews with revenue, retention, pricing, quota, and growth metrics. |
| Dan Martell | AI leverage, company operating systems, leadership, and scaling teams with AI. |
| Marc Lou | Build-in-public SaaS updates, shipping cadence, analytics, product-led iteration, and MRR transparency. |
| Simon Hoiberg | AI agents, niche AI SaaS, self-hosting, developer-led SaaS, and automation workflows. |
| Justin Kan | Included in the source list as a founder/operator reference for future collection. |

Together, these sources cover both strategy and execution: what to publish, how to package it, how to distribute it, how to connect it to pipeline, and how to use technical tools to collect and analyze the material.

## Topics covered

The collected material is strongest around:

- B2B YouTube strategy.
- Founder-led content.
- LinkedIn distribution.
- SaaS SEO and AEO.
- AI search visibility.
- Content repurposing.
- Webinar-led demand generation.
- Free tools and product-led acquisition hooks.
- ICP and positioning.
- SaaS demos and sales conversion.
- Pipeline measurement.
- AI-assisted content and operations.
- Build-in-public SaaS growth.

## Tools

The project uses Python tooling managed with `uv`.

Core tools and libraries include:

- `yt-dlp` for discovering recent YouTube videos from channel URLs.
- `youtube-transcript-api` for collecting available YouTube transcripts.
- `requests` and `beautifulsoup4` for collecting public web content.
- `pydantic` for validating source and document models.
- `pyyaml` for reading the source manifest.
- `rich`, `pandas`, and standard Python tooling for future analysis workflows.

Common commands are documented in:

```text
youtube-b2b-saas-research/scripts.md
```

## Repository structure

```text
.
|-- README.md
`-- youtube-b2b-saas-research/
    |-- pyproject.toml
    |-- uv.lock
    |-- scripts.md
    |-- scripts/
    |   |-- collect_youtube_transcripts.py
    |   |-- collect_linkedin_posts.py
    |   `-- source_utils.py
    `-- research/
        |-- sources.yaml
        |-- sources.md
        |-- synthesis.md
        |-- youtube-transcripts/
        `-- linkedin-posts/
```

## Ability to work with APIs and technical tools

This project demonstrates the ability to:

- Define a research source manifest in YAML.
- Use Python scripts to collect data from YouTube channels.
- Validate collected metadata with typed models.
- Save unstructured content as organized Markdown files.
- Structure a research repository for repeatable analysis.
- Use technical tooling to move from raw transcripts and posts to synthesis.
- Prepare the corpus for deeper analysis such as topic clustering, publishing cadence analysis, engagement pattern review, and playbook creation.

## Current synthesis

The main research synthesis is here:

```text
youtube-b2b-saas-research/research/synthesis.md
```

It identifies:

- Recurring themes.
- Advice repeated by multiple experts.
- Contradictory opinions.
- YouTube growth tactics.
- SaaS demand generation tactics.
- Founder-led content strategies.

## The corpus has enough depth because it includes

- Multiple experts discussing the same problems from different angles.
- Full YouTube transcripts, not just titles or summaries.
- LinkedIn posts that show current positioning, offers, and content hooks.
- Strategy sources and operator sources.
- Tactical YouTube packaging advice.
- Tactical SaaS demand-generation advice.
- Repeated themes around ICP clarity, trust, long-form content, SEO/AEO, AI-assisted workflows, and pipeline measurement.

Useful future outputs could include:

- A B2B SaaS YouTube channel strategy template.
- A founder-led LinkedIn content.
- A content repurposing workflow.
- A YouTube topic validation checklist.
- A SaaS SEO/AEO money-page checklist.
- A pipeline attribution and weekly review template.

# Scripts & Development Commands

Common commands used during development.

---

## Environment

### Activate virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### Sync environment with lockfile

```powershell
uv sync
```

### Update all dependencies

```powershell
uv lock --upgrade
```

---

## Dependency Management

### Add a dependency

```powershell
uv add <package_name>
```

Example:

```powershell
uv add pyyaml
```

### Remove a dependency

```powershell
uv remove <package_name>
```

Example:

```powershell
uv remove pyyaml
```

### Show installed packages

```powershell
uv pip list
```

---

## Running Scripts

### Run a Python script

```powershell
uv run python scripts/<file>.py
```

Example:

```powershell
uv run python scripts/collect_youtube_transcripts.py
```

---

## Examples

### Collect YouTube transcripts using `sources.yaml`

```powershell
uv run python scripts/collect_youtube_transcripts.py
```

### Collect YouTube transcripts from specific channels

```powershell
uv run python scripts/collect_youtube_transcripts.py \
    https://www.youtube.com/@examplechannel/videos
```

### Collect transcripts from multiple channels

```powershell
uv run python scripts/collect_youtube_transcripts.py \
    https://www.youtube.com/@channel1/videos \
    https://www.youtube.com/@channel2/videos
```

---

## Quick Reference

| Task                  | Command                           |
|-----------------------|-----------------------------------|
| Activate venv         | `.venv\Scripts\Activate.ps1`      |
| Add dependency        | `uv add <package_name>`           |
| Remove dependency     | `uv remove <package_name>`        |
| Run script            | `uv run python scripts/<file>.py` |
| Sync environment      | `uv sync`                         |
| Update dependencies   | `uv lock --upgrade`               |
| List packages         | `uv pip list`                     |

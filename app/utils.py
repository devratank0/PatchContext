import json
from pathlib import Path


def ensure_dir(path: Path):
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def save_json(data, filepath: Path):
    """Save JSON data to a file."""
    ensure_dir(filepath.parent)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
"""Starter file for future automation scripts."""

from pathlib import Path
import json


def load_master_resume(path: str = "data/master_resume.json") -> dict:
    repo_root = Path(__file__).resolve().parents[1]
    file_path = repo_root / path
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    data = load_master_resume()
    print(f"Loaded {len(data.get('experiences', []))} experiences/projects")

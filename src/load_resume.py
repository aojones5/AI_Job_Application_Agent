import json
from pathlib import Path


def load_master_resume(path: str = "data/master_resume.json") -> dict:
    resume_path = Path(path)

    if not resume_path.exists():
        raise FileNotFoundError(f"Could not find resume file: {resume_path}")

    with open(resume_path, "r", encoding="utf-8") as f:
        return json.load(f)
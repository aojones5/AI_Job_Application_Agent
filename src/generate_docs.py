import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_prompt_file(filename: str) -> str:
    prompt_path = Path("prompts") / filename
    return prompt_path.read_text(encoding="utf-8")


def generate_tailored_resume(master_resume: dict, job_description: str, top_bullets: list[dict]) -> str:
    base_prompt = load_prompt_file("tailor_resume_prompt.md")

    selected_bullets = "\n".join(
        [f"- {item['bullet']} ({item['title']} at {item['organization']})" for item in top_bullets]
    )

    full_prompt = f"""
{base_prompt}

Candidate Master Resume:
{master_resume}

Job Description:
{job_description}

Top Relevant Experience Bullets:
{selected_bullets}
"""

    response = client.responses.create(
        model="gpt-5",
        input=full_prompt
    )

    return response.output_text


def generate_cover_letter(master_resume: dict, job_description: str, tailored_resume: str) -> str:
    base_prompt = load_prompt_file("cover_letter_prompt.md")

    full_prompt = f"""
{base_prompt}

Candidate Master Resume:
{master_resume}

Job Description:
{job_description}

Tailored Resume:
{tailored_resume}
"""

    response = client.responses.create(
        model="gpt-5",
        input=full_prompt
    )

    return response.output_text
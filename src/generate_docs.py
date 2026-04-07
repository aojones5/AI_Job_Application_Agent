import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_tailored_resume(master_resume: dict, job_description: str, top_bullets: list[dict]) -> str:
    selected_bullets = "\n".join(
        [f"- {item['bullet']} ({item['title']} at {item['organization']})" for item in top_bullets]
    )

    prompt = f"""
You are helping tailor a one-page resume.

Candidate master resume data:
{master_resume}

Target job description:
{job_description}

Most relevant candidate bullets:
{selected_bullets}

Write a polished, ATS-friendly one-page resume draft.
Rules:
- Focus on the most relevant experience
- Keep strong metrics and technical detail
- Do not invent experience
- Keep wording professional and concise
- Output in plain text
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


def generate_cover_letter(master_resume: dict, job_description: str, tailored_resume: str) -> str:
    prompt = f"""
Write a professional, specific cover letter based on this candidate background and tailored resume.

Candidate master resume:
{master_resume}

Target job description:
{job_description}

Tailored resume draft:
{tailored_resume}

Rules:
- Keep it to about 3 to 4 paragraphs
- Focus on the experiences emphasized in the tailored resume
- Do not invent anything
- Sound polished but natural
- Output in plain text
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text
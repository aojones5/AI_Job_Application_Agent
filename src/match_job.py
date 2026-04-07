# simple keyword match first
import re

def extract_keywords(text: str) -> set[str]:
    words = re.findall(r"\b[a-zA-Z][a-zA-Z0-9+\-#\.]+\b", text.lower())
    stopwords = {
        "the", "and", "for", "with", "that", "this", "from", "you", "your",
        "are", "our", "will", "have", "has", "had", "into", "using", "use",
        "about", "their", "they", "them", "role", "team", "work", "job",
        "years", "year", "experience", "skills", "ability", "preferred",
        "required", "responsibilities", "including", "support", "strong"
    }

    return {word for word in words if word not in stopwords and len(word) > 2}


def score_bullet_against_job(bullet_text: str, job_description: str) -> int:
    bullet_words = extract_keywords(bullet_text)
    job_words = extract_keywords(job_description)
    return len(bullet_words.intersection(job_words))


def rank_resume_bullets(master_resume: dict, job_description: str) -> list[dict]:
    ranked = []

    for exp in master_resume.get("experience", []):
        for bullet in exp.get("bullets", []):
            bullet_text = bullet.get("text", "")
            score = score_bullet_against_job(bullet_text, job_description)

            ranked.append({
                "organization": exp.get("organization", ""),
                "title": exp.get("title", ""),
                "date": exp.get("date", ""),
                "bullet": bullet_text,
                "score": score
            })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked
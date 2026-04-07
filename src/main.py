from pathlib import Path
from load_resume import load_master_resume
from match_job import rank_resume_bullets
from generate_docs import generate_tailored_resume, generate_cover_letter


def save_output(filename: str, content: str) -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / filename
    output_path.write_text(content, encoding="utf-8")

def main():
    print("Loading master resume...")
    master_resume = load_master_resume()

    print("\nPaste the full job description below.")
    print("When finished, type END on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    job_description = "\n".join(lines).strip()

    if not job_description:
        print("No job description entered.")
        return

    print("\nRanking resume bullets against the job description...")
    ranked_bullets = rank_resume_bullets(master_resume, job_description)
    top_bullets = ranked_bullets[:8]

    print("\nTop matching bullets:")
    for item in top_bullets:
        print(f"[score={item['score']}] {item['bullet']}")

    print("\nGenerating tailored resume...")
    tailored_resume = generate_tailored_resume(master_resume, job_description, top_bullets)
    save_output("tailored_resume.txt", tailored_resume)

    print("Generating cover letter...")
    cover_letter = generate_cover_letter(master_resume, job_description, tailored_resume)
    save_output("cover_letter.txt", cover_letter)

    print("\nDone.")
    print("Saved:")
    print("- outputs/tailored_resume.txt")
    print("- outputs/cover_letter.txt")


if __name__ == "__main__":
    main()
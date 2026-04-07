# Roadmap

## MVP
- Store all experience in `master_resume.json`
- Paste in a job description
- Generate a tailored resume
- Generate a matching cover letter
- Review manually before applying

## V2
- Build a ranking function for job relevance
- Save application packets by company and role
- Add recruiter message generation

## V3
- Add a dashboard in Next.js
- Track applications, statuses, and follow-ups
- Support exports to PDF and DOCX

## V4
- Add ingestion from job alerts, saved links, or email summaries
- Add optional permitted autofill helpers
- Keep human-in-the-loop approval before final submission

## Good engineering principles
- Keep every generated output grounded in the master resume data
- Prefer structured data over one large text blob
- Make ranking explainable
- Preserve factual accuracy
- Build in review checkpoints

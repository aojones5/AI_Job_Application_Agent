# AI Job Application Agent

A starter repository for an AI-assisted job application workflow that:
- stores a structured master resume
- analyzes job descriptions
- ranks relevant experience
- generates a tailored 1-page resume
- drafts a matching cover letter
- supports a future human-in-the-loop apply queue

## Why this project
This project is designed to turn a long, detailed resume into a reusable experience database that can be adapted to specific job descriptions. The goal is to automate the repetitive parts of the application process while keeping output quality high enough for real applications.

## Current scope
This starter repo includes:
- a structured master resume in JSON
- prompt templates for resume tailoring and cover letter generation
- a suggested roadmap for building the workflow into a full product

## Suggested architecture
1. **Resume database layer**
   - Store each role, project, and bullet as structured data
   - Tag entries by skills, domain, tools, and metrics

2. **Job analysis layer**
   - Parse the job description
   - Extract role title, company, keywords, must-have skills, and nice-to-haves

3. **Matching layer**
   - Score resume bullets against the job description
   - Rank the most relevant experiences

4. **Generation layer**
   - Generate a 1-page tailored resume
   - Generate a cover letter aligned to the chosen resume bullets
   - Generate a recruiter message and application notes

5. **Future automation layer**
   - Import jobs from alerts, saved links, or email digests
   - Queue high-match roles for review
   - Add optional browser automation only where permitted

## Repo structure
```text
ai-job-agent-starter/
├── README.md
├── .gitignore
├── data/
│   ├── master_resume.json
│   └── sample_job_posting.txt
├── prompts/
│   ├── tailor_resume_prompt.md
│   └── cover_letter_prompt.md
├── docs/
│   └── roadmap.md
└── src/
    └── placeholder.py
```

## Quick start
### 1. Clone or create the repo
```bash
git init
git add .
git commit -m "Initial commit: AI job application agent starter"
```

### 2. Add your API key later if you build generation scripts
Create a `.env` file and keep it out of Git.

### 3. Start simple
Use the files in `data/` and `prompts/` with ChatGPT first.
Once the workflow works manually, automate it with Python or Next.js.

## Best build path
### Phase 1
- Refine `master_resume.json`
- Test prompts against real job descriptions
- Improve resume and cover letter output quality

### Phase 2
- Build a script or web app that accepts:
  - master resume JSON
  - a pasted job description
- Output:
  - tailored resume bullets
  - cover letter draft
  - match score

### Phase 3
- Add a job tracker
- Add role scoring
- Add saved applications history
- Add review queue

### Phase 4
- Add ingestion from job alerts or saved links
- Add optional autofill helpers where allowed
- Keep a human review step before submission

## GitHub tips
A good repo description could be:

> AI-assisted workflow for scoring job descriptions, tailoring one-page resumes, and generating aligned cover letters from a structured master resume.

Suggested topics:
- ai
- automation
- resume-builder
- cover-letter-generator
- nextjs
- python
- career-tools

## First milestone
Get one job description, run the prompts, and generate:
- a tailored 1-page resume
- a matching cover letter
- a match score explanation

That is enough for a strong MVP.

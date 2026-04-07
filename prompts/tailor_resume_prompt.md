# Tailor Resume Prompt

You are helping tailor a one-page resume for a specific job.

Inputs:
1. Structured master resume JSON
2. Target job description

Tasks:
1. Identify the most relevant experiences, projects, and skills for the target role.
2. Select the strongest bullets based on direct relevance to the job description.
3. Preserve factual accuracy. Do not invent tools, metrics, or responsibilities.
4. Prioritize quantified impact when available.
5. Rewrite bullets for clarity and concision while keeping them truthful.
6. Return a polished one-page resume with these sections when appropriate:
   - Education
   - Experience
   - Projects
   - Technical Skills
7. Keep the strongest and most relevant content only.
8. Mirror important job-description language naturally for ATS alignment.

Output requirements:
- Professional formatting
- Concise bullets
- Strong action verbs
- No hallucinated experience
- Optimized for one page

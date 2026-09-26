# Resume Assist

Tailor a one-page LaTeX resume to a specific job description using an AI coding agent (Claude Code, Cursor, Copilot, etc.).

You keep all your real experience in one JSON file. For each job, the agent chooses the most relevant parts and rewrites them into `resume.tex`. It is instructed never to invent skills, companies, or dates.

## Setup (once)

1. Clone the repo and open it in your editor.
2. Replace the contents of `resume_database.json` with your own details. Follow the schema. Include **everything**: all roles, all bullet points, all projects. The agent picks the best subset for each job, so more is better.
3. In `template.tex`, update the parts the agent is told not to touch: the **header** (name, contact links) and the **Education** section.

## Tailoring for a job

1. **Build the prompt:**

   ```bash
   python3 jd_maker.py
   ```

   Enter the company name and website (optional), paste the job description end with END_JD, then press **Enter on an empty line** to finish. The prompt is now in your clipboard.

2. **Run the agent:** open your AI agent in this folder, paste the prompt, and send it. The agent reads `PROMPT.md`, creates or edits `resume.tex`, and summarizes what it kept, cut, and reworded.

3. **Review the output:** read the summary and the diff. Check that every claim is true and that the wording sounds like you.

4. **Compile to PDF:**

   ```bash
   pdflatex resume.tex
   ```

   Or upload `resume.tex` to Overleaf. Confirm it fits on **one page**. If it overflows, ask the agent to trim.

## Tips

- **Keep the database accurate.** The agent only rewords and selects what it finds there. Wrong data in the database means wrong data in the resume.
- **Add metrics to the database**, not to the resume. Numbers in the database become strong bullet points.
- **Paste the full job description.** Keyword matching works best with the complete text.
- **Customize the rules** by editing `PROMPT.md`, for example the number of projects or which sections stay fixed.
- To start fresh for a new job, delete `resume.tex` (or copy `template.tex` over it) before running the agent.

## How it works

| File | Purpose |
| --- | --- |
| [`resume_database.json`](./resume_database.json) | **Your data.** Experience, projects, skills, achievements. This is the only source of facts about you. |
| [`resume_database.schema.json`](./resume_database.schema.json) | The JSON schema for the database (lets your editor autocomplete and validate it). |
| [`template.tex`](./template.tex) | The LaTeX layout: fonts, spacing, section order. Holds formatting only. |
| [`PROMPT.md`](./PROMPT.md) | The instructions the agent follows (rules, what to cut, what never to change). |
| [`jd_maker.py`](./jd_maker.py) | Helper script that builds the prompt from a job description and copies it to your clipboard. |
| `resume.tex` | The tailored output. Created per job and git-ignored. |

## Requirements

- Python 3 (no extra packages)
- An AI coding agent that can read and edit files in this folder
- A way to compile LaTeX: [Overleaf](https://www.overleaf.com/) or a local TeX distribution (MacTeX / TeX Live)


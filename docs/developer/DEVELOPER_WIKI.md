# Developer Wiki

This developer wiki is a Phase A reference for the ILS architecture and developer workflow. It is intentionally technical and focused on implementation, not end-user guidance.

## 1. Purpose

This document is the developer entry point for the ILS documentation effort. It should answer:

- Why architectural decisions were made
- Which data model relationships matter most
- How to set up the local development environment
- How grading, snapshots, and trends flow through the system
- Known issues, gotchas, and future maintenance tasks

This repo is a docs repository. The application code remains in `ILS-dev`; this wiki references that codebase without modifying it.

## 2. Architecture decisions and rationale

### Backend

- **Node.js + Express + Sequelize**
  - Reason: stable ecosystem, familiar ORM patterns, and good migration support.
  - Rule: migrations are the single source of truth for schema changes.
  - Rule: `sequelize.sync()` must remain disabled in every environment.

- **Database-first policy**
  - All schema changes must be implemented with idempotent SQL migrations under `backend/migrations/`.
  - Migrations should include existence checks where relevant and avoid destructive operations without rollback strategy.

- **BigInt serialization**
  - The backend uses JSON middleware that converts `BigInt` values to strings before sending API responses.
  - This avoids browser `JSON.stringify()` failures and keeps API output stable.

### Frontend

- **React + Vite + Tailwind CSS**
  - Reason: fast local feedback loop, lightweight build, and predictable styling.
  - The frontend is designed to consume the backend API and render dashboards, heatmaps, and teacher workflows.

### Separation of concerns

- The system is organized as two connected domains:
  - **Vertical hierarchy**: institution → campus → course → module → assignment → class
  - **Intelligence layer**: outcomes, rubrics, criteria, trends, and heatmaps
- Keeping these domains separate avoids mixing structural course data with learning analytics.

### Docs workflow

- This documentation repo is intentionally separate from `ILS-dev`.
- `docs/phase-a-structure` is the current branch for Phase A work.
- GitHub Project 5 is used to track Phase A and Phase B documentation tasks.
- `Active-ILS-doc.md` is the local project tracker for the docs repo.

## 3. Glossary of Terms

| Term | Definition |
|------|------------|
| Outcome | A measurable learning objective or skill that the system tracks |
| Mastery Score | A 0–10 score representing outcome proficiency, derived from rubric and submission data |
| Snapshot | A point-in-time record of a student’s mastery score for a specific outcome |
| Trend Direction | The direction of change between snapshots: Up, Down, or Flat |
| Trend Confidence | A confidence category based on snapshot history and score stability |
| At-Risk | A student whose mastery score is below an applicable success threshold |
| Cockpit | The teacher-facing dashboard for identifying students and outcomes that need attention |
| Heatmap | A grid showing student mastery levels across outcomes |

## 4. Data model (key relationships)

The ILS data model is built around two connected domains.

### Vertical structure

- `institutions` → `campuses` → `courses` → `modules` → `assignments` → `classes`
- Students are enrolled in classes and submit work against assignments.

### Intelligence entities

- `outcomes` describe what students should learn.
- `rubrics` define how work is scored.
- `criteria` are the individual rubric items.
- `themes` are higher-level groupings of curriculum intelligence.

### Junction tables

- `module_outcomes` connects modules to outcomes.
- `assignment_outcomes` connects assignments to outcomes.
- `assignment_rubrics` connects assignments to rubrics.
- `module_themes` connects modules to themes.

### Core relationships

- `assignment` belongs to `module`
- `submission` belongs to `assignment` and `student`
- `submission_ratings` capture rubric criterion ratings per submission
- `student_outcome_snapshots` capture aggregated mastery per student/outcome over time

### Snapshot data

- Each snapshot is a historical record used to compute trends.
- A snapshot typically includes: student id, outcome id, mastery score, timestamp, and confidence metadata.
- The system relies on snapshots for both dashboards and trend analysis.

## 5. Setup & development environment

This repo is for documentation. The application code is in `ILS-dev`.

### ILS-doc local docs server

```powershell
cd C:\Users\0102663\Projects\bim\ILS-doc
pip install mkdocs mkdocs-material
mkdocs serve
```

### ILS-dev app setup

```powershell
cd C:\Users\0102663\Projects\bim\ILS-dev\backend
copy .env.example .env
npm install
npm run create-db
npm run dev

cd ..\frontend
npm install
npm run dev
```

### Testing

- Backend tests: `cd backend && npm run test:reporting`
- Frontend tests: `cd frontend && npm run test:playwright`

### ILS-doc repo workflow

- Always work on `docs/phase-a-structure` unless a new phase branch is needed.
- Keep content changes inside `ILS-doc` only.
- Use `Active-ILS-doc.md` to document current scope and objectives.
- Build the site locally with `mkdocs build` after content changes.
- Preview live changes with `mkdocs serve` when ready.

## 6. Key workflows

### Grading → snapshots → trends

1. A teacher grades a submission using rubrics.
2. Criterion-level ratings are saved in `submission_ratings`.
3. The backend aggregates these ratings into per-assignment outcome scores.
4. `student_outcome_snapshots` are created or updated for each student/outcome.
5. Trend computation compares the latest snapshots to previous snapshots and produces:
   - `trend_direction`
   - `trend_confidence`
   - `delta`

### Developer tasks for Phase A

- Update documentation content in this repo, not application code.
- Use the current branch `docs/phase-a-structure` for Phase A work.
- Keep Phase A focused on developer-facing architecture, setup, and workflows.

## 7. Known issues & future todos

- `pwsh` may not be available in some Windows environments; git hooks should fall back to `powershell` as needed.
- Documentation in this repo should not mix user guides with developer guidance.
- Future additions:
  - API reference examples
  - ER diagrams and relationship visualizations
  - Troubleshooting and environment setup notes

## 8. Quick links

- ILS app backend: `C:\Users\0102663\Projects\bim\ILS-dev\backend`
- ILS app frontend: `C:\Users\0102663\Projects\bim\ILS-dev\frontend`
- Docs repo: `C:\Users\0102663\Projects\bim\ILS-doc`
- Current docs branch: `docs/phase-a-structure`
- Project board: https://github.com/users/Maestrocop/projects/5

---

This page is the Phase A developer reference for ILS documentation. Review before expanding into separate MkDocs pages.

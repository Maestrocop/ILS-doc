# Developer Wiki

> Legacy long-form page. The Developer Guide content has been split into smaller pages for better navigation.
>
> Use the Developer Guide menu on the left to open:
> - Overview
> - Architecture
> - Data Model
> - Workflows
> - Setup
> - Decisions
> - API Reference
> - Glossary

## 1. Purpose

This guide is the primary developer-facing documentation for the Intelligent Learning System (ILS).
It should support maintainers in understanding:

- architecture decisions and why they were made
- the ILS data model and key relationships
- developer setup and local environment configuration
- grading, snapshot, and trend workflows
- documentation workflow and repo conventions
- known issues and future maintenance items

This repo is the docs repository. The application code remains in `ILS-dev`; this wiki references that codebase but does not modify it.

## 2. What we are building

We are building a Phase A developer reference site on top of MkDocs Material.
The goal is to make the ILS architecture, data model, and analytics workflows readable and actionable for maintainers.

The current scope includes:

- developer reference and architecture decisions
- data model relationships and entity mappings
- setup and local documentation workflow
- workflow descriptions for grading, snapshots, trends, and intelligence features
- concept-level explanation of ILS analytics features

## 3. Architecture decisions and rationale

### 3.1 Backend architecture

- **Node.js + Express + Sequelize**
  - Chosen for a familiar JavaScript stack and consistent ORM patterns.
  - Sequelize provides migration support, but the system must rely on explicit SQL migrations.

- **Database-first migration policy**
  - All schema changes are implemented through SQL migrations under `backend/migrations/`.
  - Migrations must be idempotent and include guard clauses when possible.
  - No schema changes should be made through `sequelize.sync()` in any environment.

- **BigInt handling**
  - The backend converts `BigInt` values to strings before JSON serialization.
  - This prevents browser client failures and maintains API compatibility.

### 3.2 Frontend architecture

- **React + Vite + Tailwind CSS**
  - Provides speed of development, small builds, and responsive UI styling.
  - The frontend consumes backend APIs and renders insights in dashboards, heatmaps, and cockpit screens.

### 3.3 Separation of concerns

The system maintains two core domains:

- **Vertical hierarchy**
  - `institution` → `campus` → `course` → `module` → `assignment` → `class`

- **Intelligence layer**
  - `outcomes`, `rubrics`, `criteria`, `themes`, `snapshots`, `trends`

Keeping these domains separate prevents confusion between structural curriculum data and learning analytics.

### 3.4 Documentation architecture

- Separate the docs repo from the app repo.
- Use `docs/phase-a-structure` for active Phase A work.
- Track the docs effort in GitHub Project 5 and `Active-ILS-doc.md`.

## 4. Glossary of Terms

| Term | Definition |
|------|------------|
| Outcome | A measurable learning objective or skill that the system tracks |
| Mastery Score | A 0–10 normalized score representing outcome proficiency |
| Snapshot | A point-in-time record of a student’s mastery score for a specific outcome |
| Trend Direction | The direction of change between snapshots: Up, Down, or Flat |
| Trend Confidence | A confidence label based on snapshot history and score stability |
| At-Risk | A student below the configured success threshold for an outcome |
| Cockpit | The teacher-facing dashboard for identifying students who need attention |
| Heatmap | A grid view showing student mastery across outcomes |

## 5. Data model (key relationships)

The ILS data model connects curriculum structure to intelligence data.

### 5.1 Vertical structure

- `institutions`
- `campuses`
- `courses`
- `modules`
- `assignments`
- `classes`
- `students`

Students enroll in classes and submit work for assignments.

### 5.2 Intelligence entities

- `outcomes` define learning goals.
- `rubrics` define scoring logic.
- `criteria` are the items within rubrics.
- `themes` group related curriculum intelligence.

### 5.3 Junction tables

- `module_outcomes` links modules to outcomes.
- `assignment_outcomes` links assignments to outcomes.
- `assignment_rubrics` links assignments to rubrics.
- `module_themes` links modules to themes.

### 5.4 Core relationships

- `assignment` belongs to `module`
- `submission` belongs to `assignment` and `student`
- `submission_ratings` capture criterion-level scores for a submission
- `student_outcome_snapshots` capture aggregated mastery per student/outcome over time

### 5.5 Snapshot details

- A snapshot captures:
  - student id
  - outcome id
  - mastery score
  - timestamp
  - trend or confidence metadata

- Snapshots are the basis for trend computation and historical analysis.

## 6. Setup & development environment

This repository is for documentation. The application code is in `ILS-dev`.

### 6.1 ILS-doc local docs workflow

```powershell
cd C:\Users\0102663\Projects\bim\ILS-doc
python -m pip install mkdocs mkdocs-material
mkdocs serve
```

- Run `mkdocs serve` to preview docs locally.
- Run `mkdocs build` to verify the site compiles.

### 6.2 ILS-dev app setup (reference only)

The app code is in `C:\Users\0102663\Projects\bim\ILS-dev`.

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

### 6.3 Testing

- Backend tests: `cd backend && npm run test:reporting`
- Frontend tests: `cd frontend && npm run test:playwright`

### 6.4 ILS-doc repo workflow

- Work only in `ILS-doc`; do not modify `ILS-dev` unless explicitly requested.
- Use `docs/phase-a-structure` for active Phase A authoring.
- Update `Active-ILS-doc.md` as project goals or status change.
- After changes, run `mkdocs build`.
- When ready, preview with `mkdocs serve`.

## 7. Key workflows

### 7.1 Grading → snapshots → trends

1. A teacher grades a submission using a rubric.
2. The system stores `submission_ratings` for each criterion.
3. Ratings are aggregated into an outcome-level mastery score.
4. `student_outcome_snapshots` are created or updated for the student/outcome.
5. Trend logic compares the latest snapshot to previous values and produces:
   - `trend_direction`
   - `trend_confidence`
   - `delta`

### 7.2 Why this workflow matters

- Snapshots preserve learning progress history.
- Trend analysis enables teachers to distinguish meaningful change from noise.
- The cockpit and heatmap use these signals to surface instructional priorities.

## 8. Contribution guidelines

- Keep documentation changes in `ILS-doc` only.
- Add new pages under `docs/developer` or `docs/concepts`.
- Keep the navigation updated in `mkdocs.yml`.
- Use clear headings, short sections, and code examples when relevant.
- Avoid writing user-facing instructions in Phase A documentation.

## 9. Known issues & future todos

- `pwsh` may not be installed in some Windows environments; use `powershell` or adjust hooks if needed.
- The docs repo should remain separate from `ILS-dev`.
- Future docs work should include:
  - API reference examples
  - ER diagrams and architecture diagrams
  - troubleshooting and environment diagnostics

## 10. Quick links

- ILS app backend: `C:\Users\0102663\Projects\bim\ILS-dev\backend`
- ILS app frontend: `C:\Users\0102663\Projects\bim\ILS-dev\frontend`
- Docs repo: `C:\Users\0102663\Projects\bim\ILS-doc`
- Current docs branch: `docs/phase-a-structure`
- Project board: https://github.com/users/Maestrocop/projects/5

---

This page is the Phase A developer reference for ILS documentation. Review before expanding into separate MkDocs pages.

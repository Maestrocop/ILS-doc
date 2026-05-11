# DEVELOPER_WIKI

This file is a concise, developer-focused reference for the ILS codebase. It is intentionally technical: architecture rationale, data model, setup steps, key workflows, known issues, and a glossary.

## 1. Architecture decisions and rationale

- Backend: Node.js + Express with Sequelize ORM.
  - Rationale: Familiar stack, good migration tooling, active ecosystem.
  - Decision notes: keep migrations as the single source of truth; do not enable `sequelize.sync()` in production.

- Frontend: React + Vite + Tailwind CSS.
  - Rationale: fast dev feedback loop, small bundles, and Tailwind accelerates UI development.

- DB-first policy: All schema changes must be done via idempotent migrations.
  - Rationale: maintain production compatibility and auditability.

- BigInt handling: JSON middleware converts BigInt → string for API responses.
  - Rationale: browser/JSON limitations.

- Separation of concerns: vertical hierarchy (institution → campus → course → module → assignment → class) remains separate from intelligence layer (themes, outcomes, rubrics).

## Glossary of Terms

| Term | Definition |
|------|------------|
| Outcome | Learning objective, measurable skill |
| Mastery Score | 0–10 numeric scale calculated from rubric criteria |
| Snapshot | Point-in-time record of student mastery (per outcome) |
| Trend Direction | Up / Down / Flat, derived from score delta between snapshots |
| Trend Confidence | High / Medium / Low / Insufficient — computed from snapshot counts and variance |
| At-Risk | Student below campus or class success threshold |
| Cockpit | Teacher dashboard for student attention and interventions |
| Heatmap | Matrix of students × outcomes showing mastery scores |

(Place glossary after Architecture Decisions and before Data Model in MkDocs nav.)

## 2. Data model (key relationships)

- Primary entities (high level): `institutions`, `campuses`, `courses`, `modules`, `assignments`, `classes`, `students`.
- Intelligence entities: `outcomes`, `rubrics`, `criteria`, `themes`.
- Junction tables: `module_outcomes`, `assignment_outcomes`, `assignment_rubrics`, `module_themes`.
- Important relationships:
  - `assignment` → belongsTo `module`
  - `submission` → belongsTo `assignment`, belongsTo `student`
  - `rubric` → hasMany `criteria`; `submission_ratings` store criterion-level ratings
  - `student_outcome_snapshots` capture aggregated mastery score per student/outcome at a timestamp

(Diagram: include ER diagram PNG in `docs/media` later.)

## 3. Setup & development environment

- Prereqs: Node 18+, npm 10+, PostgreSQL 14+, Git, gh CLI (optional).
- Backend:

```powershell
cd backend
cp .env.example .env
# ensure DATABASE_URL points to local test DB
npm install
npm run create-db   # run migrations and seed minimal test data
npm run dev
```

- Frontend:

```powershell
cd frontend
npm install
npm run dev
```

- Running tests:
  - Backend unit/reporting tests: `cd backend && npm run test:reporting`
  - Frontend E2E: `cd frontend && npm run test:playwright`

## 4. Key workflows

### Grading → snapshots → trends

1. Teacher grades a submission; rubric criterion ratings are persisted in `submission_ratings`.
2. A background worker (or API action) aggregates rubric scores into an assignment-level mastery and writes/updates `student_outcome_snapshots` for each (student, outcome).
3. Trend computation compares recent snapshots to compute `trend_direction` (delta sign) and `trend_confidence` (based on snapshot count and variance). See `backend/lib/grading_engine.js` for formulas.

### Typical developer tasks

- Add migration: write idempotent SQL migration under `backend/migrations/` and include `IF NOT EXISTS` guards.
- Add model field: update Sequelize model and add corresponding migration. Run migrations locally.

## 5. Known issues & future todos

- Some environments may lack `jq` which makes CLI GraphQL payload handling brittle; prefer file-based GraphQL queries or `gh` subcommands.
- Ensure `ILS_BACKUP_ROOT` points to a persistent location; backups live outside repo.
- TODO: add ER diagram, API reference examples, and troubleshooting steps for common DB errors.

## 6. Quick links (dev)

- Backend server: `backend/src/server.js`
- Migrations: `backend/migrations/`
- Frontend entry: `frontend/src/main.jsx`
- Project board (ILS-doc): GitHub Project ID 5 (owner: Maestrocop)

---

End of developer wiki (starter). Expand sections into MkDocs pages as needed.

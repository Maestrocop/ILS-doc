lass#
# Full Documentation Item List (Authoritative)
#
# This list is derived from the actual ILS-dev codebase and must be kept in sync with the project.
#
# 1. System Architecture
#    - Two-dimension model: vertical (hierarchy) and horizontal (intelligence layer)
#    - Module as system hub
#    - Backend: Node.js, Express, Sequelize, PostgreSQL
#    - Frontend: React 18, Vite, Tailwind CSS
#    - API-first design, modular structure
#
# 2. Data Model (Entities & Relationships)
#    - Institution, Campus, Course, Module, Assignment (vertical hierarchy)
#    - Themes, Outcomes, Criteria, Rubrics (horizontal/global entities)
#    - Junction tables: module_themes, module_learning_outcomes, assignment_outcomes, outcome_criteria, criteria_rubrics
#    - Module aggregates: structures (weeks/topics), assignments, teaching methods, linked themes, outcomes
#
# 3. Backend API Surface
#    - Core routes: /api/institutions, /api/campuses, /api/courses, /api/modules, /api/assignments, /api/themes, /api/outcomes, /api/assessment-types
#    - Module endpoints: CRUD, banks (outcomes, teaching methods, assignments), child fetches (structures, assessments, outcomes, teaching methods)
#    - Assignment endpoints: CRUD, module linkage, status filtering
#    - Admin endpoints: describe outcomes, describe module teaching methods, seeders
#
# 4. Model Definitions & Associations
#    - Sequelize models for all entities
#    - Model associations: hasMany, belongsTo, belongsToMany (as per index.js)
#    - Paranoid (soft delete) and timestamp conventions
#
# 5. Frontend Workflows & Pages
#    - Main pages: ModulesPage, ModuleEditor, ModuleForm, AssignmentsPage, OutcomesPage, ThemesPage, SettingsPage
#    - Admin section: AdminSidebar, admin routes
#    - Data fetching: fetchApi, banks, entity lists, detail views
#    - Form flows: module creation/editing, assignment creation/editing
#
# 6. Core Workflows
#    - Module creation and editing
#    - Assignment creation and editing (linked to modules)
#    - Linking themes, outcomes, teaching methods
#    - Fetching and displaying banks (outcomes, teaching methods, assignments)
#    - Data integrity: required fields, fallback/defaults, error handling
#
# 7. Development & Architecture Rules
#    - No orphan entities, strict parent-child hierarchy
#    - No cross-ownership in vertical hierarchy
#    - Horizontal entities are global, never owned by modules/courses
#    - All relationships via junction tables, not nesting
#    - No new tables or schema redesigns without approval (stabilization phase)
#    - UI ↔ API consistency is a top priority
#
# 8. Database & Migrations
#    - PostgreSQL with BIGINT IDENTITY PKs
#    - Migrations: idempotent, never alter existing files, only add new
#    - Soft deletes (deleted_at), created_at/updated_at timestamps
#
# 9. Environment & Setup
#    - Backend: .env, DATABASE_URL, npm scripts
#    - Frontend: VITE_API_URL, npm scripts, Vite proxy
#    - Dev server ports: backend 4000, frontend 5173
#
# 10. Utilities & Scripts
#    - Backup scripts, migration runners, seeders
#    - Admin/utility endpoints for describing schema


# Active ILS-doc

**MANDATORY RULE:**
All documentation tasks, categories, priorities, effort estimates, and status MUST be tracked in this file (`Active-ILS-doc.md`).

- Every new documentation task must be registered here with:
	- Category
	- Priority (High/Medium/Low)
	- Effort (S/M/L/XL)
	- Status (Not started / In progress / Complete)
- After completing any task, update this file to reflect the new status.
- This file is the central, authoritative todo list for all ILS-doc work.


This file tracks the current documentation work in `C:\Users\0102663\Projects\bim\ILS-doc`.

## Current focus

- **Primary goal:** rewrite the Developer Guide from audited `ILS-dev` code.
- **Secondary goal:** keep Teacher Guide content aligned with the actual teacher-facing pages.
- **Tertiary goal:** add an Admin Guide based on the existing admin UI and API surface.
- **Current working file:** `DEVELOPER_WIKI.md` and related developer guide pages.
- **Task source:** use GitHub Projects board `https://github.com/users/Maestrocop/projects/5` as the active todo list for documentation work.

## Source of truth

- `ILS-dev` is the source of truth.
- `ILS-doc` is the documentation repository.
- All content must reflect actual application behavior, not planned or hypothetical features.

## Work completed

- Audited key backend route files in `ILS-dev/backend/routes`.
- Audited frontend route definitions in `ILS-dev/frontend/src/App.jsx`.
- Rewrote `docs/developer/architecture.md`, `docs/developer/data-model.md`, `docs/developer/workflows.md`, and `docs/developer/api.md`.
- Added `docs/admin/index.md` and exposed the new Admin Guide in `mkdocs.yml`.

## Open validation step

- Run `mkdocs build` in `C:\Users\0102663\Projects\bim\ILS-doc`.
- Fix any Markdown or navigation issues reported by the build.


## Task Tracker

| Task                                         | Category           | Priority | Effort | Status       |
|----------------------------------------------|--------------------|----------|--------|--------------|
| Document System Architecture                 | Developer Guide    | High     | M      | Done         |
| Document Data Model (Entities & Relationships)| Developer Guide    | High     | L      | Done         |
| Document Backend API Surface                 | Developer Guide    | High     | L      | Done         |
| Document Period Template apply/replace behavior | Developer Guide    | High     | M      | Done         |
| Review and refine `DEVELOPER_WIKI.md`        | Developer Guide    | High     | M      | In progress  |
| Document Model Definitions & Associations    | Developer Guide    | High     | M      | Done         |
| Document Frontend Workflows & Pages          | Developer Guide    | High     | L      | Done         |
| Document Core Workflows                     | Developer Guide    | High     | L      | Done         |
| Document Grading Cockpit page                | Developer Guide    | High     | M      | Complete     |
| Document Heatmap page                        | Developer Guide    | High     | M      | Complete     |
| Document Student Cockpit page                | Developer Guide    | High     | M      | Complete     |
| Document Classroom Intelligence page         | Developer Guide    | High     | M      | Complete     |
| Document Assignments page                    | Developer Guide    | Medium   | M      | Complete     |
| Document Rubrics page                        | Developer Guide    | Medium   | M      | Complete     |
| Document Institutions page                   | Developer Guide    | Medium   | S      | Complete     |
| Document Campuses page                       | Developer Guide    | Medium   | S      | Complete     |
| Document Courses page                        | Developer Guide    | Medium   | S      | Complete     |
| Document Themes page                         | Developer Guide    | Medium   | S      | Complete     |
| Document Outcomes page                       | Developer Guide    | Medium   | S      | Complete     |
| Document Criteria Bank page                  | Developer Guide    | Medium   | S      | Complete     |
| Document Mapping Matrix page                 | Developer Guide    | Medium   | S      | Complete     |
| Document Classes page                        | Developer Guide    | Medium   | S      | Complete     |
| Document Users page                          | Developer Guide    | Medium   | S      | Complete     |
| Document Reporting Rules page                | Developer Guide    | Medium   | S      | Complete     |
| Document Teacher Roster page                 | Developer Guide    | Medium   | S      | Complete     |
| Document Development & Architecture Rules    | Developer Guide    | High     | M      | Done         |
| Document Database & Migrations               | Developer Guide    | Medium   | M      | Done         |
| Document Environment & Setup                 | Developer Guide    | Medium   | S      | Done         |
| Document Utilities & Scripts                 | Developer Guide    | Medium   | S      | Done         |
| Document New Route Groups (Student/Curriculum/Quizzes/Module Items/AI) | Developer Guide | High | M | Complete |
| Document Phase 5 Calendar (Epic #122)       | Phase 5            | High     | M      | Complete     |
| Document Phase 5 Process Engine (Epic #127) | Phase 5            | High     | M      | Complete     |

## Current checklist

- [x] Audit actual code in `ILS-dev`.
- [x] Rewrite Developer Guide pages to match live implementation.
- [x] Add Admin Guide content based on current admin pages and APIs.
- [x] Validate the docs site with `mkdocs build`.
- [ ] Confirm Teacher Guide remains UI-focused.

## Recent activity (2026-05-25)

- Added Admin pages: `docs/admin/academic-calendar.md`, `docs/admin/admin-tools.md` — reference backend validation and per-day expansion behavior.
- Added Marketing feature highlights: `docs/marketing/feature-highlights.md`, `docs/marketing/module-composer.md`, `docs/marketing/dashboards.md`, `docs/marketing/calendar.md`.
- Added `docs/processes/daily-checkpoint.md` summarizing session actions.
- Extended `docs/developer/api.md` with concrete examples for `/api/events`, `/api/academic-calendar`, and `GET /api/modules/:id/items`.
- Built the site with `mkdocs build --strict` to validate the changes.


## Notes

- The Admin Guide is intentionally lightweight and based on the current admin UI and backend API support.
- The Developer Guide now documents actual request payloads, route groups, and model associations.
- Do not add new docs pages for features that are not present in `ILS-dev`.

## Assistant Enforcement Constraints

Primary Role: Author accurate, user-facing documentation in ILS-doc that reflects the actual ILS-dev implementation.

Anti-Hallucination Guard: Follow strict project rules: DB_FIRST, SCHEMA_FIRST_IMPLEMENTATION, NO_FIELD_INVENTION, MODEL_DB_PARITY, NO_JSONB_FOR_RELATIONAL_DATA. If an API payload or database column is not explicitly visible via a read-action in ILS-dev, do not invent it.

Code Restrictions: You are in a documentation repository. Do not modify ILS-dev runtime code or execute migrations.

Markdown Standard: Every feature doc must contain: Purpose, Users, Step-by-step tasks, Expected outcomes with concrete examples/tables, and UI navigation labels. No placeholders like TODO allowed.

## Lead Technical Writer Mandate

- Role: Lead Technical Writer & Content Manager for ILS (documentation-only).
- Scope: Maintain and synchronize User Manuals for Developers, Teachers, Students, and Administrators; maintain Marketing documentation highlighting high-value features.
- Daily Full-App Scan: Perform a read-only scan of the entire ILS-dev application every cycle to detect new or changed features and update docs accordingly.
- Priority Queue: Always prioritize scanning the full ILS-dev state and keep Teacher, Student, Admin, Developer, and Setup guides synchronized.
- Marketing Focus: Track and document top-value features (e.g., Module Composer sequencing logic, smart dashboards, intelligence panels) for marketing collateral.
- Decision Authority: If frontend behavior is ambiguous, pause and ask the user before writing; NEVER modify ILS-dev code.
- Review Mode (Gate): Complete one user-facing guide section at a time, run `mkdocs build --strict` to validate, and wait for explicit user approval before advancing to the next user type.
- Daily Checkpoint: At end of each working session provide a concise summary listing manuals updated, marketing points captured, and pending clarifications.
- Communication: Provide short preambles before tool batches and concise progress updates after grouped actions; use `manage_todo_list` to track multi-step work.
- Enforcement: Strict docs-only policy; no code changes, migrations, or non-doc edits to ILS-dev without explicit user sign-off.
- Memory: Persisted to /memories/assistant_workflow_preferences.md (LastUpdated: 2026-05-25).

## Session Note — 2026-06-03
- GitHub auth: user resolved GH CLI authentication; advised persistent credential helper and/or SSH key to avoid repeated prompts.
- Documentation: Reviewed Classroom Intelligence; docs and frontend implementation present in `ILS-dev` (ClassroomIntelligencePage).
- Saved by assistant: session note recorded and todo updated.


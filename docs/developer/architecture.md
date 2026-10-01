# Architecture

This page describes the current implementation architecture of the ILS application in `ILS-dev`.
It is grounded in the actual source files and route mounting behavior of the backend and the frontend.

## System overview

The ILS application is split into two repositories:

- `ILS-dev/backend` — Node.js + Express backend with Sequelize model loading and JSON APIs
- `ILS-dev/frontend` — React 18 + Vite frontend with an admin-style SPA and teacher intelligence pages

The architecture is API-first and modular: the backend exposes `/api/*` JSON endpoints, and the frontend consumes those endpoints through a shared API client.

### Architecture at a glance

| Layer | Components | Role |
|---|---|---|
| Backend | Node.js, Express, Sequelize, PostgreSQL | Data storage, API routing, model associations, grading and reporting logic |
| Frontend | React 18, Vite, Tailwind CSS | Admin UI, teacher cockpit, heatmap, and forms |
| Data model | Vertical hierarchy + horizontal intelligence | Curriculum structure, outcome mapping, and mastery reporting |

The documentation repository `ILS-doc` is separate and reads the application code for factual reference only.

## Backend architecture

The backend starts in `ILS-dev/backend/index.js`.

Key implementation points:

- `dotenv` loads `backend/.env` and `DATABASE_URL` is required.
- `Sequelize` connects to PostgreSQL and `initModels()` dynamically imports models from `backend/models/*.js`.
- Model associations are defined in `backend/models/index.js` after all model factories are loaded.
- All API routes mount under `/api` and the app injects the Sequelize models into `req.models` before each router.
- JSON responses are serialized with a custom BigInt-safe replacer so `BigInt` values are converted to strings.
- A lightweight CORS policy allows the frontend origin configured by `CORS_ORIGIN` or `*` in development.
- `requireAuth` protects all routes except `/api/health` and `/api/auth`.
- The backend is intentionally modular, with each route file responsible for a specific entity or feature area.

The backend does not use `sequelize.sync()` in the main startup flow.
Migrations and the database schema are intended to be managed outside the runtime.

## Route structure

The backend exposes these top-level API groups:

- `GET /api/health`
- `POST /api/auth` and related auth routes
- `GET|POST|PUT|DELETE /api/institutions`
- `GET|POST|PUT|DELETE /api/campuses`
- `GET|POST|PUT|DELETE /api/courses`
- `GET|POST|PUT|DELETE /api/modules`
- `GET /api/modules/bank/outcomes`
- `GET /api/modules/bank/ref_teaching_methods`
- `GET /api/modules/bank/assignments`
- `GET|POST|PUT|DELETE /api/assignments`
- `GET|POST|PUT|DELETE /api/themes`
- `GET|POST|PUT|DELETE /api/outcomes`
- `GET|POST|PUT|DELETE /api/outcome-categories`
- `GET /api/frameworks`
- `GET /api/reference`
- `GET|POST|PUT|DELETE /api/rubrics`
- `GET /api/rubrics/categories`
- `GET /api/rubrics/criteria`
- `GET /api/grading/*`
- `GET /api/heatmap/*`
- `GET /api/cockpit/summary`
- `GET|POST|PUT|DELETE /api/classes`
- `/api/admin/*` maintenance routes
- `GET /api/matrix`
- `GET /api/assessment-types`
- `GET /api/periods`

### Backend route categories

| Category | Example paths | Purpose |
|---|---|---|
| Curriculum management | `/api/institutions`, `/api/courses`, `/api/modules`, `/api/assignments` | Create and maintain the vertical curriculum structure |
| Learning intelligence | `/api/themes`, `/api/outcomes`, `/api/rubrics`, `/api/frameworks` | Manage reusable outcome, rubric, and mastery metadata |
| Grading and reporting | `/api/grading/*`, `/api/heatmap/*`, `/api/cockpit/summary` | Capture scores, compute mastery, and summarize classroom health |
| Class delivery | `/api/classes`, `/api/users`, `/api/periods` | Manage classes, enrollment, and scheduling context |
| Administration | `/api/admin/*`, `/api/reference`, `/api/matrix` | Back-office maintenance and lookup data |

The homepage route definitions are located in `ILS-dev/frontend/src/App.jsx`.
That file defines the teacher and admin SPA routes, including:

- `/admin/...` admin pages
- `/courses/:courseId/modules/:moduleId/assignments/...` assignment editor paths
- `/admin/grading`
- `/admin/heatmap`
- `/admin/classroom-intelligence`
- `/admin/student-cockpit`

## Core model architecture

The app separates two domains:

- Vertical curriculum structure:
  - `institutions`, `campuses`, `courses`, `modules`, `assignments`, `classes`
- Horizontal intelligence layer:
  - `themes`, `outcomes`, `rubrics`, `rubric_criteria`, `rubric_ratings`, `student_outcome_snapshots`

The module is the central hub of the vertical hierarchy. Assignments belong to modules, and classes are the enrollment context for a module.

## Development & Architecture Rules

The ILS implementation follows a strict set of architectural rules to keep the system stable and consistent.

| Rule | Why it matters |
|---|---|
| Vertical hierarchy only through ownership | Keeps structure clear and avoids orphan entities |
| Assignments belong only to modules | Preserves the module hub as the authoritative owner of work items |
| Modules belong only to courses | Prevents cross-course ownership and keeps curriculum clean |
| Horizontal intelligence is global | Makes themes, outcomes, and rubrics reusable across courses |
| Use explicit junctions for links | Decouples intelligence data from ownership and enables flexible mapping |
| No nesting of intelligence entities | Keeps the model normalized and easier to maintain |
| No new tables without approval | Protects the stabilization phase from uncontrolled schema drift |
| Database schema is the source of truth | Ensures application code matches actual database structure |
| Environment-driven configuration | Avoids hardcoded database credentials and makes deployments safe |
| UI/API contract first | Keeps the frontend aligned with live backend behavior |

## Model Definitions & Associations

The backend defines Sequelize models in `backend/models/*.js` and initializes associations in `backend/models/index.js`.

Model conventions include:

- `id` is `BIGINT` and auto-incrementing for primary keys.
- `deleted_at` is used for soft deletes and models are configured with `paranoid: true`.
- `created_at` and `updated_at` are standard timestamp fields.
- `underscored: true` maps JavaScript camelCase to snake_case database columns.
- `defaultScope` typically filters out soft-deleted records by requiring `deleted_at IS NULL`.

Association patterns include:

- `hasMany` / `belongsTo` for one-to-many relationships.
- `belongsToMany` through junction models for many-to-many relationships.
- Junction tables are modeled explicitly and used for decoupling intelligence entities from the vertical hierarchy.

The code uses explicit association aliases such as `Module.hasMany(ModuleStructureRow, { as: 'structures' })` and `Module.belongsToMany(Outcome, { through: ModuleLearningOutcome, as: 'outcomes' })` to make relationship usage readable in queries.

### Main backend associations

The model associations defined in `backend/models/index.js` include:

- `Course.hasMany(Module)` and `Module.belongsTo(Course)`
- `Module.hasMany(Assignment)` and `Assignment.belongsTo(Module)`
- `Module.belongsToMany(Theme)` via `ModuleTheme`
- `Module.belongsToMany(Outcome)` via `ModuleLearningOutcome`
- `Assignment.belongsToMany(Rubric)` via `AssignmentRubric`
- `Rubric.hasMany(RubricCriterion)` and `RubricCriterion.belongsTo(Rubric)`
- `RubricCriterion.hasMany(RubricRating)` and `RubricRating.belongsTo(RubricCriterion)`
- `RubricCriterion.belongsTo(Outcome)` through `linked_outcome_id`
- `User.hasMany(Submission)` and `Submission.belongsTo(User)`
- `Submission.belongsTo(Assignment)` and `Assignment.hasMany(Submission)`
- `Submission.belongsTo(Class)` and `Class.hasMany(Submission)`
- `StudentOutcomeSnapshot.belongsTo(Outcome)`, `Class`, `User`, and `Submission`

### Snapshot and intelligence tables

The key intelligence artifact is `student_outcome_snapshots`.
It stores the most recent mastery score per student, outcome, and class, and it is the source of truth for the heatmap and classroom cockpit reports.

## Backend intelligence flow

The core intelligence flow is implemented in `/api/grading` and `/api/heatmap`.

### Grading flow

`POST /api/grading/submissions/:submissionId/score` is the primary grading endpoint.
It:

- upserts `submission_criterion_scores` for each rubric criterion
- computes the submission total score from selected ratings
- marks grading status as `complete` when the run is finalized
- updates `submissions.overall_score` and `submissions.grade_status`
- writes outcome snapshots in the same transaction using `backend/lib/snapshotWriter.js`

The flow supports two assessment modes:

- `simple` mode finalizes grading immediately
- `advanced` mode allows draft saves and explicit finalization

### Heatmap flow

`GET /api/heatmap/classes/:classId` builds the classroom heatmap by:

- selecting outcomes linked to rubric criteria used by assignments in the class
- loading the most recent non-stale `student_outcome_snapshots`
- detecting pending ungraded submissions for linked outcomes
- optionally enriching the response with trend data when `includeTrends=true`

### Cockpit flow

`GET /api/cockpit/summary` aggregates class and student health metrics using:

- class reporting rules from `campus_reporting_rules`
- pending submission counts and overdue work from `submissions`
- outcome mastery snapshots from `student_outcome_snapshots`
- student trend averages computed from snapshot history

## Frontend architecture

The frontend uses React Router in `ILS-dev/frontend/src/App.jsx` and a single-page admin UI design.

Important frontend entrypoints:

- `frontend/src/pages/GradingPage2.jsx` — grading cockpit and student submission selection
- `frontend/src/pages/HeatmapPage.jsx` — outcome mastery matrix
- `frontend/src/pages/ClassroomIntelligencePage.jsx` — report summary and recommendation logic
- `frontend/src/pages/StudentCockpitPage.jsx` — teacher task prioritization and student risk list
- `frontend/src/pages/RubricsPage.jsx` and `frontend/src/pages/RubricEditor.jsx` — rubric management
- `frontend/src/pages/AssignmentForm.jsx` — assignment builder with rubric selection
- `frontend/src/pages/ModuleForm.jsx` — module edit flow with outcomes, teaching methods, and structures

The shared API client is `frontend/src/lib/api.js`, which prefixes requests with `/api` and attaches the stored JWT token.

## Developer implications

- Backend route behavior should be audited against `backend/routes/*.js` for exact contract expectations.
- The frontend UI is tightly coupled to the backend route payload shapes in the grading, heatmap, and admin pages.
- `student_outcome_snapshots` is the canonical data source for reporting; it should be treated as the consistency layer for heatmap and cockpit results.

## Navigation and documentation

This architecture page is the entry point for the developer guide. It is intentionally tied to the live code in `ILS-dev` and does not describe future or unimplemented features.


**Last updated:** 2026-07-08

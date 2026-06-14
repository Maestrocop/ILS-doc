# Progression Review (BSA) — Implementation Summary

This page documents what exists in the codebase for the Progression Review (BSA) feature. It is a factual, read-only summary of implemented models, API routes, scripts, and frontend pages. No recommendations or troubleshooting guidance are included.

## Backend: models
- `ProgressionReviewDefinition` (backend/models/ProgressionReviewDefinition.js)
  - Stores review type configuration (local_name, description, trigger_months, is_binding, applicable_year, available_outcomes, is_active, thresholds, decision stages).

- `ProgressionReviewInstance` (backend/models/ProgressionReviewInstance.js)
  - Represents a single student's review file (definition_id, student_id, class_id, review_owner_id, slb_id, status, recommendation, decision, decision_reason, due_date, appeal fields, timestamps, paranoid deletes).

- `StudentOutcomeSnapshot` (backend/models/studentOutcomeSnapshot.js)
  - Snapshot entity where outcome mastery scores are written; used by snapshotWriter and related backfill scripts.

## Backend: core libraries and scripts
- `backend/lib/reviewDefinition.js`
  - Helpers to resolve the active `ProgressionReviewDefinition` for a given class and to obtain thresholds.

- `backend/lib/snapshotWriter.js`
  - Centralised writer for outcome snapshots. Implements `writeOutcomeSnapshots`, `writeQuizOutcomeSnapshots`, and `writeProjectTaskOutcomeSnapshots`. Aggregates evidence from assignments, quizzes, and project tasks and writes `student_outcome_snapshots`, `sos_evidence`, and `sos_params` as appropriate.

- `backend/scripts/seed_progression_definition.cjs`
  - Seed script that inserts a BSA progression review definition (example BSA definition with decision policy) and the associated `progression_review_decision_policies` row.

- `backend/scripts/backfill_outcome_snapshots.cjs`
  - Backfill script to populate `student_outcome_snapshots` from historical graded submissions; idempotent and safe to preview before running.

## Backend: API routes
All routes are mounted under `/api/progression-reviews` and enforce role-based access.

- `GET /api/progression-reviews/definitions`
  - Returns progression review definitions (scoped to institution unless admin requests `all=true`). Includes attached `decisionPolicy` when present.

- `POST /api/progression-reviews/definitions` (admin)
  - Create a new review definition (optionally with a decision policy).

- `PUT /api/progression-reviews/definitions/:id` (admin)
  - Update an existing definition and its `decisionPolicy`.

- `GET /api/progression-reviews/definitions/:id/event-types`
  - Returns event types associated with a definition (timeline events such as meetings, warnings, decisions).

- Coordinator / dashboard endpoints:
  - `GET /api/progression-reviews/coordinator-stats` — cohort-level KPIs, pass rates, status distributions, scatter data, and lists used by coordinator dashboards.
  - `GET /api/progression-reviews/slb-stats` — stats and lists scoped to the logged-in SLB/owner (personal dashboard).

- Policy enforcement helper:
  - `checkDecisionPolicy(models, instanceId, decision)` — server-side check that blocks issuing a negative decision (e.g., `transfer`, `exit`) if required evidence (warning, intervention, student acknowledgment) is missing according to the definition's `decisionPolicy`.

## Backend: alerts & reports
- `backend/routes/alerts.js`
  - Coordinator-facing alert endpoints such as `coordinator/:coordinatorId/overdue-reviews`, `coordinator/:coordinatorId/students-no-advisor`, and `coordinator/:coordinatorId/grading-backlog`. Uses helper `getCourseIdFilter` to scope results.

## Frontend: pages and components
- `frontend/src/pages/ProgressionReviewsPage.jsx`
  - Admin/Coordinator listing of progression reviews, creation modal, filters, KPIs, and table UI.

- `frontend/src/pages/MyBSAReviewPage.jsx`
  - Student-facing review page showing status, progress summary, actions, and acknowledgments.

- `frontend/src/pages/BSACoordinatorDashboard.jsx`
  - Coordinator dashboard with KPIs, donut/bar charts, coverage stats, and backlog display.

- `frontend/src/components/ProgressionReviewDefinitionsTab.jsx`
  - UI for creating and editing review definitions, event types, action types, decision stages, thresholds, and policy text/document uploads.

## Data & Policy
- Decision stages and thresholds are stored on `ProgressionReviewDefinition` (fields like `decision_stages`, `warning_threshold`, `decision_threshold`, `is_binding`).
- Decision-policy flags (require_warning, require_intervention, require_acknowledgment) are stored in `progression_review_decision_policies` and enforced by server-side checks before allowing certain negative or binding decisions.

## Seeds and migrations
- A seed (`backend/scripts/seed_progression_definition.cjs`) exists to create a canonical BSA definition and attach a decision policy. Migration files and model definitions are the source of truth for schema (DB-first policy).

## Where to find the source files (examples)
- `ILS-dev/backend/routes/progressionReviews.js`
- `ILS-dev/backend/models/ProgressionReviewDefinition.js`
- `ILS-dev/backend/models/ProgressionReviewInstance.js`
- `ILS-dev/backend/lib/reviewDefinition.js`
- `ILS-dev/backend/lib/snapshotWriter.js`
- `ILS-dev/backend/scripts/seed_progression_definition.cjs`
- `ILS-dev/backend/scripts/backfill_outcome_snapshots.cjs`
- `ILS-dev/frontend/src/pages/ProgressionReviewsPage.jsx`
- `ILS-dev/frontend/src/pages/MyBSAReviewPage.jsx`
- `ILS-dev/frontend/src/pages/BSACoordinatorDashboard.jsx`
- `ILS-dev/frontend/src/components/ProgressionReviewDefinitionsTab.jsx`

## Validation and notes
- This document describes existing code and artifacts only. All writable documentation edits are under `ILS-doc/docs/`.

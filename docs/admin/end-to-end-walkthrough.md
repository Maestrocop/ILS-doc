# Progression Review — End-to-End Walkthrough (what exists)

This document describes the existing end-to-end flow implemented in the codebase for progression reviews (BSA). It is a read-only summary of the sequence of components and data flows; it does not propose changes.

1. Definition creation
   - Admins create a `ProgressionReviewDefinition` via `POST /api/progression-reviews/definitions` or the `ProgressionReviewDefinitionsTab` UI.
   - Definitions include decision stages, thresholds, evidence policy codes, and optional PDF policy documents. A `progression_review_decision_policies` row may be created alongside the definition.

2. Seeding / Backfill (optional ops)
   - The repository includes `backend/scripts/seed_progression_definition.cjs` to insert a canonical BSA definition and `backend/scripts/backfill_outcome_snapshots.cjs` to generate historical `student_outcome_snapshots`.

3. Triggering a review
   - Reviews can be started manually via the UI (`ProgressionReviewsPage`) or programmatically by institution logic (not modified here).
   - Creating a `ProgressionReviewInstance` stores student, class, owner, status, due_date, and policy-related fields.

4. Evidence aggregation and snapshots
   - When graded submissions, quizzes, or project tasks are processed, `backend/lib/snapshotWriter.js` writes outcome snapshots via `writeOutcomeSnapshots`, `writeQuizOutcomeSnapshots`, and `writeProjectTaskOutcomeSnapshots`.
   - Snapshots are stored in `student_outcome_snapshots` and related evidence rows are written to `sos_evidence` and `sos_params`.

5. Dashboards and coordinator views
   - Coordinator and SLB dashboards fetch cohort stats from `GET /api/progression-reviews/coordinator-stats` and `/slb-stats`.
   - Frontend pages `BSACoordinatorDashboard.jsx` and `ProgressionReviewsPage.jsx` display KPIs, status distributions, per-program charts, and lists used for actioning reviews.

6. Actions, events, and improvement plans
   - Event types and action types are defined per `ProgressionReviewDefinition` and managed via the `ProgressionReviewDefinitionsTab` UI.
   - Actions and timeline events are stored on the review instance (models and API endpoints manage create/update of actions and events).

7. Decision policy enforcement
   - Before issuing a negative or binding decision (e.g., `transfer`, `exit`), server-side helper `checkDecisionPolicy` verifies required evidence (warning, intervention, acknowledgment) exists per the definition's policy.

8. Final decision and recording
   - Decisions are recorded on `ProgressionReviewInstance` (`decision`, `decision_reason`, `decided_at`). Frontend pages show status and decision labels to users and coordinators.

9. Alerts and reports
   - Alerts endpoints (`backend/routes/alerts.js`) provide coordinator-scoped reports (overdue reviews, students without advisors, grading backlog) used by dashboards.

Source files referenced (examples):
- `ILS-dev/backend/models/ProgressionReviewDefinition.js`
- `ILS-dev/backend/models/ProgressionReviewInstance.js`
- `ILS-dev/backend/lib/snapshotWriter.js`
- `ILS-dev/backend/routes/progressionReviews.js`
- `ILS-dev/backend/scripts/seed_progression_definition.cjs`
- `ILS-dev/backend/scripts/backfill_outcome_snapshots.cjs`
- `ILS-dev/frontend/src/pages/ProgressionReviewsPage.jsx`
- `ILS-dev/frontend/src/pages/BSACoordinatorDashboard.jsx`
- `ILS-dev/frontend/src/pages/MyBSAReviewPage.jsx`
- `ILS-dev/frontend/src/components/ProgressionReviewDefinitionsTab.jsx`

This is a factual walkthrough of implemented components only; no changes are made to `ILS-dev`.

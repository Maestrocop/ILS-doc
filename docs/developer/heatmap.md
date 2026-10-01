# Heatmap

This page documents the current developer implementation of the classroom heatmap feature in `ILS-dev`.
The heatmap is a teacher-facing matrix that shows student mastery scores for each linked outcome in a class.

## Frontend entrypoint

The heatmap page is mounted at `/admin/heatmap` in `frontend/src/App.jsx`.
The page implementation is in `frontend/src/pages/HeatmapPage.jsx`.

## Backend data source

The frontend loads heatmap data from:

- `GET /api/heatmap/classes/:classId`
  - optional query param: `moduleId`
  - returns `outcomes`, `students`, and `summary`

The page also uses:

- `GET /api/heatmap/classes/:classId/drilldown` for assignment-level evidence when a user drills down on a student-outcome cell.

## Key data flows

### Outcome columns

The heatmap builds outcome columns from rubric criteria linked to assignments in the selected class.
This is resolved in the backend by joining:

- `submissions`
- `assignment_rubrics`
- `rubric_criteria`
- `outcomes`
- `assignments`

If `moduleId` is supplied, the backend filters the columns to outcomes used by that module's assignments.

### Student mastery data

Student rows are built from enrolled class students plus their latest outcome snapshot scores.
The backend returns a `scores` object for each student, keyed by `outcome_id`.
These scores come from `student_outcome_snapshots` and are the canonical mastery values for the heatmap.

### Pending work and evidence

The heatmap API includes pending submissions for ungraded outcome-linked work.
In the frontend, heatmap cells can indicate:

- graded scores from outcome snapshots
- pending grading status for ungraded submissions
- drilldown navigation to the student/outcome evidence view

### Summary metrics

The `summary` payload from the backend includes:

- `total_submissions`
- `graded`
- `pending`
- `avg_score`
- `at_risk_count`

The frontend uses these values to show overall class grading coverage and at-risk density.

## Frontend behavior

Key developer behaviors in `HeatmapPage.jsx`:

- loads `classId` and optional `moduleId` from the URL search params
- fetches the heatmap payload via `fetchApi('/heatmap/classes/:classId')`
- computes cell styles based on score ranges and pending status
- renders the outcome matrix with score colors and tooltips
- uses `evaluateMatrixStatus` from `frontend/src/utils/matrixEvaluator` to derive additional status labels
- supports drilldown to `/api/heatmap/classes/:classId/drilldown` for student/outcome evidence

## Developer implications

- Heatmap relies on the stability of `students[].scores` and `outcomes` in the API contract.
- Changing the shape of `student_outcome_snapshots` or the heatmap endpoint will affect both `HeatmapPage.jsx` and `ClassroomIntelligencePage.jsx`.
- The heatmap is primarily a read-only report; it does not write grades or snapshots.

## Related developer content

- `docs/developer/classroom-intelligence.md` — interpretation layer built on heatmap data
- `docs/developer/api.md` — heatmap backend route contract
- `docs/developer/data-model.md` — snapshot and outcome relationships


**Last updated:** 2026-07-08

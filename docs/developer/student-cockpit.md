# Student Cockpit

This page documents the current developer implementation of the Student Cockpit feature in `ILS-dev`.
The Student Cockpit is the teacher-facing action dashboard for identifying at-risk students and grading priorities.

## Frontend entrypoint

The Student Cockpit route is mounted at `/admin/student-cockpit` in `frontend/src/App.jsx`.
The page implementation is in `frontend/src/pages/StudentCockpitPage.jsx`.

## Backend and supporting API calls

The page loads these backend endpoints:

- `GET /campuses` — campus list for the filter UI
- `GET /grading/classes` — available classes for the teacher
- `GET /periods?active=true` — current academic periods
- `GET /api/cockpit/summary` — main student/class health payload
- `GET /api/heatmap/classes/:classId?includeTrends=true` — per-student outcome trends for the student detail panel

## Main data flow

### Cockpit summary

The page fetches `GET /api/cockpit/summary` with optional query params:

- `campusId`
- `periodId`
- `classIds` (comma-separated)

The returned payload includes:

- `pulse` — overall counts for at-risk, inactive, pending, and flagged classes
- `classes` — class health rows with thresholds, counts, and health state
- `at_risk_students` — prioritized student action rows

### Student action table

The Student Cockpit displays an action table of `at_risk_students`.
Each student row includes:

- average score
- pending submission count
- overdue assignment count
- outcome score list
- risk level (`At Risk`, `Borderline`, `Safe`)
- teacher task recommendation such as `Grade submission`, `Intervention`, or `Monitor`

The page supports filtering by:

- scope view: teacher vs manager
- campus
- academic period
- selected class(es)
- action type

### Trend and risk interpretation

The Student Cockpit uses trend direction to show how a student’s mastery trajectory is moving between snapshots.
- A stable trend means the most recent snapshot average is essentially unchanged from the prior snapshot.
- Stable does not mean the student is doing well. A student can be stable at 3.3 and still be below the success threshold.
- The backend can flag this as a stagnant risk type when a student is both stable and below threshold.

### Student detail panel

When a teacher opens a student row, the cockpit loads additional details from:

- `GET /api/heatmap/classes/:classId?includeTrends=true`

The detail panel computes:

- per-outcome scores and trend direction
- target gap relative to the class success threshold
- class-average comparison for each outcome
- hidden risk when a student’s average is acceptable but some outcomes are critically low

## Frontend behavior

Key developer behaviors in `StudentCockpitPage.jsx`:

- syncs `view`, `campusId`, `periodId`, and `classIds` into the URL search params
- uses `fetchApi()` for all backend calls
- derives filtered student lists and action counts from the cockpit payload
- builds a `classLookup` map from returned class rows
- renders a modal-style student intelligence panel for detailed student scoring context
- links from student detail into the full heatmap page

## Developer implications

- The cockpit depends on the `cockpit/summary` contract for its top-level view.
- It also depends on `heatmap/classes/:classId?includeTrends=true` for trend details in the student panel.
- Changes to student risk state, teacher task labels, or score thresholds should be mirrored in both backend summary logic and the frontend UI.

## Related developer content

- `docs/developer/classroom-intelligence.md` — cohort interpretation and intervention guidance
- `docs/developer/heatmap.md` — the heatmap report that backs the cockpit and intelligence pages
- `docs/developer/api.md` — backend contracts for cockpit, heatmap, and grading routes


**Last updated:** 2026-07-08

# Classroom Intelligence

This page documents the current developer implementation of the Classroom Intelligence feature in `ILS-dev`.
It is a frontend interpretation layer built on top of the heatmap data returned by the backend.

## What Classroom Intelligence is

Classroom Intelligence is the teacher-facing report that interprets outcome mastery and cohort health.
It lives at the frontend route `/admin/classroom-intelligence` and is implemented in `frontend/src/pages/ClassroomIntelligencePage.jsx`.

The page does not compute raw mastery from rubric scores itself. Instead, it combines:

- heatmap data from `GET /api/heatmap/classes/:classId`
- class metadata from `GET /api/classes/:id`
- campus reporting rules from `GET /api/campuses/:campusId/reporting-rules`
- course/module context from `GET /api/modules`
- the list of classes from `GET /api/grading/classes`

## Frontend entrypoints

The route is mounted in `frontend/src/App.jsx`:

- `Route path="admin/classroom-intelligence" element={<ClassroomIntelligencePage />} />`

The main page file is:

- `frontend/src/pages/ClassroomIntelligencePage.jsx`

The page also depends on configuration and rules in:

- `frontend/config/intelligence.config.js`

## Feature data flow

### Step 1: class and module selection

The page loads the teacher-visible class list from `GET /api/grading/classes`.
Once a class is selected, it loads class details from `GET /api/classes/:id` and the campus reporting rules from `GET /api/campuses/:campusId/reporting-rules`.

If the class belongs to a course with multiple modules, the page also loads `/api/modules` and allows the teacher to filter the report by module.

### Step 2: heatmap data source

Classroom Intelligence pulls the main classroom state from:

- `GET /api/heatmap/classes/:classId`
- optional query param: `moduleId`

This endpoint returns:

- `outcomes` — outcome columns linked to graded assignments in the class
- `students` — enrolled students with `scores` by `outcome_id`
- `summary` — overall submissions, graded/pending counts, average score, and `at_risk_count`

The score values are loaded from `student_outcome_snapshots`, which is the canonical mastery snapshot table in the backend.

### Step 3: client-side intelligence

The classroom intelligence page computes higher-level insights from the heatmap payload.
It derives:

- per-outcome breakdown rows (worst-first), including class average and percent-below-threshold
- weak-area severity labels for each outcome (`critical`, `warning`, `watch`, `ok`)
- weak-area alert cards for outcomes in `critical` or `warning` state
- cohort readiness and threshold risk
- confidence labels based on graded student coverage
- pattern detection such as polarized cohorts, technical gaps, and recovery potential
- teaching insights from outcome category averages and threshold sensitivity
- suggested interventions based on triggered patterns and threshold pressure

The page also supports an explain mode that reveals the rule IDs, expressions, and evidence values used by each insight.

### Outcome breakdown implementation (current)

The page computes `outcomeStats` directly from heatmap `students[].scores` and `outcomes` in `frontend/src/pages/ClassroomIntelligencePage.jsx`.

- `avg`: mean score per outcome for students with numeric scores
- `belowPct`: percentage of scored students below `reportingRules.success_threshold`
- `belowCount` and `count`: denominator and below-threshold count used in the UI
- `severity` thresholds:
	- `critical` when `belowPct >= 60`
	- `warning` when `belowPct >= 40`
	- `watch` when `belowPct >= 20`
	- `ok` otherwise

The rendered section title is currently: `Outcome Breakdown — Weak Area Highlights`.

## What the page does not do

- It does not call `GET /api/cockpit/summary`.
- It does not build individual student risk statuses directly from submissions.
- It does not write snapshots or grades.

The student cockpit and classroom intelligence pages are separate UX layers:

- `GET /api/cockpit/summary` is used by the student cockpit for at-risk student prioritization.
- `GET /api/heatmap/classes/:classId` is the main backend source for Classroom Intelligence.

## Developer implementation notes

- The Classroom Intelligence page is largely client-side logic.
- The backend heatmap API returns outcome scores and pending submission references, but the pattern detection and suggested interventions are computed in the browser.
- When extending Classroom Intelligence, update both the frontend rule config in `frontend/config/intelligence.config.js` and the page's derived logic in `frontend/src/pages/ClassroomIntelligencePage.jsx`.
- The heatmap payload must remain stable for this page; any contract changes to `students[].scores`, `outcomes`, or `summary` should be coordinated with this implementation.

## Related pages

- `docs/developer/workflows.md` — general grading, heatmap, and cockpit lifecycle documentation
- `docs/developer/api.md` — backend API contracts for heatmap and cockpit endpoints
- `docs/developer/architecture.md` — system architecture and intelligence flow context


**Last updated:** 2026-07-08

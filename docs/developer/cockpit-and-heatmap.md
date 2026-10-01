# Cockpit & Heatmap APIs

This page documents the Teacher-facing intelligence endpoints used by the Teacher Dashboard, Student Cockpit, and the Heatmap grid. All content is a read-only extraction from `ILS-dev/backend/routes/cockpit.js` and `ILS-dev/backend/routes/heatmap.js`.

Security

- All endpoints require authentication and teacher/coordinator role (`requireRole('teacher','coordinator')`).

Data sources and assumptions

- Mastery scores come from `student_outcome_snapshots` (the single source of truth). These snapshots are produced by the snapshot writer and are used across cockpit and heatmap views.
- Assignment/Submission scores (`submissions.overall_score`) are used for some fast aggregations (briefing/pulse).
- Outcome columns shown in the heatmap may be filtered by `moduleId`, but mastery values are always the full class-level snapshot for that outcome.

Cockpit endpoints

1. GET /api/cockpit/summary
- Query params: `campusId` (optional), `periodId` (optional), `classIds` (optional, comma-separated)
- Returns: `{ pulse, classes, at_risk_students }`
  - `pulse`: totals (total_at_risk, total_inactive, total_pending, classes_flagged)
  - `classes`: array of class health objects (class_id, class_code, class_name, total_students, at_risk_count, inactive_count, pending_count, below_threshold_pct, health)
  - `at_risk_students`: prioritized flat list of exception students with metadata, derived fields, trend, and drill links.

Notes:
- Uses `student_outcome_snapshots` for mastery and `submissions.overall_score` as a quick scoring proxy.
- Produces teacher-facing `teacher_task` hints (e.g., "Grade submission", "Intervention").

2. GET /api/cockpit/dashboard
- Query params: `classIds` (required; comma-separated)
- Returns: `{ briefing, classes, risk_watchlist, ghost_students, action_inbox, outcome_gaps, class_vector }`
  - `briefing`: counts like `critical_decline_count`, `pending_grades_count`, etc.
  - `classes`: per-class cards with sparkline arrays, trend distributions and health.
  - `action_inbox`: pending assignment/quiz submissions ranked by age (for grading inbox).

3. GET /api/cockpit/outcome-submissions?classId=&userId=&outcomeId=
- Returns the graded submissions that contributed to a student's outcome score.
- Response rows include `submission_id`, `assignment_id`, `assignment_title`, `submitted_at`, `overall_score`, `outcome_score`, `criterion_count`.

4. GET /api/cockpit/student-panel?classId=&userId=
- Full intelligence payload for one student in a class.
- Returns: student metadata, `avg_score`, `risk_level`, `trend_direction`, `pending_count`, `overdue_count`, `outcome_scores` (array), recency labels, and class summary info.

5. GET /api/cockpit/class-panel?classId=
- Full diagnostic payload for a single class: stats, campus benchmark (this class vs campus), outcome gaps, assignment autopsy (worst assignments per outcome), ghost students, top performers, and 4-week sparkline.

6. GET /api/cockpit/quiz-outcomes?classId=&userId=
- Returns latest quiz-derived snapshots per outcome for a student in a class. Useful for formative pulse and showing recent quiz evidence.

Implementation notes (Cockpit)

- Trend classification helpers (`classifyTrendDirection`, `classifyTrendConfidence`) convert snapshots into `up|down|flat|unknown` and a confidence estimate.
- Many payloads include both `score` (0–10) and `overall_score` (submission-level 0–100 numeric stored as overall_score). UI clients frequently normalize these to display scales.
- Action ordering and prioritization are deterministic: `Grade submission` > `Intervention` > `Follow up overdue` > `Monitor` > `No immediate task`.

Heatmap endpoints

1. GET /api/heatmap/classes/:classId
- Query params:
  - `moduleId` (optional) — filters which outcome *columns* are shown (based on rubric criteria used in assignments for that module)
  - `includeTrends=true` (optional) — when present, returns per-cell trend info (direction, delta)
- Returns: `{ outcomes, students, summary }`
  - `outcomes`: array of outcome column metadata (id, code, friendly_name, category_id, category_name, category_color)
  - `students`: array of student rows: `{ user_id, name, student_number, last_submission_at, scores: { [outcome_id]: score_0_to_10 | null }, submissions: { [outcome_id]: { submission_id, grade_status } } }`
  - `summary`: totals (total_submissions, graded, pending, avg_score, at_risk_count)

Important behavior (Heatmap)

- Mastery scores are read from `student_outcome_snapshots` (most-recent non-stale snapshot). Scores are already computed by snapshotWriter and returned as numbers on a 0–10 scale (rounded to 1 decimal when used in responses).
- The `moduleId` parameter controls which outcomes appear as columns (via assignment→rubric→criterion→linked_outcome); however, mastery values are class-level snapshots regardless of module filter.
- Cells may include `submissions` entries for both graded and pending submissions; pending cells have `grade_status` and `submission_id` so the UI can deep-link into grading workflows.
- At-risk counting uses a cutoff of `< 4.0` on outcome scores (any student with at least one outcome < 4.0 is included in `at_risk_count`).

2. GET /api/heatmap/classes/:classId/drilldown?outcomeId=&userId=&moduleId=
- Query params: `outcomeId` (required), `userId` (required), `moduleId` (optional)
- Returns: `{ rows: [{ assignment_title, criterion_title, score, max_score }] }` — used to show criterion-level contributions for a student's outcome.

Examples

Cockpit summary (abridged):

```json
{ "pulse": { "total_at_risk": 12, "total_inactive": 5, "total_pending": 7, "classes_flagged": 1 }, "classes": [ /* class cards */ ], "at_risk_students": [ /* prioritized list */ ] }
```

Heatmap classes (abridged):

```json
{
  "outcomes": [{ "id": 11, "code": "OC.1", "friendly_name": "Research" }],
  "students": [
    { "user_id": 201, "name": "A Student", "scores": { "11": 7.5, "12": 4.0 }, "submissions": { "11": { "submission_id": 900, "grade_status": "graded" } } }
  ],
  "summary": { "total_submissions": 120, "graded": 95, "pending": 25, "avg_score": 7.2, "at_risk_count": 3 }
}
```

References (read-only)

- `ILS-dev/backend/routes/cockpit.js`
- `ILS-dev/backend/routes/heatmap.js`

If you want, I can:

- Add these pages to the MkDocs `nav` and run `mkdocs build --strict` to validate (I'll wait for explicit approval), or
- Expand any endpoint above into a full example request/response pair with realistic data drawn from the code.


**Last updated:** 2026-07-08

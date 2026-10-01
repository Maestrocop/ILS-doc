# Grading & Submissions API

This page documents the backend grading and submission-related endpoints used by the Teacher Grading Cockpit and related UIs. All details are read-only extracts from `ILS-dev/backend/routes/grading.js` and `ILS-dev/backend/routes/submissionFiles.js`.

Security

- All grading endpoints are mounted under `/api/grading` and require an authenticated user (`requireAuth`). The grading router uses `requireRole('teacher','coordinator')` so only teachers and coordinators (and admins) may access these routes.

Assessment mode

- The system supports two assessment modes: `simple` and `advanced`. The class-level assessment mode is read from the institution (if the `assessment_mode` column exists) and falls back to the server default.

Scoring algorithm (rubric-based assignments)

- The server stores per-criterion scores in `submission_criterion_scores` and computes an overall score as:
  - raw_score = SUM(selected criterion `score` values)
  - max_possible = SUM(max score per criterion)
  - overall_score = (raw_score / max_possible) * 100 (rounded to one decimal)
- When grading is finalized the server writes outcome snapshots via `writeOutcomeSnapshots()`.

Key endpoints

1. `GET /api/grading/classes`
- Purpose: Class picker for grading UI. Teachers see only their classes; admins see all.
- Response: array of classes with `assessment_mode`, `module_id`, `course_id`, etc.

Example response (abridged):

```json
[{ "id": 12, "name": "Class A", "module_id": 34, "module_title": "Intro", "course_id": 7, "assessment_mode": "simple" }]
```

2. `GET /api/grading/classes/:classId/assignments`
- Purpose: assignments in class (via module) with submission counts and linked rubric.
- Response fields: `assignment_id`, `assignment_title`, `points_possible`, `rubric_id`, `total_submissions`, `graded_count`, `ungraded_count`, plus `assessment_mode`.

3. `GET /api/grading/assignments/:assignmentId/classes/:classId/students`
- Purpose: list student submissions for a single assignment in a class.
- Response includes: `submission_id`, `status`, `grade_status`, `overall_score`, student `first_name`, `last_name`, and `scored_criteria_count`/`total_criteria_count`.

4. `GET /api/grading/classes/:classId/submissions`
- Purpose: flat list of all submissions for a class grouped by assignment (used by class-level grading views).

5. `GET /api/grading/submissions/:submissionId`
- Purpose: load full submission for grading UI.
- Response: `{ submission, criteria, assessment_mode }` where `submission` contains student, assignment, class metadata and `criteria` is an array of rubric criteria augmented with `ratings`.

Example response (abridged):

```json
{
  "submission": { "id": 987, "status": "submitted", "overall_score": null, "student_id": 201, "assignment_id": 123 },
  "criteria": [{ "criterion_id": 11, "criterion_title": "Research", "ratings": [{ "id": 101, "label": "Excellent", "points": 5 }] }],
  "assessment_mode": "simple"
}
```

6. `POST /api/grading/submissions/:submissionId/score`
- Purpose: Save rubric criterion scores (upsert semantics implemented as: delete-all → insert new set).
- Request body: `{ scores: [{ criterion_id, rating_id?, score?, grader_notes? }], grader_notes?, finalize? }`.
- Behavior:
  - If `scores` is empty → clears grade (sets `overall_score` NULL, `grade_status` 'pending', `status` 'draft').
  - Otherwise: inserts `submission_criterion_scores`, computes normalized overall score (0–100), updates `submissions` row, and on finalization writes outcome snapshots.

Example request:

```json
{
  "scores": [
    { "criterion_id": 11, "rating_id": 101, "score": 5 },
    { "criterion_id": 12, "rating_id": 103, "score": 3 }
  ],
  "grader_notes": "Good work overall",
  "finalize": true
}
```

Example response:

```json
{
  "submission_id": 987,
  "scored_criteria": 2,
  "total_criteria": 4,
  "overall_score": 85.5,
  "grade_status": "complete",
  "assessment_mode": "simple",
  "updated_at": "2026-05-25T12:34:56Z",
  "updated_by": 42
}
```

7. `PATCH /api/grading/submissions/:id/return`
- Purpose: teacher returns a graded submission to the student (`status` → `returned`). Enforced attempt limits.

8. Quiz-specific grading endpoints (manual open question grading)
- `GET /api/grading/classes/:classId/quizzes` — quizzes that need manual grading (counts).
- `GET /api/grading/quizzes/:quizId/classes/:classId/students` — students with quiz submission status.
- `GET /api/grading/quiz-submissions/:submissionId` — full Q&A detail + rubric criteria for manual grading.
- `POST /api/grading/quiz-submissions/:submissionId/grade` — submit manual open-answer scores: `{ answer_scores: [{ answer_id, score }] }`. Server recomputes overall score, finalizes submission, and writes quiz outcome snapshots.
- `PATCH /api/grading/quiz-submissions/:submissionId/return` — return a graded quiz to student.
- `PATCH /api/grading/quiz-submissions/:submissionId/reset` — reset a graded quiz to `submitted` and clear open-answer scores.

9. Submission file management (mounted under `/api/submissions`)

- `GET /api/submissions/:submissionId/files` — list files attached to a submission.
- `POST /api/submissions/:submissionId/files` — upload a file. Multipart form-field name: `file`. Allowed types: PDF, Word, Excel, PowerPoint, images, plain text.
- `GET /api/submissions/file/:fileId` — download or render file; token query param supported for browser embedding.
- `DELETE /api/submissions/file/:fileId` — delete a file (soft DB delete and best-effort disk cleanup).

Example upload response (abridged):

```json
{ "id": 321, "original_name": "essay.pdf", "mime_type": "application/pdf", "size_bytes": 234567, "uploaded_at": "2026-05-25T10:11:12Z" }
```

Implementation notes & gotchas

- Grading endpoints use an explicit delete-then-insert model for criterion scores to simplify deselection handling.
- Finalization behavior depends on the `assessment_mode` (some modes may require explicit `finalize=false` semantics); the server computes an effective finalize flag.
- Outcome snapshots are written only when grading is finalized (both assignment and quiz flows).
- File uploads are limited to 20 MB and a whitelist of mime types/extensions.

References (read-only)

- `ILS-dev/backend/routes/grading.js`
- `ILS-dev/backend/routes/submissionFiles.js`


**Last updated:** 2026-07-08

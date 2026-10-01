# Student APIs (Dashboard & My Work)

This page documents the student-facing APIs (mounted under `/api/student`) used by the student UI: dashboard, my-work, course structure, assignments, quizzes, projects, and task submissions. All details are read-only extracts from `ILS-dev/backend/routes/student.js`.

Authentication

- All endpoints require an authenticated JWT session. Endpoints return `401` when not authenticated.

Common error cases

- `400` — missing required parameters
- `401` — not authenticated
- `403` — action forbidden (example: sequence lock preventing submission)
- `404` — resource not found
- `500` — server error

Key endpoints

1. GET /api/student/my-work
- Purpose: list enrolled classes and pending/graded assignments per class.
- Response: array of class objects each with an `assignments` array. Each assignment entry includes `assignment_id`, `assignment_title`, `points_possible`, `submission_id`, `submission_status`, `overall_score`, `submitted_at`.

2. GET /api/student/courses
- Purpose: list distinct courses the student is enrolled in.

3. GET /api/student/courses/:courseId/curriculum
- Purpose: return Period → Module list for the student's enrolled classes in the course. Frontend uses this to render curriculum pages lazily.

4. GET /api/student/courses/:courseId/enrolled-modules
- Purpose: returns `module_id` and `class_id` pairs for modules the student is enrolled in for the course.

5. GET /api/student/course-structure
- Purpose: full Period → Module → Assignment tree for the student's active enrollments. Each assignment includes the student's latest `submission` (if any).

6. GET /api/student/assignments/:assignmentId?classId=X
- Purpose: full assignment detail for the student: assignment metadata, rubric criteria with ratings, and the student's most-recent submission (if any).
- Notes: If `classId` is omitted the server attempts to auto-resolve the class from the student's enrollments where the assignment appears.

7. POST /api/student/submissions
- Purpose: create (or return existing) a draft submission for an assignment.
- Body: `{ assignment_id, class_id }` → returns `{ submission_id, status, overall_score, submitted_at }`. Returns `201` when created, or existing submission row if present.

8. PATCH /api/student/submissions/:id/submit
- Purpose: student submits a draft submission. Transitions `draft` → `submitted` and increments `attempt_number`.
- Behavior & validations:
  - Checks sequence locks: finds the `module_items` row for the assignment and class and computes locked items via `computeLockedItems(...)`. If the item is locked the server returns `403` with message "This item is locked. Complete the previous item first."
  - Respects `submission_attempts` on the assignment; returns `400` if max attempts reached.

9. GET /api/student/dashboard
- Purpose: aggregated student stats for their dashboard.
- Response shape (abridged):

```json
{
  "stats": { "total_assignments": 42, "graded": 10, "submitted": 3, "pending": 29, "avg_score": 7.4 },
  "recent_grades": [{ "assignment_title": "Essay", "overall_score": 85, "score10": 8.5 }],
  "outcomes": [{ "id": 11, "code": "OC.1", "name": "Research", "avg_score10": 7.1, "graded_count": 3 }]
}
```

10. GET /api/student/my-assessments
- Purpose: flat list of assignments across enrolled classes with submission status and scores (`submission_id`, `submission_status`, `overall_score`).

11. GET /api/student/my-quizzes
- Purpose: flat list of quizzes with last attempt (via LATERAL subquery). Returns `submission_id`, `submission_status`, `submission_score`, `attempt`, `submitted_at`.

12. Projects & task submissions
- `GET /api/student/my-projects` — list projects assigned to student's classes with per-project task progress and earned/possible totals.
- `GET /api/student/projects/:projectId` — project overview (auto-resolves `classId` when omitted), phases and tasks.
- `GET /api/student/projects/:projectId/tasks/:taskId` — task detail with rubric, ratings, student submission, files and criterion scores.
- `POST /api/student/task-submissions` — upsert a draft task submission. Body: `{ task_id, class_id, text_response? }`.
- `PATCH /api/student/task-submissions/:id` — autosave text_response (cannot edit when submitted/graded).
- `PATCH /api/student/task-submissions/:id/submit` — mark task submission as submitted.

File uploads for task submissions

- `POST /api/student/task-submissions/:id/files` — multipart upload; form field name `file`; allowed types: PDF, Word, Excel, PowerPoint, images, text; max 20 MB. Returns `201` with created file metadata.
- `DELETE /api/student/task-submissions/:id/files/:fileId` — delete a file (auth + ownership check).
- `GET /api/student/task-submissions/:id/files/:storedName` — download the file (auth + ownership check).

Module item lock awareness

- `GET /api/student/modules/:moduleId/items?classId=` — returns module items and computes `is_locked` for the current student using `computeLockedItems(sequelize, items, userId, classId)`. The `classId` query parameter is required for correct lock evaluation.

Implementation notes & cautions

- Many endpoints auto-resolve `classId` from the student's enrollments when omitted, but the frontend should pass `classId` when available for precise behaviour.
- Sequence locks are enforced server-side on submission; the frontend should read `/api/student/modules/:moduleId/items?classId=` to compute `is_locked` and surface UI affordances.
- Quizzes queries use `LATERAL` queries to fetch the most recent quiz attempt per class for the student.
- Deleted rows are generally filtered by `deleted_at IS NULL` in SQL queries.

References (read-only)

- `ILS-dev/backend/routes/student.js`


**Last updated:** 2026-07-08

# Events API (calendar & scheduling)

This document describes the event and calendar endpoints implemented in `ILS-dev/backend/routes/events.js`. It is a factual extraction of the current implementation and makes no changes to ILS‑dev.

Overview

- Primary route: `/api/events`
- Purpose: provide a unified calendar feed used by teacher, student and admin views. The endpoint returns computed events (assignment due/open, quiz/exam due), custom calendar events (with recurrence expansion), and academic calendar events expanded into per-day entries.

Authentication & permissions

- `GET /api/events` — public for authenticated/unauthenticated callers (the code requires `from`/`to` but does not require req.user to be set; student/teacher/class filters are supported).
- `POST /api/events`, `PATCH /api/events/:id`, `DELETE /api/events/:id` — require an authenticated user (`req.user?.id` is checked). The implementation does not perform explicit owner or role checks in this file (it reads `created_by` on update but does not enforce ownership here).

Key endpoints

- GET /api/events
  - Query params (required/optional):
    - `from` (ISO date string, required)
    - `to` (ISO date string, required)
    - `classId` (optional) — filter events to a single class
    - `studentId` (optional) — include events for classes the student is enrolled in
    - `teacherId` (optional) — include events for classes the teacher teaches or events the teacher created
  - Returns: unified array of event objects with fields including `id`, `type`, `title`, `date`, `starts_at`, `ends_at`, `all_day`, `entity_type`, `entity_id`, `class_id`, `class_name`, `description`, `location`, and recurrence metadata when applicable.
  - Computed event types:
    - `assignment_due` — from `assignments.due_date`
    - `assignment_open` — from `assignments.available_from`
    - `quiz_due` / `exam` — from `quizzes.due_date` (quiz_type `exam` maps to `exam`)
    - `calendar_event` — custom events from `calendar_events` (may be recurring; expanded by `expandRecurring()`)
    - `academic_*` — institution-level academic calendar events expanded into per-day entries

- POST /api/events
  - Body: `{ event_type, title, description?, location?, frequency?, frequency_until?, starts_at, ends_at?, all_day?, class_id?, course_id? }`
  - Requires `title` and `starts_at` — returns `201` with the created row.

- PATCH /api/events/:id
  - Body may include any of the updatable fields: `title`, `description`, `location`, `frequency`, `frequency_until`, `starts_at`, `ends_at`, `all_day`, `event_type`, `class_id`.
  - Returns the updated event row.
  - If no fields provided, returns `400` with `No fields to update`.

- DELETE /api/events/:id
  - Soft-deletes the event by setting `deleted_at = now()` and returns `204` on success.

Recurrence & expansion behavior

- `expandRecurring(event, from, to)` supports frequencies: `daily`, `weekdays`, `weekly`, `monthly`, `yearly`, and `does_not_repeat`.
- The implementation normalizes dates using noon (`T12:00:00`) to avoid DST edge cases and limits expansions to 500 iterations to prevent runaway loops.
- Recurring event IDs in the returned feed are synthesized as `${event.id}-${YYYY-MM-DD}` so each occurrence has a unique id.
- Academic calendar multi-day events are expanded into one entry per date in the query window.

Filtering logic notes

- If `classId` is provided, the feed is scoped to that class's modules and custom events.
- If `studentId` is provided the server resolves active enrollments (`class_enrollments`) for that student and includes events for those classes.
- If `teacherId` is provided the server resolves classes the teacher teaches (`class_teachers` and `class_module_teachers`) and includes events for those classes; additionally it includes events the teacher created with no class.

Sample requests

GET events for a week (JSON):

```bash
curl "http://localhost:4000/api/events?from=2026-09-01&to=2026-09-07" \
  -H "Accept: application/json"
```

Create a custom recurring event (authenticated):

```bash
curl -X POST "http://localhost:4000/api/events" \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{"event_type":"custom","title":"Weekly Lab","starts_at":"2026-09-01T09:00:00","frequency":"weekly","class_id":123}'
```

Implementation notes & caveats

- The feed merges computed events (assignments/quizzes) with stored `calendar_events` and `academic_calendar_events`. Check the SQL in the source if you need exact column shapes or filtering nuances.
- The code constructs several `id` prefixes (`assignment-due-`, `assignment-open-`, `quiz-due-`, `custom-`, `academic-`) to indicate origin — frontends may rely on these ids for deduplication or grouping.
- The route performs direct SQL via `sequelize.query(...)` and depends on `module_items`/`class_modules` joins to link assignments/quizzes to classes.

Source (read-only): `ILS-dev/backend/routes/events.js`


**Last updated:** 2026-07-08

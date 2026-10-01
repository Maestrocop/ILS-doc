# Classes API (server: `backend/routes/classes.js`)

This document describes the classes-related HTTP endpoints implemented in `ILS-dev/backend/routes/classes.js`. It is a factual extraction of the current code and intended for developer reference.

Authentication & Roles

- Several endpoints require elevated roles:
  - `requireRole('admin')` — endpoints that create/update/delete classes, manage enrollments, and bulk module assignments.
  - `requireRole('teacher')` — the `GET /api/classes/my` endpoint returns teacher-assigned classes.

Key endpoints

- GET /api/classes
  - Purpose: list classes with module, course, campus and period info.
  - Response: array of class objects including `id`, `name`, `code`, `academic_year`, `semester`, `module_id`, `module_title`, `course_id`, `course_title`, `campus_name`, `period_name`, `student_count`.

- GET /api/classes/health
  - Purpose: readiness checks and compact module summary for classes.
  - Query: optional `mine=true` to restrict to classes the requesting teacher is attached to.

- GET /api/classes/my
  - Purpose: classes assigned to the logged-in teacher (requires teacher role).

- GET /api/classes/enrolled-elsewhere
  - Purpose: return `user_id`s already enrolled in other classes.
  - Query params: `exclude_class_id` (omit given class), optional `period_id` to scope to a period.

- GET /api/classes/:id
  - Purpose: single-class detail (module/course resolution and `blueprint_course_id` detection).

- GET /api/classes/:id/students
  - Purpose: list enrolled students for a class, with profile and last submission timestamp. Includes enrollment `status`, `enrollment_type`, and `enrolled_at`.

- POST /api/classes/:id/students
  - Purpose: enroll a student (admin only).
  - Body: `{ "user_id": <number> }` (required).
  - Behavior: reads the class's `enrollment_type` and enforces `is_exclusive` when applicable; inserts or re-activates a row in `class_enrollments` using `ON CONFLICT`.
  - Responses: `201` on success, `400` when `user_id` missing, `404` if class not found, `409` if exclusive enrollment conflict.

- POST /api/classes/:id/students/csv-import
  - Purpose: CSV-driven enrollment flow with optional dry-run preview (admin/coordinator).
  - Body shape:
    - `rows`: array of parsed row objects (`student_number`, optional `first_name`, `last_name`, `email`, `cohort`)
    - `dry_run`: boolean (default behavior is preview mode in current frontend flow)
  - Behavior in dry-run mode:
    - validates each row
    - resolves existing users by student number and/or email
    - classifies each row into action states (`create_and_enroll`, `enroll`, `already_enrolled`, `error`)
    - returns preview actions without DB writes
  - Behavior in import mode (`dry_run=false`):
    - creates missing users and `student_profiles` where needed
    - enrolls applicable users into `class_enrollments`
    - returns counters such as `created`, `enrolled`, `skipped`, `total`
  - Enrollment type handling:
    - current implementation reads the class `enrollment_type` and propagates it into `class_enrollments` inserts during CSV import.

- DELETE /api/classes/:id/students/:userId
  - Purpose: unenroll a student (admin only). Returns `204` on success.

- GET /api/classes/:id/modules
  - Purpose: modules assigned to the class and the teachers for each module.

- PUT /api/classes/:id/modules
  - Purpose: bulk replace module+teacher assignments (admin only).
  - Body: `{ modules: [ { module_id, teacher_ids: [...] }, ... ] }`.
  - Behavior: runs inside a DB transaction that clears existing `class_module_teachers` and `class_modules` for the class, then inserts the new rows.

- GET /api/classes/:id/projects
  - Purpose: list class-assigned projects (teacher metadata included).

- POST /api/classes
  - Purpose: create a class (admin only). Body accepts fields: `name, code, module_id, campus_id, period_id, academic_year, semester, enrollment_type`.
  - Returns: created class object (201).

- PUT /api/classes/:id
  - Purpose: update class fields (admin only). Returns updated class or `404` if not found.

- PATCH /api/classes/:id/enrollments/:userId/memo
  - Purpose: save a teacher memo for a student in a class (updates `teacher_memo` in `class_enrollments`).

- DELETE /api/classes/:id
  - Purpose: delete a class (admin only). The current implementation deletes the row from `classes` and returns `204`.

Notes & caveats

- The code performs SQL queries directly via `sequelize.query(...)` and frequently uses `ON CONFLICT` for upserts.
- CSV enrollment has replaced the older separate preview/bulk pattern in the current UI flow (`/students/csv-import` with `dry_run=true/false`).
- The `DELETE /api/classes/:id` handler performs a hard delete (`DELETE FROM classes`) despite an inline comment that says "soft delete" — be aware when relying on soft-delete semantics.
- Several endpoints auto-resolve or aggregate related entities (modules, course blueprint detection) — see the source for exact `SELECT` logic.

Reference

- Source: `ILS-dev/backend/routes/classes.js` (read-only)


**Last updated:** 2026-07-08

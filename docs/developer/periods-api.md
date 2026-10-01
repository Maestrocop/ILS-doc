# Periods API

This document describes the Academic Periods endpoints implemented in `ILS-dev/backend/routes/periods.js`. It is a read-only extraction of current server behaviour used for academic scheduling and period management.

Overview

- Purpose: manage academic periods (semesters, blocks, years, quarters, custom periods) that are used by academic calendar, timetable, and registration flows.
- Core model: `academic_periods` with fields such as `name`, `type`, `start_date`, `end_date`, `institution_id`, `campus_id`, `parent_id`, `is_active`, and soft-delete `deleted_at`.
- Allowed `type` values: `semester`, `block`, `year`, `quarter`, `custom`.

Endpoints

- GET /api/periods
  - Query params: `institution_id`, `campus_id`, `active` (set `active=true` to filter active periods).
  - Behaviour: returns all periods where `deleted_at IS NULL` and `course_id IS NULL` (periods scoped to courses are excluded). Joins to provide `parent_name`, `institution_name`, and `campus_name`.

- GET /api/periods/tree
  - Returns a nested tree of periods. The endpoint fetches matching rows and assembles parent/child relationships in-memory, returning root nodes with `children` arrays.

- GET /api/periods/:id
  - Returns the period row with `parent_name`, `institution_name`, and `campus_name`. Returns `404` if not found or deleted.

- POST /api/periods
  - Auth: `admin` role required (`requireRole('admin')`).
  - Body: `{ name, type='semester', start_date?, end_date?, institution_id?, campus_id?, parent_id?, is_active=true }`.
  - Validation: `name` required; `type` must be one of the allowed types.
  - Response: `201` with created row.

- PUT /api/periods/:id
  - Auth: `admin` role required.
  - Body: any of the period fields. The handler validates `type` if provided and uses `COALESCE` for `name` and `is_active` to preserve existing values when nulls are supplied.
  - Response: the updated period row or `404` if not found.

- DELETE /api/periods/:id
  - Auth: `admin` role required.
  - Behaviour: soft-delete sets `deleted_at = NOW()` and returns `204` on success.

Implementation notes & cautions

- The list and tree endpoints exclude rows where `course_id` is not NULL; these are course-scoped periods and intentionally filtered out for system-level period endpoints.
- Ordering: results are ordered by `start_date NULLS LAST, name` to surface open/ongoing periods first.
- Soft-delete pattern is used consistently across period APIs; clients should treat missing rows as deleted rather than absent.

Source (read-only): `ILS-dev/backend/routes/periods.js`


**Last updated:** 2026-07-08

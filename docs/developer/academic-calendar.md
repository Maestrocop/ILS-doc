# Academic Calendar API

This document describes the Academic Calendar endpoints implemented in `ILS-dev/backend/routes/academicCalendar.js`. It is a read-only extraction of the current server behaviour used by admin and scheduling flows.

Overview

- Purpose: create, update, list and soft-delete academic calendar events (holidays, breaks, exam periods, semester boundaries, registration windows).
- Core model: `academic_calendar_events` with fields including `event_type`, `title`, `description`, `starts_on`, `ends_on`, `institution_id`, `academic_year`, `period_id`, and soft-delete `deleted_at`.
- Valid `event_type` values: `holiday`, `exam_period`, `semester_start`, `semester_end`, `break`, `registration`.

Key behaviours

- The list endpoint expands multi-day events into one entry per calendar date within the requested range. Each expanded event has an id of the form `academic-<eventId>-<date>` and a type prefixed with `academic_` (e.g., `academic_holiday`).
- Date arithmetic uses a midday anchor (`T12:00:00`) to avoid DST edge cases, and the expansion loop includes a guard (max 400 iterations) to prevent runaway loops.
- Create/modify/delete endpoints require an authenticated user (`req.user.id`) and perform write operations against `academic_calendar_events`.
- Deletion is a soft delete implemented by setting `deleted_at = now()`.

Endpoints

- GET /api/academic-calendar?from=&to=&institutionId=
  - Parameters: `from` (required, ISO date), `to` (required, ISO date), `institutionId` (optional).
  - Behaviour: returns expanded daily events for all matching `academic_calendar_events` that intersect the `[from,to]` range. If `institutionId` is provided, the query includes events where `institution_id` matches or is NULL (global events).
  - Response: array of objects with keys: `id`, `type`, `title`, `date`, `starts_at`, `ends_at`, `all_day`, `entity_type`, `entity_id`, `description`, `institution_name`, `academic_year`, `period_id`, `period_name`.

- POST /api/academic-calendar
  - Auth: required.
  - Body: `{ event_type, title, description?, starts_on, ends_on?, institution_id?, academic_year?, period_id? }`.
  - Validation: `title` and `starts_on` required; `event_type` must be one of the valid types.
  - Response: `201` with the created `academic_calendar_events` row.

- PATCH /api/academic-calendar/:id
  - Auth: required.
  - Body: any of `{ title, description, starts_on, ends_on, event_type, academic_year, period_id }`.
  - Behaviour: updates provided fields and sets `updated_at = now()`; returns `404` if not found or already deleted.

- DELETE /api/academic-calendar/:id
  - Auth: required.
  - Behaviour: soft-deletes the event by setting `deleted_at = now()`; returns `204` on success.

Examples

Fetch academic events for a date range:

```bash
curl "http://localhost:4000/api/academic-calendar?from=2026-08-01&to=2026-09-30"
```

Create a holiday event:

```bash
curl -X POST "http://localhost:4000/api/academic-calendar" \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{"event_type":"holiday","title":"Founders Day","starts_on":"2026-09-15","ends_on":"2026-09-15"}'
```

Edit an event:

```bash
curl -X PATCH "http://localhost:4000/api/academic-calendar/42" \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{"title":"Founders Week","ends_on":"2026-09-18"}'
```

Delete (soft) an event:

```bash
curl -X DELETE "http://localhost:4000/api/academic-calendar/42" \
  -H "Authorization: Bearer <JWT>"
```

Implementation notes & cautions

- The list query filters `deleted_at IS NULL` and expands multi-day rows into daily entries; consumers should treat the returned objects as calendar-day entries rather than raw DB rows.
- The server-side expansion uses a `while` loop bounded by 400 iterations to prevent accidental infinite loops for malformed data.
- Global academic events have `institution_id = NULL` and are included when an `institutionId` filter is provided.

Source (read-only): `ILS-dev/backend/routes/academicCalendar.js`


**Last updated:** 2026-07-08

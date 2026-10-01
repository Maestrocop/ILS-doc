# Timetable API (sessions, slots, generation)

This document describes the timetable and session-generation endpoints implemented in `ILS-dev/backend/routes/timetable.js`. It is a read-only extraction of current server behaviour used by the admin/teacher calendar flows.

Overview

- Purpose: manage class timetables (timetable rows, slots) and generate concrete `timetable_sessions` from slots across a date range. The generator is holiday-aware and idempotent.
- Key concepts: `class_timetable` (timetable meta), `timetable_slots` (repeating slot definitions by day-of-week), and `timetable_sessions` (concrete scheduled dates).

Core behaviours

- Session generation (`generateSessions`) is idempotent: it skips already-generated dates and only inserts new session rows.
- Holidays/breaks are read from `academic_calendar_events` and produce `cancelled` statuses; exam periods produce `flagged` sessions.
- When a slot is edited (`PATCH /api/timetable/slots/:slotId`), the implementation marks existing `timetable_sessions` for that slot as deleted (soft-delete) so a subsequent `POST /api/timetable/:id/generate` will rebuild sessions with the new slot times.
- Editing a session (`PATCH /api/timetable/sessions/:sessionId`) marks it as an exception (`is_exception = true`).

Session statuses

- `scheduled` — normal session
- `cancelled` — session blocked by holiday/break
- `flagged` — session occurs during an exam period (monitoring/attention)

Endpoints

- GET /api/timetable?classId=
  - List timetables; optional `classId` filters to a class. Returns meta including `session_count`.

- GET /api/timetable/:id
  - Returns the timetable row plus `slots` and current `sessions` (non-deleted).

- POST /api/timetable
  - Create a timetable. Body required: `{ class_id, valid_from, valid_until }`. Optional `slots` array may be provided to insert initial slots.

- PATCH /api/timetable/:id
  - Update timetable metadata: `valid_from`, `valid_until`, `period_id`, `notes`, `status`.

- DELETE /api/timetable/:id
  - Soft-delete the timetable (sets `deleted_at`).

Slots

- POST /api/timetable/:id/slots
  - Create a slot for a timetable. Body: `{ day_of_week, start_time, end_time, valid_from?, valid_until? }`.

- PATCH /api/timetable/slots/:slotId
  - Update a slot. Body accepts the same fields as POST. The handler also soft-deletes existing `timetable_sessions` for the slot so regenerate will rebuild sessions with new times.

- DELETE /api/timetable/:id/slots/:slotId
  - Soft-delete a slot (sets `deleted_at`).

Session generation

- POST /api/timetable/:id/generate
  - Runs the idempotent generator which:
    1. Reads timetable `valid_from` / `valid_until` and slots for the timetable.
    2. Reads `academic_calendar_events` to build a set of blocked dates (holidays/breaks) and flagged dates (exam periods).
    3. Computes all calendar dates matching each slot's day-of-week within the slot's validity window.
    4. Skips existing `timetable_sessions` to avoid duplicates.
    5. Inserts new `timetable_sessions` with `status` set to `scheduled`, `cancelled`, or `flagged` and returns `{ generated: <count> }`.
  - The endpoint also marks the timetable `status = 'active'` on success.

Session edits

- PATCH /api/timetable/sessions/:sessionId
  - Edit a single session (reschedule, cancel, add notes). The handler sets `is_exception = true` for edits and returns the updated session.

Examples

Generate sessions for timetable `42`:

```bash
curl -X POST "http://localhost:4000/api/timetable/42/generate" \
  -H "Authorization: Bearer <ADMIN_JWT>"
```

Edit a slot (this wipes generated sessions for the slot so regenerate rebuilds them):

```bash
curl -X PATCH "http://localhost:4000/api/timetable/slots/17" \
  -H "Authorization: Bearer <ADMIN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"day_of_week":0,"start_time":"08:30","end_time":"10:00"}'
```

Mark a session as cancelled with a note:

```bash
curl -X PATCH "http://localhost:4000/api/timetable/sessions/999" \
  -H "Authorization: Bearer <ADMIN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"status":"cancelled","cancellation_reason":"teacher_absent","notes":"Substitute arranged"}'
```

Implementation notes & cautions

- The generator uses a 500-iteration guard per slot to avoid infinite loops when computing dates.
- Date handling uses local-date arithmetic with noon (`T12:00:00`) to reduce DST edge-case issues.
- Holiday/block detection relies on `academic_calendar_events` — exam periods are treated as `flagged` rather than cancelled.
- Slot `PATCH` currently soft-deletes session rows for that slot to ensure a clean regenerate; this is a deliberate design choice and is documented in the Slot Edit Proposal page.

Source (read-only): `ILS-dev/backend/routes/timetable.js`


**Last updated:** 2026-07-08

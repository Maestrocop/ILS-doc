# Slot Edit Proposal (Timetable)

Goal: Make timetable slots editable so admins can correct day/time errors without manual delete+recreate work.

Why

- Current behavior: regenerating sessions only appends new rows; editing a slot requires deleting existing sessions then re‑generating. The UI currently only supports delete + add which is clunky.

Proposal — Server API

- PATCH `/api/timetable/slots/:slotId`
  - Body: `{ "day_of_week": "Mon", "start_time": "08:30", "end_time": "10:00" }` (schema fields to match existing DB)
  - Auth: admin or timetable-manager role
  - Behavior:
    1. Validate new times (no overlap within same class/campus/period)
    2. Begin DB transaction
    3. Delete existing generated sessions tied to the slot (or mark them archived), e.g. `DELETE FROM timetable_sessions WHERE slot_id = :slotId` (adjust to actual schema)
    4. Update the slot row with new times
    5. Re-run session generation for the slot (use the same generator used for initial creation)
    6. Commit transaction and return updated slot + regenerated sessions

Implementation notes

- Use a DB transaction to avoid partial state if generation fails.
- If other entities reference generated sessions (attendance records, grades), consider soft-delete or a migration that preserves those links and copies them to the new session rows.
- If the system does not store `slot_id` on generated sessions today, add a small migration to record the origin slot to make this safe.

Frontend UI

- Inline edit on each slot chip (no modal): click → expand fields `day`, `start`, `end` → Save / Cancel
- On Save: show confirmation: "This will delete and re-generate sessions for this slot. Proceed?" with a list of affected weeks/date ranges
- If editing is frequent, add an undo/preview step showing affected sessions before committing

Acceptance tests

- PATCH updates slot and replaced sessions in a single transaction
- Editing a slot with overlapping times is rejected (400)
- Editing preserves historical attendance/grades according to chosen strategy (archive vs recreate)

Developer deliverables

- Backend: new route handler `PATCH /api/timetable/slots/:slotId`, unit tests, integration test that regenerates sessions
- Frontend: inline slot editor component, confirmation UX, integration test that visualizes regenerated sessions

Notes

- Exact table/column names for sessions and slots were not verified in ILS‑dev as part of this doc; implementers should refer to the schema before writing SQL. If you want, I can draft the exact SQL and a patch (in a separate branch) — I will not modify ILS‑dev unless you explicitly request it.


**Last updated:** 2026-07-08

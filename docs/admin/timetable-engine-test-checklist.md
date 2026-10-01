# Timetable Engine — Test Checklist (Ticket #163)

This checklist documents the manual test steps for the Timetable Engine and session workflow. Use it when verifying new timetable changes.

## 1. Create a timetable

- Click **+ New Timetable**
- Select a class
- Select an Academic Period → dates should auto-fill from the period
- Adjust dates if needed (Valid From / Valid Until)
- Add a weekly slot: pick a day (e.g. Mon), set `09:00 → 11:00`
- Click **+ Add slot** to add a second slot on a different day
- Click **Create Timetable** → should appear in the left list with `draft` status

## 2. Generate sessions

- With the timetable selected, click **⚡ Generate Sessions**
- Alert should say "Generated N sessions" — verify N is a sensible number for the date range
- Sessions list populates, all showing `scheduled` badge (sky blue)

## 3. Mark as Held (new in this commit)

- Hover over any `scheduled` session → a **Held** button appears on the right
- Click it → status badge immediately changes to `held` (green) — no modal, 1 click

## 4. Edit a session manually

- Hover over a session → click **Edit**
- Change status to `cancelled` → a **Reason** field should appear below
- Type a reason (e.g. "teacher absent")
- Save → session shows `cancelled` with strikethrough style and the reason text

## 5. Add a makeup session (new in this commit)

- Click **+ Makeup** (amber button, top-right of sessions panel)
- Amber form expands: fill in a date, `09:00`, `11:00`, optional notes
- Click **Add Makeup** → new session appears in list with amber `makeup` badge
- Filter dropdown → select "Makeup" → only that session shows

## 6. Edit an existing slot

- In the **Weekly Pattern** section, click the **✎** pencil icon on a slot chip
- Change the time inline (e.g. `10:00 → 12:00`)
- Click ✓ → hint appears: *"Slot edited — click ↻ Re-sync Sessions to apply changes"*
- Click **↻ Re-sync Sessions** → session times update

## 7. Add a slot post-creation

- Click **+ Add slot** in the Weekly Pattern header
- Pick a new day/time → click Add → new chip appears

## 8. Duplicate a timetable

- With timetable selected, click **Duplicate**
- Modal opens — slots and dates are pre-filled, class is empty
- Select a **different** class → click Create Timetable → second timetable appears in list


---

Notes:
- This checklist is intended for the QA team and release engineers validating the timetable changes. It assumes default campus reporting rules and active academic periods are present.
- For automation, these steps can be converted into Playwright flows using the Timetable UI selectors.


**Last updated:** 2026-07-08

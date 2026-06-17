# Timetable Engine — End-to-End Walkthrough

Follow these steps in order — each role picks up where the previous left off. This is a read-only user guide entry; no code in `ILS-dev` is modified.

## Prerequisites
- At least one Class exists (e.g. BK Jaar 1 — 2025/2026)
- At least one Academic Period is set (e.g. Semester 1)
- Academic Calendar has at least one holiday event (to test skip logic)
- The class has at least one enrolled student and one assigned teacher

---

## Phase 1 — Admin/Coordinator: Create & Activate Timetable

1. Open the Timetable page: `/admin/timetable`, select the class — you should see "No timetable configured yet".
2. Create a timetable: click **New Timetable**, select class and academic period, save → timetable appears with status `draft`.
3. Add recurring slots: click **Add Slot**; e.g. Monday 09:00–11:00, Wednesday 14:00–16:00; save — slots listed.
4. Activate: click **Activate** → system generates session rows up to period end; holiday dates are marked `cancelled` and show holiday name.
5. Inspect sessions: confirm scheduled vs cancelled/makeup statuses and expected session count.

---

## Phase 2 — Teacher: Mark Attendance

6. Open teacher schedule: log in as assigned teacher → `/admin/my-schedule`, week view with session blocks.
7. Mark a session as held: click a session block → **Mark as Held**; status becomes `held`.
8. Register attendance: open session → **Attendance**, mark Present/Absent, save → confirmation badge.
9. Cancel a session: choose a future session → **Cancel**, enter reason → status `cancelled`.
10. Add a makeup session: on a cancelled session → **Schedule Makeup**, pick date/time → new session with status `makeup`.

---

## Phase 3 — Session Edit (occurrence / following)

11. Edit a single session: choose **This occurrence only** when changing time/room — only that session updates.
12. Edit this and following: choose **This and all following** to update sessions from this point onward.

---

## Phase 4 — Student View

13. Student calendar: log in as an enrolled student → calendar shows sessions with color coding and status badges.
14. Attendance badge on dashboard: student dashboard shows donut reflecting sessions held vs attended.

---

## Phase 5 — Curriculum Hook (optional)

15. Link a session to module content: open a session (teacher/admin) → Lessons/Curriculum tab → add planned module item; after session mark as covered.

---

## What to note during testing
- Flag any step that errors or shows blank.
- Flag confusing UI text.
- Flag missing functionality.

Those gaps become the remaining Timetable Engine work.

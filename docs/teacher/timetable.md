# Timetable

The Timetable page shows scheduled classes, sessions, and allows teachers to view and manage sessions.

## Features

- View class schedules by period and week
- Record held sessions and schedule makeup sessions

## Recent changes (June 2026)

- Timetable lifecycle improvements: makeup sessions and held actions are now fully supported in the timetable UI. Teachers can record held sessions and create makeup entries where required.

## Troubleshooting

### "No module linked to this session" message

**What it means:** The system cannot find a module assigned to this time slot. This typically happens for:
- Makeup sessions that were created before a module assignment
- Sessions generated before schedule rules were configured

**What to do:**

1. **Close the session modal** (click outside or press Escape)
2. **Go to Schedule Rules** (from the Timetable menu)
3. **Assign a module** to the appropriate time slot or class schedule
4. **Click "Re-sync Sessions"** to regenerate sessions from the updated rules
5. **Reopen the session** — it should now show the module

If sessions still do not appear or show no module, contact your system administrator.

## Teacher Step-by-step Guide

### Open your timetable (today)

1. From the main Teacher menu click **Timetable** or open `/teacher/timetable`
2. The default view shows the current week and your assigned classes
3. Use the **Today** or week picker to jump to the date you need

### Filter by class, period or week

1. Use the left-hand class list to pick a class you teach
2. Use the period tabs (top-right) to switch academic periods
3. Use the day/weekday quick filters to view only Monday/Tuesday etc.

### View session details

1. Click a session block in the calendar or the sessions list
2. A session modal opens showing:
	- Module name
	- Teacher (owner)
	- Room
	- Attendance status (if recorded)
	- Linked assignments or activities

### Mark a session as held (record the lesson)

1. Open the session modal for the session you ran
2. Click **Record Held** or **Mark as Held**
3. Optionally add notes about what you covered
4. Save — this marks the session as held and enables delivery-planner options (due dates default to session date + 4 days)

### Cancel a session

Use this when a session won't happen at all — e.g. students are pulled into a different school activity that day. Don't delete the session; cancelling keeps it visible in the timetable history instead of erasing the record that it was ever scheduled, and it can interfere with the recurring-series logic that generates sessions from the schedule rule.

1. Open the session modal for the session that's not happening
2. Click **Edit**
3. Set **Status** to **Cancelled**
4. Enter a short **cancellation reason** (e.g. "Students at other activity")
5. Save

Once cancelled, the session no longer expects attendance to be registered, and it shows up under the **Cancelled** filter in the sessions list instead of **Scheduled**.

### Create a makeup session

Use a makeup session when you need to schedule an extra lesson for the class.

1. Open the session modal for the original session or go to **+ New Session**
2. Select **Makeup session** (or toggle `Is makeup`)
3. Pick the new date/time and room
4. Assign a module and teacher if needed
5. Save — the makeup session appears in the calendar for that date

### Edit a session (change teacher, module, or time)

1. Open the session modal
2. Click **Edit**
3. Change the fields (teacher, module, room, start/end time)
4. Save

Notes on editing:
- If a session already has attendance recorded, edits that would change historical ownership are blocked — you can create an exception instead.

### Re-sync sessions after schedule rule changes

When Schedule Rules are updated (admin area), you may need to re-sync:

1. Close any open session modals
2. Go to **Schedule Rules** (from the Timetable menu)
3. Apply changes (assign module/teacher to the rule)
4. Click **Re-sync Sessions** to regenerate sessions from rules
5. Reopen sessions to confirm module and teacher were applied

### Quick actions

- **Jump to today**: click Today
- **Filter by teacher**: use the teacher filter if you cover multiple classes
- **Publish/Unpublish**: teachers see only published timetables — contact admin if your timetable shows unexpected sessions

### Common issues

- "Session shows no module": follow the Troubleshooting steps above
- "Session doesn't appear on my calendar": ensure the timetable is Published and you are assigned as teacher for that class/period
- "Makeup session missing": check the target date and the class filter; confirm the makeup session was saved (not cancelled)

---

**Last updated:** 2026-10-01

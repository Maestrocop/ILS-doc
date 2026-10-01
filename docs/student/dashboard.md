# Student Dashboard (My Dashboard)

Your dashboard is your personal learning home page. It shows your progress at a glance, recent grades, attendance, and module progress.

## What the dashboard shows

- **Average Score** — your overall grade across all graded work (0–10 scale)
- **Quick stats** — how many assignments you've submitted, what's pending, and what's graded
- **Next Actions** — assignments due soon or overdue, ordered by urgency, linking straight to each one
- **Attendance** — a present/absent/late/excused breakdown, with a warning if attendance drops below 80%
- **Modules** — how many of your enrolled modules are Completed / In Progress / Not Started, plus a module-completion progress bar (see "Modules progress" below)
- **Recent Grades** — your most recent graded submissions with scores and feedback links
- **Outcome Performance** — how you're doing on each learning outcome (Strong / Developing / At-Risk), the day-to-day/weekly view of competency mastery

## Modules progress

Each module is bucketed by your submission activity in it, not by whether you've opened it:

- **Not started** — you have zero graded and zero submitted assignments in that module. Opening the module or starting a draft doesn't move it out of this bucket — only submitting something does.
- **In progress** — at least one assignment has been submitted (graded or awaiting grading), but not every assignment in the module is graded yet.
- **Completed** — every assignment in the module is graded.

Progress is shown as plain module completion (e.g. "10/13 modules passed, 77%"), not a credit estimate.

### Resolved 2026-09-19: the "EC" credit estimate didn't fit MBO

This used to show `~X / 45 EC estimated`. **EC (European Credits / ECTS)** is HBO/WO (higher education) terminology from the Bologna credit system — MBO doesn't use EC at all; it's organized around Kwalificatiedossiers, Kerntaken/werkprocessen, and study load in hours (SBU), not credit points. The widget (and the `BSA_NORM_EC` constant behind it) was built for an HBO context — "BSA" is Bindend Studieadvies, itself an HBO/WO mechanism — and was never adapted when the same dashboard got reused for TCR's MBO students. See #386.

Fix shipped ("Option 3a" of the discussion): dropped the EC framing, show plain module-completion % instead — no new data needed. While fixing this, also found and fixed a real undercounting bug: the Outcome Performance section's Strong/Developing/At-Risk counts were silently capped by a backend `LIMIT 10` meant for a different purpose ("weakest 10 to review"), so a student with more than 10 outcomes with evidence never got their genuinely mastered ones counted.

### Planned next: Kerntaken-level rollup ("Option 3b")

The Outcome Performance section already gives day-to-day/weekly monitoring at the individual skill/werkproces level (using real graded evidence via `student_outcome_snapshots`, not a manual estimate). The next step is rolling that up to the Kerntaak level for periode-end review (teacher/SLB/student together) — e.g. "2 of 3 Kerntaken mastered" instead of a flat list of skills.

Prerequisite already in progress: linking outcomes to assignment rubrics (65 rubric criteria linked locally as of 2026-09-19, 2,941 snapshots generated). To finish the setup:
1. Create one `outcomes` row per Kerntaak (e.g. B1-K1, B1-K2, B1-K3).
2. Set `parent_id` on the existing skill/werkproces-level outcomes to point up to the right Kerntaak (the column already exists on `outcomes` — no migration needed, just data entry).
3. A Kerntaak then reads as mastered once its child outcomes collectively clear the mastery threshold.

## How to read your dashboard

1. **Check your Average Score** — quick view of your overall performance
2. **Review Recent Grades** — click any grade to see the full feedback and assignment details
3. **Look at Outcome Performance** — find the outcomes where you're strongest and weakest
4. **Plan your next steps** — use low-performing outcomes to focus your revision work

## Using outcome performance

When you see an outcome with low performance:
- Click it to see which assignments contributed to that score
- Review the feedback comments for that outcome
- Work with your teacher or advisor to plan improvement

## Quick workflow

1. Open "My Dashboard" when you log in
2. Scan your stats for anything that needs attention
3. If you see pending work, check the assignment page for details
4. If a grade was returned, review the feedback immediately
5. Use outcome trends to guide your revision priorities


**Last updated:** 2026-09-19

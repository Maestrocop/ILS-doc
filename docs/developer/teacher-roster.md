# Teacher Roster

This page documents the teacher roster implementation in ILS. The roster is a teacher-facing workspace for viewing assigned classes and the students enrolled in each class.

## What My Roster is

- The Teacher Roster page is accessible at `/admin/my-roster`.
- It is intended for teachers and administrators.
- The page shows classes assigned to the current teacher and lists enrolled students with activity and enrollment status.

## Admin UI

- Frontend route: `/admin/my-roster`
- Files:
  - `ILS-dev/frontend/src/pages/TeacherRosterPage.jsx`
  - `ILS-dev/frontend/src/App.jsx`
  - `ILS-dev/frontend/src/components/AdminSidebar.jsx`

### Page behavior

`TeacherRosterPage.jsx` performs these actions:
- loads the teacher's own classes from `GET /api/classes/my`
- shows a class selector for the teacher's assigned classes
- loads students for the selected class from `GET /api/classes/:id/students`
- filters students by name or student number
- sorts students so the least active or most stale students appear first
- provides a quick navigation link to the Student Cockpit for each student

### Student roster details

Each row in the roster table shows:
- student name
- student number
- cohort
- enrollment status
- last activity label, with color-coded urgency
- a `View` button that navigates to `/admin/student-cockpit?student_id=...&class_id=...&from=roster`

The last activity label is computed by the frontend from `last_submission_at`:
- `Today` / `<= 3d ago` — green
- `<= 14d ago` — gray/orange
- `> 14d ago` — red
- missing activity is shown as `No activity`

## Permissions

- The page is gated by role membership: only users with `teacher` or `admin` roles may access it.
- If a user lacks these roles, the page displays an access message.

## Backend API

The Teacher Roster page relies on class and student endpoints in the backend:
- `GET /api/classes/my` — teacher's assigned classes
- `GET /api/classes/:id/students` — students enrolled in a specific class

These routes are implemented in `ILS-dev/backend/routes/classes.js`.

## Implementation notes

- The page defaults to selecting the only class when the teacher has exactly one assigned class.
- Student sorting emphasizes stale activity first, supporting teacher triage.
- The roster page is integrated into the admin sidebar as `My Roster`.


**Last updated:** 2026-07-08

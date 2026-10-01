# Users

This page documents the current user management implementation in ILS. The users workflow covers account listing, profile editing, role management, campus assignment, and archived status.

## What Users represent

- Users are the system accounts for students, teachers, admins, and other staff roles.
- Each user has a `roles` array, an active/archived flag, and optional campus assignment.
- The backend joins `users` with `student_profiles`, `staff_profiles`, and `campuses` to provide rich profile details.

## Admin UI

- Frontend route: `/admin/users`
- Files:
  - `ILS-dev/frontend/src/pages/UsersPage.jsx`

### Users page behavior

`UsersPage.jsx` loads the data needed for user administration:
- `GET /api/users` — master user list with role, email, campus, student number, cohort, department, and active flag
- `GET /api/campuses` — campus list for filtering and user attribute assignment
- `GET /api/institutions` — institutions for the campus selector

The page supports:
- searching users by name or student number
- filtering by role, campus, cohort, and active/archived status
- pagination of results in 50-item pages
- opening a modal to edit an existing user
- creating a new user via a modal (admin only)

### Edit user workflow

The edit modal allows admins to update:
- first name
- last name
- email
- campus assignment
- roles

Role editing is handled through a dedicated role selector that supports preset roles and custom role names.

### Create user workflow

The create modal requires:
- first name
- last name
- email
- password (minimum 8 characters)

It also allows selecting a campus and choosing roles. The default role set is `student` unless additional roles are provided.

## Backend API

The user management backend is implemented in `ILS-dev/backend/routes/users.js`.

### Primary endpoints

- `GET /api/users` — list all users with profile, campus, student number, cohort, and department
- `GET /api/users/:id` — fetch a single user's full profile
- `POST /api/users` — create a new user (admin only)
- `PUT /api/users/:id` — update user profile fields (admin only)

### User administration endpoints

- `PUT /api/users/:id/status` — archive or unarchive a user by toggling `is_active` (admin only)
- `PUT /api/users/:id/roles` — replace a user's roles array (admin only)
- `PUT /api/users/:id/password` — set or reset a user's password (admin only)

### Payload details

`POST /api/users` accepts:
- `email` (required)
- `first_name` (required)
- `last_name` (required)
- `password` (required, min 8 chars)
- `roles` (array of strings)
- `campus_id`
- `cohort` (optional student cohort)

`PUT /api/users/:id` accepts:
- `first_name`
- `last_name`
- `email`
- `campus_id`
- `cohort` (student cohort updates student profile)

`PUT /api/users/:id/status` accepts:
- `is_active` (boolean)

`PUT /api/users/:id/roles` accepts:
- `roles` (array of strings)

`PUT /api/users/:id/password` accepts:
- `password` (required, min 8 chars)

## Role and status rules

- The frontend exposes a default role palette: `admin`, `coordinator`, `designer`, `teacher`, and `student`.
- `superuser` is intentionally excluded from the UI and is intended to be set only in the database.
- Custom roles may still be added from the UI and are stored as strings in the `roles` array.
- Archiving is represented by `is_active = false`; active users are shown by default.
- The list page includes a toggle to show archived users.

### Recommended role architecture

The ILS role model is best understood as a set of distinct responsibilities, with users able to hold multiple roles simultaneously.

| Role | Primary responsibility | Enrollment rights |
|---|---|---|
| `superuser` | Institution owner / IT infrastructure; bypasses all role checks. Set in DB only and never through the UI. | Full system-wide access |
| `admin` | Campus or school administrator; manages users, classes, enrollment, and settings within the assigned domain. | Full enrollment and admin access in their domain |
| `coordinator` | Program manager for assigned courses; coordinates enrollment and course delivery. | Classes within assigned course(s) only |
| `designer` | Curriculum designer; creates modules, assignments, rubrics, outcomes, and mapping without student roster or grading permissions. | No enrollment rights |
| `teacher` | Classroom delivery and grading; uses teacher cockpit, heatmap, and roster tools. | No enrollment rights |
| `student` | Learning consumer; accesses curriculum, assignments, quizzes, and progress views. | Self-enroll in keuzedelen only (future) |

The existing `roles` array already supports this extension. Current system behavior keeps `superuser` as a DB-only top-level bypass role, while `admin` remains the primary UI-facing administrative role. Future work may scope `coordinator` and `designer` access more narrowly according to assigned courses and curriculum domains.

## Implementation notes

- The Users page keeps its own filter state and recalculates visible users locally after the initial load.
- Both edit and create flows use campuses and institutions for location metadata.
- Role updates are committed through a separate API call to `/api/users/:id/roles`.
- The backend normalizes duplicate emails and returns a `409` conflict if the email already exists.


**Last updated:** 2026-07-08

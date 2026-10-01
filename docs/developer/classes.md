# Classes

This page documents the current Classes implementation in ILS. Classes represent active teaching sessions and connect modules, teachers, students, campuses, and academic periods.

## What a Class is

- A Class is a scheduled session or cohort that links a module to a specific period and campus.
- Classes are not the same as modules: a module is the curriculum unit, while a class is the actual delivery section for students.
- The frontend exposes class management under the admin UI, and the backend exposes a `/api/classes` route group.

## Admin UI

- Frontend list page: `/admin/classes`
- Detail page: `/admin/classes/:id`
- New class page: `/admin/classes/new`

### Frontend files

- `ILS-dev/frontend/src/pages/ClassesPage.jsx`
- `ILS-dev/frontend/src/pages/ClassDetailPage.jsx`

### List page behavior

`ClassesPage.jsx` loads:
- `GET /api/classes` — all classes with module, course, campus, period, and student count
- `GET /api/periods` — period metadata used for filtering

The class list page supports:
- searching by class name, code, module title, or course title
- filtering by academic period
- navigating to class detail
- deleting a class (admin only)

The list row includes:
- class name or code
- course title
- period label with a color-coded badge
- campus name
- enrolled student count
- admin actions menu for manage/delete

### Detail page behavior

`ClassDetailPage.jsx` is used for both viewing/editing existing classes and creating new classes.

For existing classes it loads:
- `GET /api/classes/:id`
- `GET /api/classes/:id/modules`
- `GET /api/classes/:id/students`
- `GET /api/classes/:id/projects`
- `GET /api/modules`
- `GET /api/users`
- `GET /api/periods`
- `GET /api/campuses`

For new class creation it loads reference data only:
- modules
- users
- periods
- campuses

The page manages:
- class metadata: name, code, period, campus
- module assignments for the class
- teacher assignments per module
- student enrollment

## Key class workflows

### Save details

- Creating a class sends `POST /api/classes`
- Updating a class sends `PUT /api/classes/:id`
- The detail page persists classroom metadata, module assignments, and student enrollment in one flow

### Assigning modules and teachers

- The detail page loads all modules and teacher users.
- Assigned modules are persisted with `PUT /api/classes/:id/modules`.
- Each module entry can have one or more assigned teachers.

### Enrolling students

- Students are staged locally in the UI before save.
- New enrollments are posted to `POST /api/classes/:id/students`.
- Unenrollments are sent to `DELETE /api/classes/:id/students/:userId`.

## Backend API

The class routes are implemented in `ILS-dev/backend/routes/classes.js`.

### Primary endpoints

- `GET /api/classes` — list classes with module/course/campus/period summary and student count
- `GET /api/classes/:id` — class detail
- `POST /api/classes` — create class (admin only)
- `PUT /api/classes/:id` — update class (admin only)
- `DELETE /api/classes/:id` — delete class (admin only)

### Class enrollment endpoints

- `GET /api/classes/:id/students` — enrolled students list
- `POST /api/classes/:id/students` — enroll a student (admin only)
- `DELETE /api/classes/:id/students/:userId` — remove a student from a class (admin only)
- `GET /api/classes/:id/projects` — projects assigned to the class

### Module assignment endpoints

- `GET /api/classes/:id/modules` — assigned modules with teacher rosters
- `PUT /api/classes/:id/modules` — bulk replace module assignments and class-module teachers (admin only)

### Role requirements

- Admin privileges are required for create, update, delete, enrollment, and module assignment changes.
- The frontend exposes the class detail workflow to admins.
- Teachers and coordinators may access class-related views through dedicated pages such as `/admin/classes` and `/admin/classes/:id` when permitted by UI flow.

## Model relationships

Classes are connected to model entities as follows:

- `Class` belongs to `Module` via `class_modules` / `class_module_teachers`
- `Class` belongs to `Campus`
- `Class` belongs to `AcademicPeriod`
- Students are connected through `class_enrollments`
- Teachers are connected through `class_module_teachers`

### Enrollment types and hybrid class support

The ILS class model supports multiple simultaneous enrollments per student.

- `class_enrollments` may include an `enrollment_type` flag such as `primary`, `keuzedeel`, or `minor`.
- `primary` represents the student’s home cohort or main class. A student may have at most one primary enrollment, but a primary enrollment is not required.
- `keuzedeel` and `minor` represent elective or optional classes. Students may join multiple of these at the same time.
- The backend enforces a partial unique index on `class_enrollments` so only one `primary` is allowed per student. This constraint does not require any `primary` enrollment.
- For US-style schools, all class enrollments can be `keuzedeel` and the constraint stays invisible.
- This supports hybrid education models: one main cohort plus several elective or subject-specific classes.
- The student dashboard can show all enrolled classes, while class-level teacher views may filter to the current class scope.
- Outcome and snapshot tracking aggregates across all of a student’s active class enrollments, regardless of type.

## Implementation notes

- The class list page uses server-side reporting for student count and period metadata.
- The detail page keeps a local dirty state so saves are only enabled when class details, module assignments, or enrollments change.
- `ClassDetailPage.jsx` separates data loading for new classes versus existing classes to avoid unnecessary backend requests.


**Last updated:** 2026-07-08

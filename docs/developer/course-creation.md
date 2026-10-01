# Course Creation

This page documents the real course creation flow in ILS, based on the current `ILS-dev` source. It describes the frontend steps, the API call, and the backend handler that persists the new course.

## Entry point

- Frontend route: `/admin/courses`
- File: `ILS-dev/frontend/src/pages/CoursesPage.jsx`
- Navigation in `ILS-dev/frontend/src/App.jsx` defines the route:
  - `admin/courses` → `CoursesPage`
  - `admin/courses/new` → `CourseForm`

## Step-by-step flow

1. The user opens the admin course bank page.
   - `CoursesPage.jsx` loads the existing course list from `GET /api/courses`.
   - The page renders a `+ New Course` button linking to `/admin/courses/new`.

2. The user clicks `+ New Course`.
   - React Router navigates to `/admin/courses/new`.
   - `App.jsx` maps that route to `ILS-dev/frontend/src/pages/CourseForm.jsx`.

3. `CourseForm.jsx` renders the course editor form.
   - Fields shown include:
     - Full Name
     - Short Code / Identifier
     - Level
     - Duration
     - Description
     - Course Color
     - Status (`draft`, `published`, `archived`)
     - Enrollment Type (`Open Enrollment`, `Invite Only`)
     - Total Credits (ECTS)
     - Partner Institutions (checkboxes, loaded from `/api/institutions`)
   - File: `ILS-dev/frontend/src/pages/CourseForm.jsx`

4. The user fills in the course details and submits the form.
   - The form submit handler is `save()` in `CourseForm.jsx`.
   - It builds a payload object with the entered values.
   - It calls `fetchApi('/courses', { method: 'POST', ... })` for a new course.
   - File: `ILS-dev/frontend/src/lib/api.js` defines `fetchApi()` and prefixes requests with `/api`.

5. The frontend sends a POST request to the backend.
   - Actual request path: `POST /api/courses`
   - Payload keys include:
     - `title`
     - `description`
     - `code`
     - `short_code`
     - `duration`
     - `level`
     - `total_credits`
     - `status`
     - `enrollment_type`
     - `primary_color`
     - `institutionIds`
     - `default_teaching_method_id`
     - `default_assessment_type_id`
   - File: `ILS-dev/frontend/src/pages/CourseForm.jsx`

6. The backend receives `POST /api/courses`.
   - Route file: `ILS-dev/backend/routes/course.js`
   - The route handler checks for `req.models.Course`.
   - It requires `payload.title`; if missing, it returns `400` with `title is required`.
   - It calls `models.Course.create(payload)` to persist the new course.
   - On success, it returns `201` with the created course object.
   - On database errors, it returns a structured error response.

7. The frontend handles the backend response.
   - `CourseForm.jsx` reads the JSON response and updates the form state.
   - For a new course, it navigates to the newly created course detail view (`/admin/courses/:id`).
   - For an existing course, it sets a saved confirmation state and keeps the user on the form.
   - If the response fails, the page displays a save error message.

## Trigger chain

- UI event: click `+ New Course` → navigate to `/admin/courses/new`
- UI event: submit form → `CourseForm.jsx` `save()`
- API call: `POST /api/courses`
- Backend action: `models.Course.create(payload)` in `backend/routes/course.js`
- DB persistence: Sequelize creates a new `Course` row
- UI reaction: success alert, redirect to `/admin/courses`

## Important implementation notes

- The frontend always uses `fetchApi()` from `ILS-dev/frontend/src/lib/api.js`, which prefixes paths with `/api`.
- The backend route is mounted under `/api/courses` in `ILS-dev/backend/index.js`.
- `CourseForm.jsx` also loads institutions from `GET /api/institutions` to support the partner institution checkbox list.
- There is no explicit course creation helper outside the admin flow; the route is driven entirely by `CoursesPage.jsx` and `CourseForm.jsx`.

## Missing or unclear items

- The backend `course.js` route file implements `GET /`, `POST /`, `GET /:id`, `PUT /:id`, and `DELETE /:id`, so course editing and soft delete are supported by the current API.
- The form loads partner institutions from `GET /api/institutions`, but the exact institution-course linking semantics are handled by the backend and may depend on the current institution records.


**Last updated:** 2026-07-08

# Grading Cockpit

This page documents the current developer implementation of the grading cockpit in `ILS-dev`.
It is the main teacher scoring workflow and the entry point for turning rubric grading into mastery state.

## Frontend entrypoint

The grading cockpit is mounted at `/admin/grading` in `frontend/src/App.jsx`.
The primary page implementation is in `frontend/src/pages/GradingPage2.jsx`.

## Backend contract

The grading cockpit loads data from these backend endpoints:

- `GET /api/grading/classes`
- `GET /api/grading/classes/:classId/assignments`
- `GET /api/grading/assignments/:assignmentId/classes/:classId/students`
- `GET /api/grading/submissions/:submissionId`
- `POST /api/grading/submissions/:submissionId/score`
- `PATCH /api/grading/submissions/:submissionId/return`
- `PATCH /api/grading/quiz-submissions/:submissionId/return`
- `PATCH /api/grading/quiz-submissions/:submissionId/reset`

## Frontend data flow

### Deep-link initialization and URL cleanup

`GradingPage2.jsx` captures deep-link query params once on mount (`classId`, `assignmentId`, `submissionId`, `quizId`, `contentType`) and then removes the query string from the browser URL using `window.history.replaceState(...)`.

Current purpose of this behavior:

- preserve deep-link entry behavior at initial load
- reduce leakage of grading identifiers through browser history and referrer propagation after mount

### Step 1: class list

On mount, `GradingPage2.jsx` fetches `GET /api/grading/classes`.
The returned list is used to populate the class picker and compute course/module metadata.

### Step 2: assignment list

When a class is selected, the page requests `GET /api/grading/classes/:classId/assignments`.
This endpoint returns assignments in the class plus linked rubric metadata and grading counts.

### Step 3: student submission list

After an assignment is chosen, the page requests:

- `GET /api/grading/assignments/:assignmentId/classes/:classId/students`

The returned rows include each student’s submission status, submission ID, and grading progress.

### Step 4: submission detail

When a student is selected, the grading cockpit loads full grading detail from:

- `GET /api/grading/submissions/:submissionId`

The payload includes:

- submission metadata
- student and class context
- assignment context
- rubric criteria and selectable rating options
- linked outcome metadata
- assessment mode information

### Step 5: save scores

The in-page grading form posts rubric scores to:

- `POST /api/grading/submissions/:submissionId/score`

The request payload includes selected criterion ratings, numeric scores, optional grader notes, and a `finalize` flag.

In quiz mode, the page may also post quiz answer scores and return actions through the quiz-specific grading endpoints:

- `PATCH /api/grading/quiz-submissions/:submissionId/return`
- `PATCH /api/grading/quiz-submissions/:submissionId/reset`

## UI structure

The grading cockpit uses a three-column workflow:

1. class picker
2. assignment list
3. student submission list + grading detail

It also supports a graded toggle to hide fully graded assignments and a refresh after scoring.

## Developer implications

- The grading cockpit is the only frontend page that writes rubric scores directly through `/api/grading/submissions/:submissionId/score`.
- The backend grading route is the gateway for both raw submission scoring and snapshot generation.
- `GradingPage2.jsx` is the authoritative grading workflow page and should be updated when the grading API payload changes.

## Related pages

- `docs/developer/api.md` — grading backend contract and endpoint docs
- `docs/developer/workflows.md` — grading lifecycle within the broader app
- `docs/developer/data-model.md` — submission, rubric, and snapshot relationships


**Last updated:** 2026-07-08

# Assignments

This page documents the current developer implementation of assignment authoring in `ILS-dev`.
Assignments are the work items students submit, and they link curriculum modules to rubrics for grading.

## Frontend entrypoints

The assignment admin screens are mounted in `frontend/src/App.jsx`:

- `Route path="admin/assignments" element={<AssignmentsPage />} />`
- `Route path="admin/assignments/new" element={<AssignmentForm />} />`
- `Route path="admin/assignments/:assignmentId" element={<AssignmentForm />} />`

The relevant frontend pages are:

- `frontend/src/pages/AssignmentsPage.jsx`
- `frontend/src/pages/AssignmentForm.jsx`

## Backend contract

Assignment creation and editing use these endpoints:

- `GET /api/assignments`
- `GET /api/assignments/:id`
- `POST /api/assignments`
- `PUT /api/assignments/:id`
- `DELETE /api/assignments/:id`

Supporting reference data comes from:

- `GET /api/modules`
- `GET /api/rubrics`
- `GET /api/rubrics/:id`

## Frontend data flow

### Assignments list

`AssignmentsPage.jsx` loads either:

- `/assignments` for the global assignment list, or
- `/modules/:moduleId/assignments` when browsing assignments within a specific module.

The page supports filtering by module, status, due date, and text search.
It displays assignment title, module context, status, submission counts, and action controls.

### Assignment form

`AssignmentForm.jsx` is the main create/edit screen.
It loads a rubric list from `/rubrics` and optionally loads assignment details from `/assignments/:id` when editing.

The form model includes:

- title, description, objectives, case study, instructions
- module assignment (`module_id`)
- points possible and grading display mode
- submission type and entry type controls
- due date, available dates, and status
- exportable rubric links via `rubric_ids`

### Rubric preview and selection

The assignment form supports selecting one or more rubrics from the rubric bank.
It also previews rubric details by fetching `GET /rubrics/:id` when a rubric is selected in the picker.

### Autosave and drafts

When editing an existing assignment, `AssignmentForm.jsx` uses an autosave mechanism for draft state.
It serialises `entry_types` into `submission_entry_types` and sends the full form payload to the backend.

## Developer notes

- Assignment data must be written with `rubric_ids` so grading and heatmap endpoints can resolve rubric-to-outcome links.
- The page normalises `submission_entry_types` as JSON and uses `allowed_extensions` only when file submissions are enabled.
- Assignment route changes should be reflected in both `AssignmentsPage.jsx` and `AssignmentForm.jsx`.

## Related pages

- `docs/developer/api.md` — assignment and rubric backend endpoints
- `docs/developer/grading-cockpit.md` — how assignments appear in the grading workflow
- `docs/developer/rubrics.md` — rubric authoring and criteria linkages


**Last updated:** 2026-07-08

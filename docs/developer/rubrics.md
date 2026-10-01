# Rubrics

This page documents the current developer implementation of rubric authoring in `ILS-dev`.
Rubrics are reusable grading instruments that connect criteria to outcomes.

## Frontend entrypoints

The rubric management screens are mounted in `frontend/src/App.jsx`:

- `Route path="admin/rubrics" element={<RubricsPage />} />`
- `Route path="admin/rubrics/new" element={<RubricEditor />} />`
- `Route path="admin/rubrics/:id" element={<RubricEditor />} />`

The relevant frontend pages are:

- `frontend/src/pages/RubricsPage.jsx`
- `frontend/src/pages/RubricEditor.jsx`

## Backend contract

Rubric authoring uses these endpoints:

- `GET /api/rubrics`
- `GET /api/rubrics/:id`
- `POST /api/rubrics`
- `PUT /api/rubrics/:id`
- `DELETE /api/rubrics/:id`
- `GET /api/rubrics/categories`
- `GET /api/rubrics/criteria`

## Frontend data flow

### Rubric list

`RubricsPage.jsx` loads the rubric bank and category filters using:

- `/rubrics`
- `/rubrics/categories`

The page renders each rubric’s title, category, criteria count, total points, and pass threshold.
It also supports edit and delete actions.

### Rubric editor

`RubricEditor.jsx` is the create/edit screen.
The editor supports:

- adding and editing rubric criteria
- editing rating rows for each criterion
- linking criteria to outcomes using `OutcomePicker`
- previewing rubric details
- fine-grained point and description fields

### Outcome-linked criteria

Each rubric criterion can link to a single outcome via `linked_outcome_id`.
This linkage is critical for heatmap and outcome mastery reporting because:

- `assignment_rubrics` uses the rubric to connect assignments to outcomes indirectly
- `rubric_criteria.linked_outcome_id` enables snapshots to map criterion scoring to outcomes
- `student_outcome_snapshots` is computed from rubric criteria scores and linked outcomes

## Developer notes

- The rubric editor uses inline criteria and ratings state; the final payload is sent as a full rubric object to the backend.
- When a criterion is linked to an outcome, the page may lock or derive rating metadata from the selected outcome.
- Changes to rubric payload shape should be coordinated with `GradingPage2.jsx`, `AssignmentForm.jsx`, and heatmap/cockpit contracts.

## Related pages

- `docs/developer/api.md` — rubric API contract
- `docs/developer/data-model.md` — rubric criteria and outcome mapping
- `docs/developer/assignments.md` — assignment-to-rubric linkage
- `docs/developer/grading-cockpit.md` — how rubrics are used in grading


**Last updated:** 2026-07-08

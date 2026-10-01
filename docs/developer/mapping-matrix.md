# Mapping Matrix

This page documents the Curriculum Mapping Matrix feature in ILS. The matrix shows which assignments cover which outcomes through rubric criteria links.

## Frontend entrypoint

- Route: `/admin/mapping`
- File: `ILS-dev/frontend/src/pages/MappingMatrixPage.jsx`
- The page is mounted in `ILS-dev/frontend/src/App.jsx` under the admin routes.

## What the matrix shows

- Rows: active assignments
- Columns: outcomes
- A filled cell means the assignment is linked to the outcome via rubric criteria
- Hovering a cell shows which rubric and how many criteria connect the assignment to that outcome

> Note: This mapping matrix reflects derived outcome coverage only. It shows outcomes that are actually linked through rubric criteria on graded assignments, not a separate teacher-declared curriculum intent layer.

## Frontend behavior

`MappingMatrixPage.jsx` performs the following steps:

1. Fetch `/api/matrix` on mount using `fetchApi('/matrix')`.
2. Build category bands from outcome categories.
3. Build an assignment list grouped by module and optionally filtered by:
   - course
   - module
   - outcome category
   - coverage state (`all`, `covered`, `uncovered`)
4. Render the matrix table with outcome codes as vertical headers.
5. Render each assignment row with a dot for each covered outcome cell.
6. Show a tooltip on hover with rubric details for the selected assignment-outcome link.

### Filters and stats

The page supports:

- course filter
- module filter (scoped to selected course)
- outcome category filter
- coverage filter

It also computes summary stats:

- number of assignments
- number of outcomes
- covered cells count and percentage
- uncovered outcome count

## Backend API

The matrix backend route is `GET /api/matrix` in `ILS-dev/backend/routes/matrix.js`.

The backend returns:

- `courses` — course lookup list
- `outcomes` — outcome list with category metadata
- `modules` — module list with course context
- `assignments` — assignment rows with module/course context
- `coverage` — map of assignment_id → outcome IDs covered by that assignment
- `links` — detailed link rows for hover tooltips

### How coverage is computed

`/api/matrix` loads assignments and includes:

- `Module` and its `Course`
- `Rubric` details linked to assignments
- `RubricCriterion` rows with `linked_outcome_id`

For each assignment, the backend builds:

- `coverage[assignment_id]` — unique list of linked outcome IDs
- `links` — one row per rubric criterion link with assignment, rubric, criterion, and outcome metadata

## Developer implications

- The matrix is a read-only audit view; it does not write data.
- It depends on rubric criteria correctly linking outcomes through `linked_outcome_id`.
- Changes to rubric structure, assignment-rubric relationships, or outcome linkage will affect both the backend matrix route and the frontend rendering logic.
- The hover tooltip groups linked criteria by rubric so users can understand why a cell is covered.

## Related content

- `docs/developer/rubrics.md` — rubric criteria and outcome linking
- `docs/developer/outcomes.md` — outcome definitions and categories
- `docs/developer/heatmap.md` — student mastery view based on outcome snapshots
- `docs/developer/api.md` — API route reference for matrix data

## Recent changes (June 2026)

- The mapping page backend was corrected to resolve assignment coverage via the `module_items` junction rather than a removed direct `module` foreign key. Developer readers: see `backend/routes/matrix.js` for details.


**Last updated:** 2026-07-08

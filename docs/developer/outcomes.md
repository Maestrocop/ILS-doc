# Outcomes

This page documents the Outcome Bank in ILS. Outcomes are the core learning goals used throughout modules, assessments, grading, heatmaps, and classroom intelligence.

## Admin interface

- Frontend route: `/admin/outcomes`
- Files:
  - `ILS-dev/frontend/src/pages/OutcomesPage.jsx`
  - `ILS-dev/frontend/src/pages/OutcomeForm.jsx`
- Outcomes are managed through a searchable bank with category filters and inline edit/delete actions.
- The page supports:
  - listing outcomes
  - searching by code, friendly name, or description
  - filtering by category
  - creating a new outcome
  - editing an existing outcome
  - deleting an outcome

## Outcome list behaviors

`OutcomesPage.jsx` loads outcomes from the backend using `GET /api/outcomes`.
- It also loads categories from `GET /api/outcome-categories`.
- It optionally loads frameworks from `GET /api/frameworks`.
- The UI normalizes response payloads into camelCase fields for the table.

Search and filtering behavior:
- Search text filters outcome code, friendly name, and description.
- Category selector supports:
  - All categories
  - Uncategorized outcomes
  - Specific category values

Each outcome card shows:
- code
- friendly name
- mastery threshold
- category name
- framework name
- calculation method
- custom calculation flag

## Outcome form

`OutcomeForm.jsx` handles both create and edit flows.
- New outcome route: `/admin/outcomes/new`
- Edit outcome route: `/admin/outcomes/:id/edit`
- The form loads:
  - outcome categories from `GET /api/outcome-categories`
  - frameworks from `GET /api/frameworks`
  - calculation methods from `GET /api/reference/calculation-methods`
  - existing outcome data from `GET /api/outcomes/:id` when editing
  - existing mastery levels from `GET /api/outcomes/:id/mastery-levels` when editing

Form fields include:
- `code`
- `friendly_name`
- `description`
- `category_id`
- `framework_id`
- `mastery_threshold`
- `calculation_method`
- custom calculation indication
- mastery level definitions

The form supports nested mastery-level editing:
- create new levels
- update existing levels
- delete removed levels
- mastery level payloads are synced with the backend after the main outcome save

## Backend API

The outcomes backend is mounted under `/api/outcomes` in `ILS-dev/backend/index.js`.

Routes implemented in `ILS-dev/backend/routes/outcomes.js`:
- `GET /api/outcomes` — list outcomes, optionally filtered by category or uncategorized
- `POST /api/outcomes` — create an outcome
- `GET /api/outcomes/:id` — fetch a single outcome, including parameters and mastery levels
- `PUT /api/outcomes/:id` — update an outcome
- `DELETE /api/outcomes/:id` — delete an outcome

Nested mastery-level routes:
- `GET /api/outcomes/:id/mastery-levels`
- `POST /api/outcomes/:id/mastery-levels`
- `PUT /api/outcomes/:id/mastery-levels/:level`
- `DELETE /api/outcomes/:id/mastery-levels/:level`

## Outcome model notes

Outcomes are stored as a global intelligence entity. They are not owned by modules or courses directly.
- The API normalizes `calculation_method` and determines `is_custom_calculation` by comparing with the category default.
- Outcome parameters are stored separately as records on `OutcomeParameter` when available.
- Outcome mastery levels are stored in `OutcomeMasteryLevel` and returned alongside the single outcome payload.

## Integration points

Outcomes are used across the product:
- module editing: `ModuleForm.jsx` loads `/modules/bank/outcomes` and links outcome IDs to modules
- assignment criteria: outcomes appear in criteria pickers and rubric linkers
- heatmap and cockpit dashboards: outcome IDs, codes, and categories appear in classroom performance reports
- grading: rubric criteria map to `linked_outcome_id`, which drives outcome-level snapshots and mastery calculations


**Last updated:** 2026-07-08

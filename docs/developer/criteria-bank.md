# Criteria Bank

This page documents the ILS Criteria Bank feature. The Criteria Bank shows all rubric criteria across the app, including linked outcomes and rating scales.

## Admin UI

- Frontend route: `/admin/criteria`
- File: `ILS-dev/frontend/src/pages/CriteriaBankPage.jsx`
- The page is accessible from the admin sidebar under `Criteria Bank`.

### User interactions

- The page fetches all criteria from `GET /api/rubrics/criteria`.
- Users can:
  - search criteria by title, description, rubric title, or linked outcome
  - filter criteria by `All`, `Linked to Outcome`, or `Free`
  - click through to the owning rubric for editing
  - create a new rubric from the header button

## Data grouping

The Criteria Bank groups criteria by parent rubric.
- Each rubric section shows the rubric title and a count of criteria.
- Criteria rows display:
  - criterion title and description
  - rating chips with points and labels
  - linked outcome code, friendly name, and threshold
  - maximum criterion points (sum of rating points)

## Backend API

The Criteria Bank endpoint is implemented in `ILS-dev/backend/routes/rubrics.js`.

Route:
- `GET /api/rubrics/criteria`

This route returns all rubric criteria with related data:
- `RubricCriterion` records
- associated `RubricRating` rows (`ratings`)
- parent `Rubric` summary (`rubric`)
- linked `Outcome` metadata (`linkedOutcome`)

The backend uses Sequelize `findAll()` with `include` to return each criterion and its related rubric, ratings, and linked outcome.

## Integration with outcomes and rubrics

- Criteria may link to outcomes through `linked_outcome_id`.
- Linked outcome data is joined and displayed as a badge in the Criteria Bank.
- Rubric creation/editing flows control actual criterion persistence and linking.
- The page is a read-only overview and does not itself create or edit criteria.

## Notes

- The Criteria Bank is a convenience view for cross-rubric visibility.
- It is driven by the `rubrics` route group and depends on rubric criteria metadata rather than a separate criteria-specific API.
- The page is useful for auditing whether rubric criteria are mapped to learning outcomes.


**Last updated:** 2026-07-08

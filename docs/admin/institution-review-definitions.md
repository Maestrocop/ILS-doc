# Institution-specific Review Definitions — Summary

This document describes the existing implementation for institution-scoped progression review definitions. It is a factual summary of what exists in the codebase and where to find it; it does not change any code in `ILS-dev`.

## What exists

- Definitions are represented by the `ProgressionReviewDefinition` model and stored in `progression_review_definitions`.
- Definitions may be scoped to an `institution_id`; when present, lookups prefer institution-level definitions for classes belonging to that institution.
- Definitions include configuration fields such as `local_name`, `description`, `trigger_months`, `is_binding`, `applicable_year`, `available_outcomes`, thresholds, decision stages, and UI labels.
- Per-definition policy flags and required evidence codes are stored in `progression_review_decision_policies` and related fields on the definition (e.g., `required_evidence_types`, `binding_required_types`).

## How the code resolves definitions

- `backend/lib/reviewDefinition.js` provides `getDefinitionForClass(sequelize, classId)` which returns the active `ProgressionReviewDefinition` for a given class — it falls back from class → module → course → institution.
- The helper `getPassThreshold(sequelize, classId, fallback)` returns a threshold value (warning/decision threshold) for use in server-side computations and dashboards.

## Admin UI

- The `ProgressionReviewDefinitionsTab` component in the frontend allows admins to create and edit definitions, set decision stages (2 or 3), define thresholds, and upload policy documents.
- Event types and action types are configurable per definition via the UI and persisted through the API endpoints under `/api/progression-reviews/definitions`.

## Seeds and examples

- `backend/scripts/seed_progression_definition.cjs` seeds an example BSA definition for an institution and creates an associated `progression_review_decision_policies` row.

## Where to find the code

- `ILS-dev/backend/models/ProgressionReviewDefinition.js`
- `ILS-dev/backend/lib/reviewDefinition.js`
- `ILS-dev/backend/scripts/seed_progression_definition.cjs`
- `ILS-dev/frontend/src/components/ProgressionReviewDefinitionsTab.jsx`

This page documents existing functionality only. No edits are made to `ILS-dev` by this file.

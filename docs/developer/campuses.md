# Campuses

This page documents the current developer implementation of campus management in `ILS-dev`.
Campuses are the second-level organizational units under institutions.

## Frontend entrypoint

The campus page is mounted at `/admin/campuses` in `frontend/src/App.jsx`.
The page implementation is in `frontend/src/pages/CampusesPage.jsx`.

## Backend contract

The campus frontend calls the backend campus API at `/api/campuses`.
The backend route implementation is in `backend/routes/campus.js`.

Supported endpoints:

- `GET /api/campuses` — list all campuses
- `POST /api/campuses` — create a new campus
- `GET /api/campuses/:id` — load a single campus
- `PUT /api/campuses/:id` — update a campus
- `DELETE /api/campuses/:id` — soft delete a campus
- `GET /api/campuses/:campus_id/reporting-rules` — get campus reporting rules
- `POST /api/campuses/:campus_id/reporting-rules` — upsert reporting rules

## Frontend behavior

### Campus list

`CampusesPage.jsx` loads campus data on mount from `fetchApi('/campuses')`.
It renders a simple list of campus names and currently supports display only.

### Campus reporting rules

The campus backend route also exposes campus reporting rule endpoints used by teacher intelligence features.
These reporting rules include:

- `low_activity_days`
- `success_threshold`
- `reteach_threshold`

The frontend uses these rules in classroom intelligence and Cockpit state calculations.

## Developer notes

- The campus list page is a simple read-only view in the current implementation.
- Creating or editing campuses is handled by the backend API contract, but there is no dedicated frontend edit form in the current code.
- The backend enforces `institution_id` and `name` when creating campuses.
- Campus deletion is soft delete via `deleted_at`.

## Related developer content

- `docs/developer/institutions.md` — institutions own campuses
- `docs/developer/data-model.md` — campus entity in the vertical hierarchy
- `docs/developer/api.md` — campus API contract and supporting routes
- `docs/developer/classroom-intelligence.md` — campus reporting rules influence teacher intelligence


**Last updated:** 2026-07-08

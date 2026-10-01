# Institutions

This page documents the current developer implementation of institution management in `ILS-dev`.
Institutions are the top-level organizational entities for the curriculum system.

## Frontend entrypoints

The institution admin screens are mounted in `frontend/src/App.jsx`:

- `Route path="admin/institutions" element={<InstitutionsPage />} />`
- `Route path="admin/institutions/new" element={<InstitutionForm />} />`
- `Route path="admin/institutions/:id" element={<InstitutionForm />} />`

The relevant frontend pages are:

- `frontend/src/pages/InstitutionsPage.jsx`
- `frontend/src/pages/InstitutionForm.jsx`

## Backend contract

The frontend uses the institution API at `/api/institutions`.
The backend route implementation is in `backend/routes/institution.js`.

Supported endpoints:

- `GET /api/institutions` — list all institutions
- `POST /api/institutions` — create a new institution
- `GET /api/institutions/:id` — load one institution for editing
- `PUT /api/institutions/:id` — update an institution
- `DELETE /api/institutions/:id` — delete an institution

## Frontend behavior

### Institutions list

`InstitutionsPage.jsx` loads the institution list on mount using `fetchApi('/institutions')`.
It supports:

- searching by name, code, or location
- inline delete for admin users
- navigation to the institution edit page
- a `New Institution` button for admin users

The list renders these columns:

- Name
- Code
- Location
- Status

### Institution form

`InstitutionForm.jsx` handles both creation and editing.
When `id` is `new`, it renders a blank form.
When editing, it loads institution data from `fetchApi(`/institutions/${id}`)`.

The form fields include:

- `name`
- `code`
- `description`
- `location`
- `website`
- `contact_email`
- `logo_url`
- `status`

When the user saves, the form sends:

- `POST /api/institutions` for new institutions
- `PUT /api/institutions/:id` for updates

### Delete behavior

The institutions page confirms deletion before calling `DELETE /api/institutions/:id`.
It reloads the list after successful delete.

## Notes

- Institution management is restricted to admin users in the frontend.
- The backend route is simple and uses Sequelize model CRUD methods directly.
- There is no frontend validation beyond the basic form state and network error handling.

## Related developer content

- `docs/developer/course-creation.md` — institutions are the root of curriculum ownership
- `docs/developer/data-model.md` — institution entity in the vertical hierarchy
- `docs/developer/api.md` — backend API contract and route overview


**Last updated:** 2026-07-08

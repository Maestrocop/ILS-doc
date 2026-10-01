# Themes

This page documents the current Theme Bank implementation in ILS. Themes are global learning/theme tags that can be linked to modules, and they are managed through the admin UI and backend API.

## What a Theme is

- Themes are global entities, not owned by a specific course or module.
- In `ILS-dev/backend/models/theme.js`, the `Theme` model defines:
  - `id`
  - `name`
  - `description`
  - `status`
  - `primary_color`
- The model intentionally avoids `module_id`; themes are linked to modules through a junction table (`module_themes`).

## Admin UI

- Frontend route: `/admin/themes`
- Files:
  - `ILS-dev/frontend/src/pages/ThemesPage.jsx`
  - `ILS-dev/frontend/src/pages/ThemeForm.jsx`
- `ThemesPage.jsx` loads theme records from `GET /api/themes`.
- The page supports:
  - listing existing themes
  - creating a new theme
  - editing a theme
  - deleting a theme

### Theme form fields

`ThemeForm.jsx` exposes:
- `name` (required)
- `description`
- `primary_color`

The form also tracks dirty state so save is only enabled when changes exist.

## Backend API

The Theme Bank backend is mounted under `/api/themes` in `ILS-dev/backend/index.js`.

Routes implemented in `ILS-dev/backend/routes/theme.js`:
- `GET /api/themes` — list all themes
- `GET /api/themes/:id` — fetch one theme
- `POST /api/themes` — create a theme
- `PUT /api/themes/:id` — update a theme
- `DELETE /api/themes/:id` — delete a theme

### Payload shape

`POST /api/themes` and `PUT /api/themes/:id` accept:
- `name` or `title`
- `description`
- `status`
- `primary_color`

The backend normalizes `title` to `name` for compatibility.

## Module linking

Themes are assigned to modules in `ILS-dev/frontend/src/pages/ModuleForm.jsx`:
- `ModuleForm.jsx` loads the themes bank from `GET /api/themes`.
- Selected themes are stored as `theme_ids` on the module payload.
- The form shows a list of available themes and lets the user toggle them for the current module.

## Model associations

In `ILS-dev/backend/models/index.js`:
- `Course.hasMany(Module)`
- `Module.belongsToMany(Theme, { through: ModuleTheme, ... })`
- `Theme.belongsToMany(Module, { through: ModuleTheme, ... })`

This makes `themes` a reusable, cross-module intelligence layer entity.

## Implementation notes

- Themes are rendered in the module editor as a selection list.
- The Theme Bank UI uses a generic `DataTable` component and action menu controls.
- The theme administration flow supports both creation and inline editing from the same form.


**Last updated:** 2026-07-08

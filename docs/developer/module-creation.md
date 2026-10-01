# Module Creation

This page documents how modules are created in ILS, using the live `ILS-dev` implementation as the source of truth.

## Entry points

- Frontend route: `/admin/modules`
- Creation route: `/admin/modules/new`
- Module editor file: `ILS-dev/frontend/src/pages/ModuleForm.jsx`
- Route registration: `ILS-dev/frontend/src/App.jsx`

## User flow

1. The user opens the module administration page at `/admin/modules`.
   - The module bank page lists existing modules and provides management actions.
   - A `New Module` entry point is available from the admin modules UI.

2. The user navigates to `/admin/modules/new`.
   - `App.jsx` maps this route to `ModuleForm.jsx`.
   - The page title becomes `Create Module`.

3. The module editor loads supporting data.
   - `ModuleForm.jsx` fetches reference data from these endpoints:
     - `GET /api/courses` for the course selector
     - `GET /api/modules/bank/outcomes` for the outcomes bank
     - `GET /api/modules/bank/ref_teaching_methods` for teaching method options
     - `GET /api/modules/bank/assignments` for assessment type fallback values
     - `GET /api/themes` for module theme selection
     - `GET /api/assessment-types` for assessment type options
   - These calls populate the editor UI, but module creation itself is triggered by the module save action.

4. The user enters module identity and curriculum details.
   - Required fields for creation:
     - `Course` (selected from `coursesBank`)
     - `Module Name` (`title`)
   - Optional fields include:
     - `Module Code` (`code`)
     - `Level` (`level`)
     - `Duration` (`duration`)
     - `Description` (`description`)
     - Themes (`theme_ids`)
     - Objectives (`objectives`)
     - Structured weekly content (`structures`)
     - Module assessments (`assessments`)
     - Teaching methods (`teaching_method_ids`)

5. The user submits the form.
   - `ModuleForm.jsx` calls `handleSave()`.
   - It builds a payload and sends it to the backend via `fetchApi()`.
   - For a new module, the request is:
     - `POST /api/modules`

## Backend API and persistence

- Backend route file: `ILS-dev/backend/routes/module.js`
- Route mount: `ILS-dev/backend/index.js` mounts `/api/modules` to this router.

### `POST /api/modules`

- The backend requires:
  - `payload.title`
- It also expects `payload.course_id` for a valid module.
  - If `course_id` is not provided, the backend currently defaults it to `1000`.
- The backend persists a minimal module row with:
  - `course_id`
  - `title`
  - `code`
  - `duration`
  - `level`
  - `weight`

- On success, it returns HTTP `201` with the created module object.

## Exact frontend-to-backend payload

`ModuleForm.jsx` sends these fields for module creation:

- `title`
- `code`
- `description`
- `duration`
- `level`
- `course_id`
- `opleidingId` (legacy course id alias)
- `structure` and `structures` (array of week/topic/activity/output/order objects)
- `outcome_ids` (array of selected outcome IDs)
- `assessment` and `assessments` (array of module assessment objects)
- `teaching_methods` and `teaching_method_ids`
- `theme_ids`

The backend creation route only persists the core module row and does not yet process child arrays on `POST /api/modules`.

## Trigger chain

- UI: `New Module` button or direct route `/admin/modules/new`
- UI: `ModuleForm.jsx` loads supporting banks and renders the editor
- UI: `handleSave()` builds the module payload
- API: `POST /api/modules`
- Backend: `backend/routes/module.js` creates a `Module` row through Sequelize
- DB: new `modules` table row is inserted
- UI: on success, the editor navigates back to `/admin/modules`

## Important implementation notes

- `ModuleForm.jsx` is the authoritative module editor.
- It uses `fetchApi()` from `ILS-dev/frontend/src/lib/api.js`, which prefixes requests with `/api`.
- `ModuleForm.jsx` also synchronizes module objectives after the module row is created, using:
  - `POST /api/modules/:id/objectives`
  - `PUT /api/module-objectives/:id`
  - `DELETE /api/module-objectives/:id`
- The module creation backend route is minimal and only creates the core row. Additional module child data is handled later on edit through route `PUT /api/modules/:id`.

## Missing information in code

- The POST `/api/modules` backend handler does not persist `theme_ids`, `assessment`, `structures`, or `teaching_method_ids` at creation time.
- That means the current implementation creates the module row first, and richer module content is managed in subsequent edit/save flows.


**Last updated:** 2026-07-08

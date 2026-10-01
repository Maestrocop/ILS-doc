# Setup

This page describes how to run the documentation site and how to reference the ILS application repository without changing it.

## ILS-doc local preview

The docs site is hosted separately from the application code.

```powershell
cd C:\Users\0102663\Projects\bim\ILS-doc
python -m pip install mkdocs mkdocs-material
mkdocs serve --dev-addr 127.0.0.1:8000
```

- Use `mkdocs serve` to preview documentation changes live in the browser.
- Use `mkdocs build` to verify that the site compiles correctly.
- Keep all documentation changes inside `ILS-doc`.

## ILS-doc environment

This repo does not require the ILS application to build the documentation.
It is safe to run `mkdocs` from `ILS-doc` without starting the backend or frontend.

If you are working with documentation only:

- `cd C:\Users\0102663\Projects\bim\ILS-doc`
- `mkdocs serve --dev-addr 127.0.0.1:8000`
- edit docs under `docs/`
- update `mkdocs.yml` when adding pages or sections

## ILS-dev application reference setup

The application repo is `C:\Users\0102663\Projects\bim\ILS-dev`.

The main app is split into two folders:

- `backend` — Node.js API server
- `frontend` — React + Vite web client

### Backend workbench

```powershell
cd C:\Users\0102663\Projects\bim\ILS-dev\backend
npm install
npm run create-db
npm run dev
```

Key backend scripts:

- `npm run dev` — start the backend with live reload
- `npm run create-db` — create the local database and run migrations
- `npm run test:reporting` — run backend reporting and outcome-related tests
- `npm run seed:heatmap-realism` — seed realistic heatmap data for demo scenarios
- `npm run check:no-hardcoded-db` — verify no hardcoded DB names exist
- `npm run backfill:outcome-snapshots` — regenerate outcome snapshot history

The backend uses `DATABASE_URL` from `ILS-dev/backend/.env` to connect to PostgreSQL.
Do not hardcode database connection strings in application files.

### Frontend workbench

```powershell
cd C:\Users\0102663\Projects\bim\ILS-dev\frontend
npm install
npm run dev
```

Key frontend scripts:

- `npm run dev` — start the React app with Vite
- `npm run build` — create a production build
- `npm run preview` — preview the production build locally
- `npm run test:playwright` — run end-to-end Playwright tests

The frontend uses `VITE_API_URL` to determine the backend API base URL.
When running locally, the frontend usually proxies `/api` requests to `http://localhost:4000`.

## Environment guidance

- `ILS-doc` is the only repo you should edit for documentation updates.
- `ILS-dev` is the application repo and should only be read as source material for facts.
- Keep `ILS-doc` content aligned with real `ILS-dev` behavior and avoid speculative documentation.

## Important boundary rule

- `ILS-doc` is the documentation repo and is the only repo you should edit for doc changes.
- `ILS-dev` is the application repo and should only be read for feature discovery.
- Do not commit or modify any application files in `ILS-dev` unless specifically requested.

## Documentation workflow

- Add new docs pages under `docs/developer`, `docs/concepts`, `docs/teacher`, `docs/admin`, `docs/student`, or `docs/management`.
- Update `mkdocs.yml` navigation when new pages are added.
- Keep guide content focused on what the system does and why it matters for each user role.
- Link architecture and terminology back to the actual app pages and route groups in `ILS-dev`.
- Run `mkdocs build` after each major content update to catch formatting or Markdown issues.

## Tracking and planning

- Active documentation work is tracked in GitHub Project 5 (`project5.json`).
- Use the project board to keep priority work visible and aligned with the current documentation plan.
- The highest priority is Developer Guide content, followed by Teacher, Admin, Student, and Management guides.


**Last updated:** 2026-07-08

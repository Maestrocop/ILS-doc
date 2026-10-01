# Key Technical Decisions

This page captures the core architectural decisions for the ILS documentation and application.

## Backend platform

- Choose **Node.js + Express + Sequelize** for backend implementation.
- Use Sequelize for data modeling and migrations, but keep schema changes in SQL migration files.
- Avoid runtime schema generation or automatic sync.

## Migration policy

- Follow a strict **database-first** policy.
- Write all schema changes in SQL migrations under `backend/migrations/`.
- Ensure migrations are idempotent and include guard clauses when needed.
- Do not rely on `sequelize.sync()` in any environment.

## Data handling

- Convert `BigInt` values to strings in JSON responses.
- This preserves compatibility with browser clients and avoids serialization errors.

## Domain separation

- Keep the **vertical curriculum hierarchy** separate from the **intelligence layer**.
- Vertical entities include: `institutions`, `campuses`, `courses`, `modules`, `assignments`, `classes`, and `students`.
- Intelligence entities include: `outcomes`, `rubrics`, `criteria`, `themes`, `snapshots`, and `trends`.

## Documentation separation

- Keep the docs repository separate from the application repository.
- Track active docs work in `docs/phase-a-structure` instead of directly editing site pages.
- Use the left-side navigation for developer content, and avoid single-page guides for long material.


**Last updated:** 2026-07-08

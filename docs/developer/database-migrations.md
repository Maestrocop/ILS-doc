# Database & Migrations

This page documents the current database conventions and migration workflow for ILS.
All content is written in `ILS-doc`; the application code remains in `ILS-dev`.

## Database stack

The ILS backend uses PostgreSQL as its database.

- The database connection is configured through `DATABASE_URL` in `ILS-dev/backend/.env`.
- The backend uses Sequelize as the ORM for model definitions and queries.
- Models are defined in `ILS-dev/backend/models/*.js`.
- The application does not rely on `sequelize.sync()` during normal startup.

## Schema conventions

The current implementation follows these schema conventions:

- Primary keys are `BIGINT` identity columns.
- Soft deletes are implemented via the `deleted_at` timestamp.
- Standard timestamp fields are `created_at` and `updated_at`.
- Sequelize models use `underscored: true`, mapping JavaScript property names to snake_case database columns.
- Model definitions and associations are the main source of truth for object relationships.

## Migration workflow

The database schema is managed through SQL migrations.

- Migration files live in `ILS-dev/backend/migrations/`.
- The backend startup flow does not auto-sync models; migrations are the authoritative schema source.
- The repository uses migration scripts and utilities to apply schema changes safely.

### Create and prepare the database

The backend package defines these scripts in `ILS-dev/backend/package.json`:

- `npm run create-db` — initialize the local database and run migrations
- `npm run seed:heatmap-realism` — seed a realistic heatmap data scenario
- `npm run check:no-hardcoded-db` — validate that no hardcoded database names exist in scripts
- `npm run backfill:outcome-snapshots` — regenerate outcome snapshot history
- `npm run seed:admin` — seed administrator user data

## Migration and maintenance policy

The repository is in a stabilization phase, which means:

- Do not add new tables or alter the schema without explicit approval.
- Migrations should be treated as idempotent and safe to run in development.
- Database changes should preserve existing flows and avoid breaking the live application.

## Maintenance scripts

Additional maintenance scripts are available in `ILS-dev/backend/scripts/`.
These support tasks such as:

- applying individual migration SQL files
- validating database configuration
- backfilling snapshots
- seeding admin data

## Reference

This page is a documentation reference for how the ILS database is structured and managed.
All operational details are grounded in the actual `ILS-dev` backend repository.


**Last updated:** 2026-07-08

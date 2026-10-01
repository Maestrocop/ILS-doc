# Utilities & Scripts

This page documents the support scripts and utilities used in the ILS application.
It is based on the actual backend scripts and package metadata from `ILS-dev`.

## Package scripts

The backend defines several useful npm scripts in `ILS-dev/backend/package.json`:

- `npm run start` — start the backend server using `node index.js`
- `npm run dev` — start the backend with `nodemon` and live reload
- `npm run create-db` — initialize the local database and run all migrations
- `npm run test:reporting` — execute backend reporting and outcome-related tests
- `npm run seed:heatmap-realism` — seed realistic heatmap data for demo scenarios
- `npm run check:no-hardcoded-db` — validate there are no hardcoded database names in scripts
- `npm run backfill:outcome-snapshots` — regenerate outcome snapshot history from existing data
- `npm run seed:admin` — seed administrator or admin user data

## Backend utility scripts

The backend includes a set of maintenance and migration helper scripts in `ILS-dev/backend/scripts/`.
These scripts are intended for support tasks and data maintenance, rather than core application behavior.

Important utilities include:

- `apply_migration.cjs` — apply a single migration SQL file manually
- `backfill_outcome_snapshots.cjs` — rebuild or refresh outcome snapshots after data changes
- `check_module_assessments_constraints.cjs` — validate module assessment constraints in the database
- `describe_module_assessments.cjs` — inspect module assessment metadata
- `ensure_module_themes_cols.cjs` — ensure the module themes table has required columns
- `query_module_themes.cjs` — query module theme records for diagnostics
- `seed_admin.cjs` — create or seed administrator account data
- `seed_assessment_descriptions.cjs` — seed assessment description metadata
- `validate_no_hardcoded_db_names.cjs` — ensure scripts do not contain hardcoded database names
- `backup_and_drop_unused_theme_tables.cjs` — backup and remove unused theme-related tables
- `backup_and_drop_unused_theme_tables_option_a.cjs` — alternative cleanup script for unused theme tables

## Usage guidance

These utilities are documented here to help maintainers understand the support tooling.
They are not part of the daily teacher or admin user flows.

When working with these scripts:

- Prefer the documented npm package scripts when available.
- Use `validate_no_hardcoded_db_names.cjs` before making changes to database scripts.
- Use `backfill_outcome_snapshots.cjs` when outcome or snapshot data needs recalculation.
- Apply individual SQL changes only through agreed migration workflows.

## Notes

This documentation is intentionally high-level and process-focused.
If the team needs a deeper maintenance guide, it can be expanded with specific command usage examples and script internals.


**Last updated:** 2026-07-08

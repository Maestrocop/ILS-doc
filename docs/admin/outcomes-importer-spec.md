# Outcomes Importer — Specification

Purpose: define the schema, validation, preview behavior, and merge semantics for importing learning outcomes.

Accepted file formats: CSV (UTF-8), XLSX (first sheet)

Required columns:
- `code` (string) — unique short code, required
- `title` (string) — required
- `description` (string) — optional
- `framework` (string) — optional (maps to existing framework name)
- `level` (string) — optional (e.g., "Introductory", "Advanced")

Validation rules:
- `code` must be unique within file and across existing outcomes (unless merge mode)
- `title` cannot be empty
- `framework` if present must match an existing framework; otherwise flag as warning

Preview behavior:
- Show first 100 rows with status badges: `OK`, `Warning`, `Error`
- Allow inline edit for `code` and `title` in preview
- Provide "Auto-fix" suggestions for common issues (trim whitespace, normalize case)

Merge semantics:
- Modes: `Create only`, `Create or Update (by code)`, `Replace` (danger)
- Default: `Create or Update` with safe heuristics (only overwrite description/title if `--force`)

Example CSV header:
```
code,title,description,framework,level
OUT001,Define variables,Students can define variables,Core,Introductory
```

Reporting:
- After import, produce import report with row statuses and messages (see `admin/import-report.md`).

Permissions: import requires `Admin` or `Designer` per `admin/permissions.md`.

**Last updated:** 2026-07-07

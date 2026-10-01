# ImportShell — Shared import workflow

Purpose: standardise import UX across entities so each importer focuses on schema and validation.

Stages (recommended):
- Upload
- Map (optional)
- Validate
- Preview
- Confirm
- Report

Importer responsibilities:
- Define accepted file types and required columns
- Provide validation rules and error messages
- Implement save/merge semantics

Shell responsibilities:
- File upload UI and progress
- Column mapping UI (for Map stage)
- Validation runner and aggregated error display
- Preview rendering and row-level actions
- Generate downloadable import report

Mapping details
- Allow users to save mappings per source (e.g., Canvas, Moodle)
- Provide example mappings to reduce friction

Example flow: Outcomes importer
1. Admin uploads `outcomes.csv`
2. (Skip Map if native) Validate rows for required fields
3. Preview first 50 rows with inline warnings
4. Confirm import; show final report and downloadable CSV with statuses

**Last updated:** 2026-07-07

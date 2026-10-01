# Data Exchange Hub

Central hub for Export, Import, and Templates. Teachers and Admins use this to move CSV data into and out of the system.

ImportShell flow: Upload → Map → Validate → Preview → Confirm. Sample templates are in `docs/admin/templates/`.

Last updated: 2026-07-08

Export step-by-step
1) Go to `Data Exchange` → `Export`.
2) Choose entity (Students, Grades, Outcomes).
3) Pick template and date range, then `Export`.

Import step-by-step (Admin)
1) `Data Exchange` → `Import` → Choose template.
2) Follow ImportShell flow; admin imports support replay and webhook notifications.

Validation rules
- Required fields must be present; IDs must match existing DB records; numeric fields must be within expected ranges.

Screenshot placeholders
- [screenshot: data-exchange-export]
- [screenshot: data-exchange-import]

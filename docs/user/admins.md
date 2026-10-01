# Admin Guide

Admin documentation for system operators and site administrators: setup, data exchange, templates, permissions, and operational runbooks.

System setup
- Initial setup: follow `backend/README` steps for DB and server (admins only).

Data Exchange hub
- Export: `Data Exchange` → `Export` → select entity (Students, Grades, Outcomes) and template.
- Import: `Data Exchange` → `Import` → follow ImportShell (Upload → Map → Validate → Preview → Confirm). Use sample templates in `docs/admin/templates/`.

Permissions
- Roles: `Teacher`, `Coordinator`, `Admin`. Assign via `Admin` → `Users` → `Manage Roles`.

Backups & migrations
- Backups: run scheduled DB backups to the configured backup root. See `Internal > Backups` for operational steps.

Last updated: 2026-07-08

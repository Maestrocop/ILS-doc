# Data Exchange Permissions (recommended)

Access model recommendations (documentation only):

Who sees the Data Exchange page: `Admin`, `Designer` (default). Teachers and Coordinators export contextually from their pages.

Action permissions (recommended):

| Action | Superadmin / Admin | Designer | Coordinator | Teacher |
|---|---:|---:|---:|---:|
| Export Students | ✓ | — | ✓ (own program) | — |
| Export Modules | ✓ | ✓ | — | — |
| Export Assignments | ✓ | ✓ | — | — |
| Export Outcomes | ✓ | ✓ | — | — |
| Export Rubrics | ✓ | ✓ | — | — |
| Export Grades | ✓ | — | ✓ (own program) | ✓ (own class) |
| Import Students | ✓ | — | — | — |
| Import Modules | ✓ | ✓ | — | — |
| Import Assignments | ✓ | ✓ | — | — |
| Import Outcomes | ✓ | ✓ | — | — |
| Import Grades | ✓ | — | — | — |
| Templates management | ✓ | ✓ | — | — |

Notes:
- Attendance import is strongly discouraged (operational live data). Export only.
- Grade import is admin-only (migration/backfill scenarios).

**Last updated:** 2026-07-07

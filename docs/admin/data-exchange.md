# Data Exchange (Export / Import / Templates)

Overview: evolve the existing `Export Data` page into a unified Data Exchange hub offering three tabs: `Export`, `Import`, and `Templates`.

Key principles
- Reuse the existing export lists; do not redesign the Export UI.
- Build an `ImportShell` that standardises upload, mapping, validation, preview, confirm, and report flows.
- Provide downloadable `Template` and `Example` files for each entity.

Recommended tab order (consistent across tabs):
- Students
- Modules
- Assignments
- Outcomes
- Rubrics
- Grades

Export: keep current functionality as-is.

## Export

The Export tab contains the existing export lists. Quick access anchors:

### Grades

Open the Grades tab to export grade CSVs for scoped classes.

Import: supported imports should initially be: Outcomes, Modules, Assignments, Rubrics, Grades. Start with Outcomes importer to validate the shell.

Templates: provide `Download Template` and `Download Example` for each entity.

Mapping step: optional Map step after upload for non-native formats (CSV column → ILS field). Store mappings for reuse.

Import report: downloadable report showing Imported / Updated / Skipped / Errors with row-level details.

Access: page visible to all roles; each role sees only their slice. Teachers and coordinators land directly on the **Grades** tab (their most relevant export). The class dropdown is scoped by role on the backend (`class_teachers` for teachers, `coordinator_programs` for coordinators). Teachers/coordinators see only one mode button (Export), so the switcher row is hidden for them.

Role matrix (what they see):

| Action / Role | Admin | Designer | Coordinator | Teacher |
|---|---:|---:|---:|---:|
| Export: Students | ✓ | — | ✓ (own programme classes) | — |
| Export: Modules/Assignments/Outcomes/Rubrics | ✓ | ✓ | — | — |
| Export: Grades | ✓ | — | ✓ (own programme classes) | ✓ (own classes) |
| Export: Attendance | ✓ | — | ✓ (own programme classes) | ✓ (own classes) |
| Import tab | ✓ | ✓ | — | — |
| Templates tab | ✓ | ✓ | — | — |

Access restricted block removed — Teachers and coordinators land directly on the **Grades** tab (their most relevant export). The class dropdown is already scoped by role on the backend (`class_teachers` for teachers, `coordinator_programs` for coordinators). Teachers/coordinators see only one mode button (Export), so the switcher row is hidden entirely for them.

Note on combined roles

If a user has both `Teacher` and `Designer` roles (for example, `P. Goen`), they will see the curriculum authoring tools (Export, Import, Templates, Modules, Assignments, Outcomes, Rubrics) because of the `Designer` role, while `Grades & Submissions` and `Attendance` remain scoped to their teacher view and list only the classes they teach. The `class` dropdown is filtered server-side by the `class_teachers` relation when `isTeacher=true` so the user sees only their class (e.g., "BK Jaar 1 — 2025/2026").

Example expected UI for teacher+designer:

- Tabs: `Export | Import | Templates`
- Export sub-list: `Modules, Assignments, Outcomes & Frameworks, Rubrics, Grades & Submissions, Attendance`
- Class dropdown: `BK Jaar 1 — 2025/2026` (only his class)
- Actions: `Download CSV` for current selection


**Last updated:** 2026-07-07

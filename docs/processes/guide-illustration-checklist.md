# Guide Illustration Checklist

This checklist consolidates the current documentation illustration TODO markers across teacher, student, and admin guides.

## Scope

- Source: existing TODO markers in `docs/teacher`, `docs/student`, and `docs/admin`
- Goal: make guide pages easier to use with screenshots, diagrams, legends, and quick-reference tables
- Status key:
  - `Not started`
  - `In progress`
  - `Done`

## Prioritization rules

- `P0`: navigation-critical visuals that help users complete core workflows immediately
- `P1`: interpretive visuals that reduce confusion and improve decision quality
- `P2`: enhancement visuals that improve onboarding and consistency

## P0 backlog

| Priority | Persona | Deliverable | Source page | Type | Status |
|---|---|---|---|---|---|
| P0 | Teacher | Teacher workflow map (Cockpit -> Heatmap -> Intelligence -> Grading -> Interventions) | [docs/teacher/index.md](../teacher/index.md) | Diagram | Not started |
| P0 | Teacher | Cockpit dashboard labeled screenshot | [docs/teacher/cockpit.md](../teacher/cockpit.md) | Screenshot | Not started |
| P0 | Teacher | Student-row callout table or screenshot | [docs/teacher/cockpit.md](../teacher/cockpit.md) | Screenshot/Table | Not started |
| P0 | Student | Student workflow map (Courses -> Curriculum -> Assignments/Quizzes -> Submissions -> Dashboard -> Feedback) | [docs/student/index.md](../student/index.md) | Diagram | Not started |
| P0 | Student | Submission page screenshot with status and upload UI | [docs/student/submissions.md](../student/submissions.md) | Screenshot | Not started |
| P0 | Student | Submission lifecycle timeline | [docs/student/submissions.md](../student/submissions.md) | Diagram | Not started |
| P0 | Student | Dashboard screenshot with courses/assignments/progress callouts | [docs/student/dashboard.md](../student/dashboard.md) | Screenshot | Not started |
| P0 | Student | Feedback panel screenshot (rubric comments, score, revisions) | [docs/student/feedback.md](../student/feedback.md) | Screenshot | Not started |
| P0 | Admin | Admin workflow map (Setup -> Curriculum -> Assessment -> Operations) | [docs/admin/index.md](../admin/index.md) | Diagram | Not started |
| P0 | Admin | Assignments list/form screenshot with scoring and rubric links | [docs/admin/assignments.md](../admin/assignments.md) | Screenshot | Not started |
| P0 | Admin | Campuses + reporting-rules editor screenshot | [docs/admin/campuses.md](../admin/campuses.md) | Screenshot | Not started |
| P0 | Admin | Users management screenshot (table + role assignment) | [docs/admin/users.md](../admin/users.md) | Screenshot | Not started |
| P0 | Admin | Rubric editor screenshot with criterion/rating and linked outcome fields | [docs/admin/rubrics-criteria.md](../admin/rubrics-criteria.md) | Screenshot | Not started |
| P0 | Admin | Settings/reporting-rules screenshot with threshold fields | [docs/admin/settings.md](../admin/settings.md) | Screenshot | Not started |

## P1 backlog

| Priority | Persona | Deliverable | Source page | Type | Status |
|---|---|---|---|---|---|
| P1 | Teacher | Guide reading-order flowchart | [docs/teacher/index.md](../teacher/index.md) | Diagram | Not started |
| P1 | Teacher | Roster screenshot/table with class and student status indicators | [docs/teacher/teacher-roster.md](../teacher/teacher-roster.md) | Screenshot/Table | Not started |
| P1 | Student | Guide reading-order flowchart | [docs/student/index.md](../student/index.md) | Diagram | Not started |
| P1 | Student | Progress report screenshot/table (mastery, trend, confidence) | [docs/student/outcomes.md](../student/outcomes.md) | Screenshot/Table | Not started |
| P1 | Admin | Admin page responsibility summary table | [docs/admin/index.md](../admin/index.md) | Table | Not started |
| P1 | Admin | Assignment statuses quick-reference table | [docs/admin/assignments.md](../admin/assignments.md) | Table | Not started |
| P1 | Admin | Audit logs screenshot (filters, events, detail) | [docs/admin/audit-logs.md](../admin/audit-logs.md) | Screenshot | Not started |
| P1 | Admin | Classes list/edit screenshot with enrollment callouts | [docs/admin/classes.md](../admin/classes.md) | Screenshot | Not started |
| P1 | Admin | Courses vs modules side-by-side field comparison visual | [docs/admin/courses-modules.md](../admin/courses-modules.md) | Table/Diagram | Not started |
| P1 | Admin | Curriculum composer screenshot sequence (period tree, drag/drop, slots) | [docs/admin/curriculum.md](../admin/curriculum.md) | Screenshot sequence | Not started |
| P1 | Admin | Mapping matrix screenshot with legend for gaps/overlaps | [docs/admin/mapping-matrix.md](../admin/mapping-matrix.md) | Screenshot/Legend | Not started |
| P1 | Admin | Teacher dashboard screenshot with metric definitions | [docs/admin/teacher-dashboard.md](../admin/teacher-dashboard.md) | Screenshot/Table | Not started |
| P1 | Admin | My Work screenshot with filters/status/grading entry points | [docs/admin/my-work.md](../admin/my-work.md) | Screenshot | Not started |
| P1 | Admin | Setup Health screenshot with pass/warn/fail examples | [docs/admin/setup-health.md](../admin/setup-health.md) | Screenshot | Not started |

## P2 backlog

| Priority | Persona | Deliverable | Source page | Type | Status |
|---|---|---|---|---|---|
| P2 | Teacher | Teacher pages purpose summary table | [docs/teacher/index.md](../teacher/index.md) | Table | Not started |
| P2 | Student | Student pages purpose summary table | [docs/student/index.md](../student/index.md) | Table | Not started |
| P2 | Admin | Categories fields and usage table | [docs/admin/categories.md](../admin/categories.md) | Table | Not started |
| P2 | Admin | Course Builder screenshot + panel explanation table | [docs/admin/course-builder.md](../admin/course-builder.md) | Screenshot/Table | Not started |
| P2 | Admin | Criteria Bank screenshot with linked-outcome indicators | [docs/admin/criteria-bank.md](../admin/criteria-bank.md) | Screenshot | Not started |
| P2 | Admin | Institutions list/form screenshot with required fields | [docs/admin/institutions.md](../admin/institutions.md) | Screenshot | Not started |
| P2 | Admin | Module Composer screenshot with metadata/outcomes/methods callouts | [docs/admin/module-composer.md](../admin/module-composer.md) | Screenshot | Not started |
| P2 | Admin | Outcomes list/form screenshot + key fields table | [docs/admin/outcomes.md](../admin/outcomes.md) | Screenshot/Table | Not started |
| P2 | Admin | Period hierarchy visual (parent-child nesting) | [docs/admin/periods.md](../admin/periods.md) | Diagram | Not started |
| P2 | Admin | Quizzes list/editor screenshot + lifecycle table | [docs/admin/quizzes.md](../admin/quizzes.md) | Screenshot/Table | Not started |
| P2 | Admin | Themes list/form screenshot with module mapping examples | [docs/admin/themes.md](../admin/themes.md) | Screenshot | Not started |

## Execution notes

- Keep visuals consistent in size and style per persona section.
- Prefer real UI screenshots over mockups.
- Add captions that explain what action the user should take next.
- Re-run `mkdocs build` after each batch of 3-5 visual insertions.


**Last updated:** 2026-07-08

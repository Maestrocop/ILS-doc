# Workflows

This page describes the actual work flows implemented in the current ILS application and how teacher actions move data through the system.

## Workflow summary

| Workflow | Main pages | Key backend paths | Purpose |
|---|---|---|---|
| Submission lifecycle | `GradingPage2.jsx` | `/api/grading/*` | Capture student submission scoring and create outcome snapshots |
| Heatmap flow | `HeatmapPage.jsx` | `/api/heatmap/*` | Visualize class mastery by outcome and support drilldown evidence |
| Cockpit flow | `ClassroomIntelligencePage.jsx`, `StudentCockpitPage.jsx` | `/api/cockpit/summary` | Surface class health and at-risk students for teacher action |
| Grading Cockpit | `GradingPage2.jsx` | `/api/grading/*` | Score submissions and update student mastery snapshots |
| Module authoring | `ModuleForm.jsx`, `ModuleEditor.jsx` | `/api/modules` | Create and update modules with linked outcomes, themes, and teaching methods |
| Assignment authoring | `AssignmentForm.jsx` | `/api/assignments` | Create assignments and attach rubrics for grading |
| Rubric authoring | `RubricsPage.jsx`, `RubricEditor.jsx` | `/api/rubrics` | Define reusable rubrics, criteria, and ratings |

## Submission lifecycle

The submission lifecycle is the path from student work to teacher decision and class-level reporting.

1. A student submits work for an assignment in a class.
2. The submission is stored in `submissions`.
3. A teacher opens the grading cockpit and scores rubric criteria.
4. The system writes or updates `submission_criterion_scores`.
5. The grading endpoint computes totals and updates `submissions.overall_score`.
6. When grading is finalized, the system writes outcome snapshots to `student_outcome_snapshots`.

## Grading flow

The grading workflow is implemented in `backend/routes/grading.js`.

### Key grading endpoints

- `GET /api/grading/classes` — lists classes with course/module context and assessment mode
- `GET /api/grading/classes/:classId/assignments` — lists assignments in a class, rubric links, and grading counts
- `GET /api/grading/assignments/:assignmentId/classes/:classId/students` — loads students and submission status for one assignment
- `GET /api/grading/submissions/:submissionId` — loads one submission with rubric criteria, ratings, and linked outcomes
- `POST /api/grading/submissions/:submissionId/score` — saves selected ratings and optionally finalizes grading

### Scoring and finalization

The grading endpoint performs these actions:

- upsert one `submission_criterion_scores` row per scored criterion
- compute the submission total score from criterion scores
- determine `grade_status` and update the submission record
- in the same transaction, write outcome snapshots when grading is final

The backend supports two assessment modes:

- `simple` — grading is finalized automatically on save
- `advanced` — the caller may save a draft and finalize separately

The frontend uses `assessment_mode` from `GET /api/grading/classes` and `GET /api/grading/submissions/:submissionId` to decide whether to show Save Draft and Finalize controls.

## Rubric lifecycle

Rubrics are created and edited through `backend/routes/rubrics.js`.

A rubric includes:

- a title and optional description
- a category from `rubric_categories`
- multiple criteria in `rubric_criteria`
- rating levels for each criterion in `rubric_ratings`
- optional linked outcomes via `linked_outcome_id` on each criterion

Creating or updating a rubric reconstructs the rubric criteria and ratings in the backend. The rubric editor can also attach outcomes to individual criteria.

## Heatmap flow

The heatmap is built from two sources:

- outcome definitions and their latest snapshot scores
- submission metadata for pending and graded work

`GET /api/heatmap/classes/:classId` returns:

- `outcomes` — outcome columns derived from rubric criteria used in class assignments
- `students` — enrolled students with current snapshot scores
- `summary` — graded/pending counts, average score, and at-risk totals

The heatmap query reads the most recent non-stale `student_outcome_snapshots` for each student/outcome/class.
This makes the heatmap consistent with the cockpit and avoids recomputing mastery from raw rubric data on every request.

### Drill-down flow

`GET /api/heatmap/classes/:classId/drilldown` returns assignment-level evidence for a selected student/outcome pair.
It shows assignment titles, criterion names, scored values, and max score.
This supports the UX of clicking a heatmap cell to inspect underlying evidence.

## Cockpit and intelligence flow

`GET /api/cockpit/summary` aggregates class-level and student-level health metrics.
It relies on:

- class reporting rules from `campus_reporting_rules`
- pending and overdue submission counts
- most recent outcome snapshots
- trend averages across snapshot history

The cockpit flow produces:

- `pulse` summary cards
- `classes` health rows with thresholds and counts
- `at_risk_students` prioritized students for teacher action

The student cockpit is not a separate database artifact; it is a view built from submissions and snapshot state.

Classroom Intelligence is related but distinct: it is a frontend report layer that consumes `/api/heatmap/classes/:classId` and computes interpretive cohort patterns in the browser.

## Frontend pages and UI workflows

The current frontend SPA is built in `ILS-dev/frontend` and is organized around teacher/admin workflow pages.
It uses a shared API client to call backend endpoints and render the workflows below.

### Main workflow pages

- `ModulesPage.jsx` — module list and course-filtered module management
- `ModuleForm.jsx` / `ModuleEditor.jsx` — module creation/edit flow with outcomes, structures, teaching methods, and assessments
- `AssignmentsPage.jsx` — assignment list for admin and module management
- `AssignmentForm.jsx` — assignment builder with rubric selection and assignment metadata
- `OutcomesPage.jsx` — outcome bank management for learning outcomes
- `ThemesPage.jsx` / `ThemeForm.jsx` — theme bank management for cross-cutting learning themes
- `RubricsPage.jsx` / `RubricEditor.jsx` — rubric authoring, criteria, and rating management
- `SettingsPage.jsx` — global admin configuration and reference lookups
- `HeatmapPage.jsx` — classroom heatmap visualization and student mastery grid
- `StudentCockpitPage.jsx` — teacher action list for priority students and risk profiles
- `ClassroomIntelligencePage.jsx` — class health interpretation and suggested interventions
- `GradingPage2.jsx` — grading cockpit and rubric scoring workflow

### Admin section and route structure

The frontend routes are mounted under `/admin/*` for administrative views and under `/courses/:courseId/modules/:moduleId/assignments/*` for assignment authoring flows.
This separation keeps curriculum administration distinct from teacher intelligence pages.

### Data-fetching patterns

The frontend uses `fetchApi()` from `frontend/src/lib/api.js` to prefix requests with `/api` and to handle local development host resolution.
Key data-fetching patterns include:

- bank endpoints such as `/api/modules/bank/outcomes`, `/api/modules/bank/ref_teaching_methods`, and `/api/modules/bank/assignments`
  to populate dropdowns and autocomplete fields in editors
- list endpoints such as `/api/modules`, `/api/assignments`, `/api/outcomes`, `/api/themes`, and `/api/rubrics`
  to power data tables and admin grid pages
- detail endpoints such as `/api/modules/:id`, `/api/assignments/:id`, `/api/rubrics/:id`, and `/api/grading/submissions/:submissionId`
  to load edit forms and grading detail views

### Form and editor flows

- Module editors save a module using `PUT /api/modules/:id` and may include child arrays for structures, assessments, themes, and outcomes.
- Assignment editors create or update assignments via `POST /api/assignments` and `PUT /api/assignments/:id`, including selected `rubric_ids`.
- Rubric editors create hierarchical rubric content with `POST /api/rubrics` and update it with `PUT /api/rubrics/:id`.

These frontend workflows are the core user-visible flows that drive the backend API surface and ensure the admin UI matches the live implementation.

## Core workflows

The core workflows are the foundation of the live ILS implementation. They focus on creating and updating curriculum, assignments, grading evidence, and reporting data.

### Module authoring and update workflow

Modules are created and updated through the frontend module editor and the backend module endpoints.

- `POST /api/modules` creates a minimal module record. Required fields are `title` and `course_id`.
- `PUT /api/modules/:id` updates module metadata and related child collections in a single transaction.
- The payload may include:
  - module identity fields: `title`, `code`, `duration`, `level`, `weight`, `course_id`
  - linked outcome IDs via `outcome_ids`
  - module structure rows via `structures`
  - teaching methods via `teaching_method_ids`
  - assessment records via `assessments` or `assessment_ids`
  - theme links via `theme_ids`

This workflow keeps module identity and linked intelligence data synchronized and avoids orphaned module children.

### Assignment creation and grading workflow

Assignments belong to modules and are created or updated through admin assignment forms.

- `POST /api/assignments` creates a new assignment and requires `module_id`.
- `PUT /api/assignments/:id` updates assignment fields and optional `rubric_ids`.
- Assignments can be linked to one or more rubrics through `assignment_rubrics`.

The grading workflow then scores submission evidence against linked rubric criteria:

- Students submit work against an assignment in a class.
- The grading cockpit loads submissions and rubric criteria via `/api/grading` endpoints.
- `POST /api/grading/submissions/:submissionId/score` saves `submission_criterion_scores`, computes totals, and may finalize grading.

### Linking themes, outcomes, and rubrics

The app separates ownership from learning intelligence by using explicit association tables.

- Modules link to outcomes through `module_learning_outcomes`.
- Modules link to themes through `module_themes`.
- Assignments link to rubrics through `assignment_rubrics`.
- Rubric criteria link to outcomes with `linked_outcome_id`.

These workflows support cross-course intelligence and keep horizontal metadata reusable.

### Bank and lookup workflows

Frontend editors load reference data from bank endpoints to keep forms responsive and avoid unnecessary full list queries.

| Endpoint | Purpose | Used by |
|---|---|---|
| `/api/modules/bank/outcomes` | Outcome lookup list for module and assignment editors | ModuleForm, AssignmentForm |
| `/api/modules/bank/ref_teaching_methods` | Teaching method reference data | ModuleForm, ModuleEditor |
| `/api/modules/bank/assignments` | Assignment lookup data | ModuleEditor, admin assignment flows |
| `/api/assessment-types` | Assessment type metadata | module and assignment forms |
| `/api/frameworks` | Outcome framework metadata | outcome/editor and report configuration |
| `/api/themes` | Theme lookup data | module/theme editors |
| `/api/outcomes` | Outcome lookup data | module/outcome editors |

### Data integrity and compatibility workflows

The system guards important workflows with explicit validation and compatibility handling:

- Required fields like `title`, `course_id`, and `module_id` are enforced at the API layer.
- The frontend may pass both legacy and current payload shapes for compatibility.
- Updates are executed transactionally where possible to keep related child records consistent.
- Soft deletes and `deleted_at` filtering keep queries safe and avoid exposing removed records.

## Module and curriculum editing

The module editor uses `PUT /api/modules/:id` to update module core details and child collections.
It updates:

- module metadata such as title, code, duration, level, and weight
- linked outcomes via `outcome_ids`
- module structures via `structures`
- teaching methods via `teaching_method_ids`
- assessments via `assessments` or `assessment_ids`
- theme links via `theme_ids`

The update is executed in a transaction to keep module children consistent.

## Why these workflows matter

- They move the app from raw student submissions to outcome mastery and class intelligence.
- They preserve a clean separation between rubric scoring and outcome snapshot reporting.
- They let teachers use the grading cockpit, heatmap, and classroom intelligence pages without the backend recomputing scores on every read.


**Last updated:** 2026-07-08

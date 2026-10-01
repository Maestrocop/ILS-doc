# Data Model

This page documents the actual data entities and relationships used by the ILS application.
It is based on the live backend models and the route behavior found in `ILS-dev/backend`.

## Core vertical entities

The structural curriculum hierarchy is the foundation of the app.

| Entity | Purpose | Description |
|---|---|---|
| `institutions` | Top-level organization | Root of the vertical hierarchy |
| `campuses` | Physical campus | Location under an institution |
| `courses` | Course offering | Program of study owned by a campus or institution |
| `modules` | Curriculum unit | Subject-level unit contained inside courses |
| `assignments` | Work item | Assessment or task attached to a module |
| `module_items` | Module composition | Ordered content (assignments + quizzes) within a module |
| `classes` | Student group | Enrollment context for students and modules |
| `users` | People | Teachers, students, and administrative staff |
| `submissions` | Student work | Work submitted for an assignment in a class |

### Class enrollment types

Classes are the delivery context for students and modules, and the system supports a flexible hybrid enrollment model.

- A student can have zero or one `primary` class enrollment (main cohort/home group) and multiple `keuzedeel` or `minor` enrollments (electives, specialisations, or optional subject sections).
- The backend uses a partial unique index so a student cannot have two `primary` enrollments, but it does not require a primary enrollment.
- This supports Dutch vocational models with a primary cohort plus elective keuzedelen, K-12 models with a home class plus subject groups, and US-style schools where all enrollments are treated as `keuzedeel`.
- Primary class grouping is often the default scope for cockpit and heatmap reports, while elective teachers may see only their own class roster.
- Outcome snapshots and intelligence reports aggregate across all of a student’s active class enrollments.

### Module as hub

A module is the central structural entity in the current application.
Assignments belong to modules, and classes link students to modules through enrollment.
The frontend uses module and course metadata in the course bank, module editor, assignment builder, and grading pages.

### Module aggregates

Modules aggregate multiple related structures and intelligence links:

- `structures` — ordered week/topic/activity rows tied to a module
- `items` — ordered content composition (assignments and quizzes) within a module via `module_items`
- `assessments` — linked module assessment records that describe assessment plans or instruments
- `teaching_methods` — module teaching methods and pedagogical metadata
- `themes` — linked learning themes via `module_themes`
- `outcomes` — linked learning outcomes via `module_learning_outcomes`

## Intelligence entities

The horizontal intelligence layer is built from reusable learning artifacts:

- `themes` — broad, cross-cutting learning themes
- `outcomes` — measurable learning goals tied to mastery tracking
- `outcome_categories` — outcome groupings for reporting and filtering
- `frameworks` — optional frameworks that group outcomes and support curriculum structure
- `rubrics` — grading instruments used to evaluate submissions
- `rubric_categories` — rubric metadata categories
- `rubric_criteria` — criteria within a rubric
- `rubric_ratings` — rating levels available for each criterion
- `student_outcome_snapshots` — the canonical mastery snapshot table used by heatmap and cockpit reports
- `assessment_types` — assessment type metadata used by module and assignment forms
- `module_learning_outcomes` — links between modules and outcomes
- `module_themes` — links between modules and themes
- `assignment_rubrics` — assignment-to-rubric links

## Mapping tables and decoupling

The application keeps the intelligence layer decoupled from ownership using join tables and reference relationships:

- `module_learning_outcomes` attaches outcomes to modules without giving outcomes ownership fields like `module_id`
- `module_themes` attaches themes to modules without nesting the theme entity
- `assignment_rubrics` attaches grading rubrics to assignments without duplicating rubric metadata
- `rubric_criteria.linked_outcome_id` maps a criterion to a single outcome for evidence-based mastery tracking
- `student_outcome_snapshots` links submission grading to student/outcome/class mastery state
- `student_outcome_snapshots` can be tagged by evidence source, such as assignment vs quiz question

## Declarative vs derived outcome mapping

The current ILS data model distinguishes between two different kinds of outcome relationships:

- **Derived outcome evidence** — the operational grading path. Rubric criteria link to outcomes via `rubric_criteria.linked_outcome_id`, and graded submissions generate `student_outcome_snapshots` used by reports, heatmaps, and cockpit dashboards.
- **Declared outcome intent** — a planning layer that describes the outcomes a project is intended to develop. This is not currently implemented in the schema, so the system does not yet support a separate `project_outcomes` junction table or explicit project-level declared outcome list.

Because the current implementation only stores DERIVED outcome evidence, curriculum coverage questions such as “which outcomes does this project intend to cover?” must be answered by drilling into assignments → rubrics → criteria. A future enhancement could add a declarative layer for curriculum mapping and coverage warnings without changing the grading pipeline.

## Key mapping relationships

The application keeps the intelligence layer decoupled from ownership using join tables.
These mappings are the real integration points between curriculum and mastery data.

| Mapping table | Connects | Purpose |
|---|---|---|
| `module_items` | Modules → Assignments/Quizzes | Ordered composition of content within a module |
| `module_learning_outcomes` | Modules → Outcomes | Link modules to their learning goals |
| `module_themes` | Modules → Themes | Tag modules with broad learning themes |
| `assignment_rubrics` | Assignments → Rubrics | Link grading instruments to assignments |
| `rubric_criteria.linked_outcome_id` | Rubric criteria → Outcome | Tie each rubric criterion to one outcome |
| `student_outcome_snapshots` | Submission → Outcome mastery | Store the computed mastery score for reporting |

## Submission and grading data

The grading workflow stores both raw submission data and rubric-derived evidence.

- `submissions` represent a student’s attempt for an assignment in a class
- `submission_criterion_scores` store the selected rating, score, and notes for each rubric criterion
- `student_outcome_snapshots` preserve computed mastery scores for a student/outcome/class combination
- `assignment_rubrics` links assignments to rubrics used for grading

This allows the system to separate:

- raw rubric scoring by criterion
- derived outcome mastery state used by reports

## Core lookup tables

Certain tables provide lookup metadata that the frontend fetches for editors and forms:

- `assessment_types` — available assessment types used by module and assignment forms
- `frameworks` — outcome grouping frameworks for curriculum planning
- `rubric_categories` — organizational categories for rubrics

## Model associations

The main model associations found in `backend/models/index.js` are:

- `Course.hasMany(Module)`
- `Module.belongsTo(Course)`
- `Module.hasMany(Assignment)`
- `Assignment.belongsTo(Module)`
- `Module.belongsToMany(Theme)` via `ModuleTheme`
- `Theme.belongsToMany(Module)` via `ModuleTheme`
- `Module.belongsToMany(Outcome)` via `ModuleLearningOutcome`
- `Outcome.belongsToMany(Module)` via `ModuleLearningOutcome`
- `Rubric.belongsToMany(Assignment)` via `AssignmentRubric`
- `Assignment.belongsToMany(Rubric)` via `AssignmentRubric`
- `Rubric.hasMany(RubricCriterion)`
- `RubricCriterion.belongsTo(Rubric)`
- `RubricCriterion.hasMany(RubricRating)`
- `RubricRating.belongsTo(RubricCriterion)`
- `RubricCriterion.belongsTo(Outcome)` via `linked_outcome_id`
- `User.hasMany(Submission)`
- `Submission.belongsTo(User)`
- `Assignment.hasMany(Submission)`
- `Submission.belongsTo(Assignment)`
- `Class.hasMany(Submission)`
- `Submission.belongsTo(Class)`
- `StudentOutcomeSnapshot.belongsTo(Outcome)`
- `StudentOutcomeSnapshot.belongsTo(Class)`
- `StudentOutcomeSnapshot.belongsTo(User)`
- `StudentOutcomeSnapshot.belongsTo(Submission)`
- `Module.hasMany(ModuleStructureRow)`
- `ModuleStructureRow.belongsTo(Module)`
- `Module.hasMany(ModuleAssessment)`
- `ModuleAssessment.belongsTo(Module)`
- `Module.hasMany(ModuleLearningOutcome)`
- `ModuleLearningOutcome.belongsTo(Module)`
- `Module.hasMany(ModuleTheme)`
- `ModuleTheme.belongsTo(Module)`

## Model conventions

Key conventions used in the backend model definitions:

- Models use `underscored: true` so database columns are snake_case while model property names can remain JavaScript-friendly.
- Soft deletes are implemented via `deleted_at` and `paranoid: true` on models.
- All models include timestamp fields `created_at` and `updated_at`.
- Primary keys are `BIGINT` identity columns.
- Relationships are expressed with explicit aliases to make query results readable, such as `structures`, `assessments`, and `outcomes` on `Module`.

## Relationship summary

| Entity A | Entity B | Relationship | Why it matters |
|---|---|---|---|
| `courses` | `modules` | One-to-many | Modules are the units of curriculum inside a course |
| `modules` | `assignments` | One-to-many | Assignments belong to a single module |
| `classes` | `assignments` | Many-to-many via module enrollment | Classes are the delivery context for assignment submissions |
| `assignments` | `rubrics` | Many-to-many via `assignment_rubrics` | Assignments can use one or more rubrics for grading |
| `rubrics` | `rubric_criteria` | One-to-many | Rubric criteria define individual scoring dimensions |
| `rubric_criteria` | `rubric_ratings` | One-to-many | Ratings define selectable score levels for a criterion |
| `rubric_criteria` | `outcomes` | Many-to-one | Each criterion may map to one outcome |
| `modules` | `themes` | Many-to-many via `module_themes` | Themes tag modules with broad learning focus areas |
| `modules` | `outcomes` | Many-to-many via `module_learning_outcomes` | Modules group outcomes for planning and reporting |
| `submissions` | `submission_criterion_scores` | One-to-many | Each submission stores scores for rubric criteria |
| `student_outcome_snapshots` | `outcomes` | Many-to-one | Snapshots preserve outcome-level mastery state |
| `student_outcome_snapshots` | `users` | Many-to-one | Snapshots are tied to a student record |

## Snapshot table role

`student_outcome_snapshots` is the canonical reporting table for the current implementation.

- The heatmap reads the most recent non-stale snapshot per student/outcome/class.
- The cockpit reads snapshots for cohort mastery and trend aggregation.
- Snapshots are refreshed when grading is finalized.

## Note on missing artifacts

The current code does not expose a separate `learningEvidence` entity as a public model or API.
Do not document tables or objects unless they are present in `ILS-dev/backend/models` or referenced by the backend routes.


**Last updated:** 2026-07-08

# Admin Guide

This guide describes the administration and curriculum management workflows available in ILS.

## Admin Responsibilities

Administrators manage the complete curriculum lifecycle from setup to reporting.

## Core Admin Pages

The most important admin pages are:

- **Institutions** — manage organization-level records
- **Campuses** — manage campus locations and reporting rules
- **Courses** — create and maintain course offerings
- **Modules** — define curriculum units and link outcomes, themes, and teaching methods
- **Assignments** — create and manage assignments within modules
- **Curriculum Composer** — review and manage course-level curriculum content
- **Curriculum Composer V2** — build next-generation course blueprints with recursive period structures
- **My Work** — review and manage submission workflows
- **Course Builder** — review student-facing course content and structure
- **Module Composer** — compose and refine module-level curriculum content
- **Quizzes** — create and manage quiz-based assessments
- **Classes** — manage teaching classes and student enrollment contexts
- **Periods** — manage academic time frames
- **Themes** — maintain cross-cutting learning themes
- **Outcomes** — manage learning outcomes and their categories
- **Categories** — manage category labels used in outcomes and reports
- **Rubrics** — create and maintain grading rubrics
- **Criteria Bank** — review rubric criteria across all rubrics
- **Mapping Matrix** — inspect assignment-to-outcome coverage across the curriculum
- **Projects** — create and manage project-based assessments and artifacts
- **Audit Logs** — review system events and changes
- **Setup Health** — validate system readiness and configuration health
- **Teacher Dashboard** — review teacher metrics and roster summaries
- **Users** — manage application users and their roles
- **Academic Calendar** — manage institution-level holidays, exam windows, and semester markers

## Curriculum Management

The ILS curriculum model separates structural content from learning intelligence.
Admins build the curriculum in these layers:

- **Structural hierarchy** — institutions, campuses, courses, modules, assignments, classes
- **Intelligence layer** — themes, outcomes, rubrics, rubric criteria, ratings

This separation helps keep the underlying curriculum stable while reusing evaluation and reporting assets.

### Course and Module Administration

- **Courses** are the top-level named offerings
- **Modules** belong to courses and are the units of curriculum delivery
- **Assignments** belong to modules and are the work items students submit
- **Classes** bind students to a module and provide the grading context

### Module Editor

The module editor supports:

- Editing module metadata
- Linking outcomes to the module
- Attaching teaching methods
- Defining module structures
- Setting assessment rules and weights

### Assignment Editor

The assignment editor supports:

- Assignment metadata and due dates
- Assignment scoring settings
- Selecting linked rubrics
- Creating the assignment record for a module

## Rubric and Outcome Administration

Rubrics are the primary grading instruments in the system.
An admin can:

- Create a rubric with title, description, and category
- Add criteria to the rubric
- Define rating levels for each criterion
- Map individual criteria to outcomes
- Delete rubrics that are no longer needed

The Criteria Bank page is a read-only view that shows all criteria across all rubrics.
It is useful for:

- reviewing rubric coverage
- finding criteria that are already linked to outcomes
- checking consistency across rubrics

### Outcome management

Outcomes are the learning goals that drive mastery reporting.
Admins can:

- create and edit outcome metadata
- assign outcomes to categories
- define calculation methods and parameters for outcome scoring

The `module_learning_outcomes` mapping links outcomes to modules.
The `rubric_criteria.linked_outcome_id` field maps rubric criteria to outcomes for reporting.

## Reporting and intelligence administration

The admin pages also provide visibility into the reporting data used by teachers:

- **Mapping Matrix** shows which assignments assess which outcomes.
- **Heatmap** and **Classroom Intelligence** are teacher-facing reports that rely on rubric/outcome linkages.

The matrix view is particularly useful for ensuring that assignments and rubrics cover the desired outcomes.

## Calendar administration and scheduling

The calendar layer now includes role-specific views and academic scheduling operations.

- `/admin/calendar` — teacher calendar (cross-class deadlines and custom events)
- `/admin/classes/:classId/calendar` — class-level calendar for one class context
- `/admin/academic-calendar` — institution-wide academic event management (holidays, exam periods, semester start/end)

Academic calendar records are maintained independently from assignment and quiz authoring, while assignment/quiz dates still flow into calendar views through computed events.

## API and backend considerations

Admin operations are implemented through backend routes in `ILS-dev/backend/routes`.
Key backend endpoints include:

- `/api/courses`
- `/api/modules`
- `/api/assignments`
- `/api/themes`
- `/api/outcomes`
- `/api/rubrics`
- `/api/matrix`

Some administrative operations are also available under `/api/admin/*` for migration and metadata utilities.

## Practical admin workflow

1. Create or verify course and module records.
2. Define module outcomes and teaching methods.
3. Build rubrics and link criteria to outcomes.
4. Create assignments and attach rubrics.
5. Create classes for teaching delivery and enroll students.
6. Monitor coverage in the Mapping Matrix.
7. Use teacher reporting pages to verify that outcome mastery data is flowing correctly.

## What this guide does not cover

This guide is not a complete operations manual.
It is focused on the current admin features that exist in `ILS-dev` and the production data model.


**Last updated:** 2026-07-08

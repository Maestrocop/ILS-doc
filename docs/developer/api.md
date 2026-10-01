# API Reference

This page documents the current backend API surface of the ILS application.
It is based on the route mounting in `ILS-dev/backend/index.js` and the route handlers in `ILS-dev/backend/routes`.

## Mounted API groups

The backend mounts these top-level groups under `/api`.

| Route group | Purpose |
|---|---|
| `/api/health` | Service health check |
| `/api/auth` | Authentication endpoints |
| `/api/institutions`, `/api/campuses`, `/api/courses` | Curriculum and organization management |
| `/api/modules`, `/api/assignments` | Module and assignment authoring |
| `/api/modules/:id/items`, `/api/library` | Module composition and content library services |
| `/api/themes`, `/api/outcomes`, `/api/outcome-categories`, `/api/frameworks` | Learning intelligence metadata |
| `/api/rubrics`, `/api/rubrics/categories`, `/api/rubrics/criteria` | Rubric authoring and criteria management |
| `/api/assessment-types`, `/api/reference`, `/api/matrix`, `/api/periods` | Lookup and reference data |
| `/api/grading`, `/api/heatmap`, `/api/cockpit` | Scoring, mastery reporting, and classroom analytics |
| `/api/classes`, `/api/users` | Class delivery, students, and enrollment context |
| `/api/student`, `/api/curriculum`, `/api/quizzes` | Student experience, curriculum composer, and quiz workflows |
| `/api/projects`, `/api/period-templates` | Project workflows and reusable period template operations |
| `/api/events`, `/api/academic-calendar` | Unified calendar feeds, custom events, and academic calendar management |
| `/api/submissions`, `/api/ai` | Submission file handling and AI-assisted quiz generation |
| `/api/admin/*` | Maintenance and administrative utilities |

## High-value workflows

The core app workflows are driven by these endpoints:

| Route | Method | Purpose |
| --- | --- | --- |
| `/api/grading/classes` | `GET` | Class picker for grading cockpit |
| `/api/grading/classes/:classId/assignments` | `GET` | Assignment list with rubric and grading counts |
| `/api/grading/assignments/:assignmentId/classes/:classId/students` | `GET` | Student submission list for one assignment |
| `/api/grading/classes/:classId/submissions` | `GET` | Class submissions grouped by assignment |
| `/api/grading/submissions/:submissionId` | `GET` | Grading cockpit detail for one submission |
| `/api/grading/submissions/:submissionId/score` | `POST` | Save rubric scores and finalize grading |
| `/api/grading/submissions/:submissionId/return` | `PATCH` | Return an assignment submission to the student |
| `/api/grading/quiz-submissions/:submissionId/return` | `PATCH` | Return a quiz submission to the student |
| `/api/grading/quiz-submissions/:submissionId/reset` | `PATCH` | Reset a quiz submission grade |
| `/api/cockpit/summary` | `GET` | Classroom risk and health summary |
| `/api/heatmap/classes/:classId` | `GET` | Heatmap grid for a class |
| `/api/heatmap/classes/:classId/drilldown` | `GET` | Assignment-level evidence for a heatmap cell |
| `/api/events` | `GET` | Unified calendar feed for assignment/quiz due dates, custom events, and academic events |
| `/api/academic-calendar` | `GET` | Institution academic-calendar events expanded for calendar rendering |

## Grading API

### `GET /api/grading/classes`

Returns the grading cockpit class picker with module and course metadata.
The response includes `assessment_mode` for each class.

### `GET /api/grading/classes/:classId/assignments`

Returns assignments in a class with linked rubric metadata and graded/ungraded counts.

### `GET /api/grading/assignments/:assignmentId/classes/:classId/students`

Returns students and submission status for a specific assignment and class.
The response includes scored criteria counts and total rubric criteria counts.

### `GET /api/grading/classes/:classId/submissions`

Returns all submissions for a class grouped by assignment.
The response includes `overall_score`, submission status, and rubric coverage indicators.

### `GET /api/grading/submissions/:submissionId`

Loads full grading detail for one submission.
The response includes:

- submission metadata
- student context
- assignment context
- rubric criteria
- linked outcome metadata
- rating options for each criterion
- `assessment_mode`

### `POST /api/grading/submissions/:submissionId/score`

Saves selected rubric scores for a submission.

Request payload:

- `scores` — array of objects with `criterion_id`, `rating_id`, `score`, and optional `grader_notes`
- `grader_notes` — optional overall notes for the submission
- `finalize` — boolean to request finalization of grading

Behavior:

- inserts or updates `submission_criterion_scores`
- computes the submission total score
- updates `submissions.overall_score` and `submissions.grade_status`
- optionally finalizes grading and writes outcome snapshots

### `PATCH /api/grading/submissions/:submissionId/return`

Returns an assignment submission to the student for revision.
This is only enabled when the student still has remaining retry attempts.

### `PATCH /api/grading/quiz-submissions/:submissionId/return`

Returns a quiz submission to the student for revision while preserving the quiz attempt count semantics.

### `PATCH /api/grading/quiz-submissions/:submissionId/reset`

Resets a quiz submission grade to allow a fresh grading workflow or retry evaluation.

## Cockpit API

### `GET /api/cockpit/summary`

Supported query parameters:

- `campusId` — optional campus filter
- `periodId` — optional academic period filter
- `classIds` — optional comma-separated list of class IDs

Returns:

- `pulse` — top-level counts for at-risk, inactive, pending, and flagged classes
- `classes` — per-class health rows with thresholds and rule metadata
- `at_risk_students` — prioritized student list for teacher action

This endpoint reads mastery state from `student_outcome_snapshots` and computes pending/overdue workload using class enrollments and submission status. It is the main backend data source for the Teacher Student Cockpit.

## Heatmap API

### `GET /api/heatmap/classes/:classId`

Supported query parameters:

- `moduleId` — optional filter to outcomes linked by assignments in a module
- `includeTrends=true` — optional trend enrichment

Returns:

- `outcomes` — outcome columns used by the class
- `students` — students with current mastery scores and pending submission markers
- `summary` — graded and pending counts, average score, and at-risk totals

This endpoint is the main backend data source for the Classroom Intelligence frontend page.
Classroom Intelligence uses the returned `outcomes`, `students`, and `summary` payload to derive cohort patterns, teaching insights, and suggested interventions.

### `GET /api/heatmap/classes/:classId/drilldown`

Required query parameters:

- `outcomeId`
- `userId`

Optional query parameter:

- `moduleId`

Returns rows of assignment and criterion-level evidence for the selected student and outcome.

## Course and module APIs

### `GET /api/courses`

Returns all courses.

### `POST /api/courses`

Creates a course record.
Supported fields include:

- `title`
- `description`
- `code`
- `short_code`
- `duration`
- `level`
- `total_credits`
- `status`
- `enrollment_type`
- `primary_color`
- `default_teaching_method_id`
- `default_assessment_type_id`

### `GET /api/modules`

Returns modules with aggregated outcome and theme counts.

### `GET /api/modules/bank/outcomes`

Returns a lightweight outcomes bank for module and assignment editors.

### `GET /api/modules/bank/ref_teaching_methods`

Returns reference teaching methods used by the module editor.

### `GET /api/modules/bank/assignments`

Returns a bank of assignments for module-related editor screens.

### `POST /api/modules`

Creates a minimal module record.
Required fields:

- `title`
- `course_id`

Optional fields include:

- `code`
- `duration`
- `level`
- `weight`

### `PUT /api/modules/:id`

Updates module metadata and child collections.
Supported payload fields include:

- `title`, `code`, `duration`, `level`, `weight`, `course_id`
- `outcome_ids`
- `structures`
- `teaching_method_ids`
- `assessments`
- `assessment_ids`
- `theme_ids`

Updates are performed transactionally in `backend/routes/module.js`.

### `GET /api/modules/:id/items`

Returns ordered module content items used by module composition pages.
The response includes mixed content types such as assignments and quizzes.

### `POST /api/modules/:id/items`

Adds a content item to a module.
The payload includes `content_type` and `content_id`.

### `PATCH /api/modules/:id/items/reorder`

Updates content ordering for module items in bulk.

### `PATCH /api/modules/:id/items/:itemId`

Updates module-item lock settings for sequence prerequisites.

Supported payload fields:

- `locked_by_previous` — boolean
- `unlock_on` — one of `submit`, `grade`, `pass`

This endpoint is used by Module Composer to define prerequisite progression between adjacent items in a module sequence.

### `DELETE /api/modules/:id/items/:itemId`

Removes an item from a module.

### `GET /api/assignments`

Returns all assignments with module context for admin views.

### `POST /api/assignments`

Creates a new assignment.
Required field:

- `module_id`

Optional fields include:

- `title`
- `description`
- `points_possible`
- `due_date`
- `available_from`
- `available_until`
- `weight`
- `status`
- `display_grade_as`
- `submission_type`
- `rubric_ids`

### `GET /api/assignments/:id`

Returns a single assignment with linked rubrics.

### `PUT /api/assignments/:id`

Updates assignment fields and optional `rubric_ids`.

## Quiz APIs

The quiz route group supports authoring, item management, student attempts, and results.

- `GET /api/quizzes`
- `POST /api/quizzes`
- `GET /api/quizzes/:id`
- `PUT /api/quizzes/:id`
- `DELETE /api/quizzes/:id`
- `POST /api/quizzes/:id/items`
- `PUT /api/quizzes/:id/items/:itemId`
- `DELETE /api/quizzes/:id/items/:itemId`
- `PATCH /api/quizzes/:id/items/reorder`
- `POST /api/quizzes/:id/start`
- `POST /api/quizzes/:id/submit`
- `GET /api/quizzes/:id/results`
- `GET /api/quizzes/:id/my-result`

## Calendar APIs

The calendar layer is currently exposed via two route groups: `/api/events` and `/api/academic-calendar`.

### `GET /api/events`

Required query parameters:

- `from` (`YYYY-MM-DD`)
- `to` (`YYYY-MM-DD`)

Optional scope filters:

- `classId`
- `studentId`
- `teacherId`

Returns a unified event list combining:

- computed assignment due events (`assignment_due`)
- computed assignment opening events (`assignment_open`)
- computed quiz and exam due events (`quiz_due`, `exam`)
- custom events from `calendar_events` (including recurring expansion)
- academic calendar events from `academic_calendar_events` (expanded to per-day entries)

Event objects include core fields such as:

- `id`, `type`, `title`
- `date`, `starts_at`, `ends_at`, `all_day`
- `entity_type`, `entity_id`
- `class_id`, `class_name`

### `POST /api/events`

Creates a custom event.

Body fields:

- `title` (required)
- `starts_at` (required)
- `event_type` (optional, default `custom`)
- `description`, `location`
- `frequency`, `frequency_until`
- `ends_at`, `all_day`
- `class_id`, `course_id`

### `PATCH /api/events/:id`

Updates a custom event (partial update for editable fields such as title, dates, type, class link, recurrence, and description).

### `DELETE /api/events/:id`

Soft-deletes a custom event.

### `GET /api/academic-calendar`

Required query parameters:

- `from` (`YYYY-MM-DD`)
- `to` (`YYYY-MM-DD`)

Optional query parameter:

- `institutionId`

Returns institution-wide academic events (for example holidays and exam periods) expanded to one event row per day within the requested range.

### `POST /api/academic-calendar`

Creates an academic calendar event.

Body fields:

- `title` (required)
- `starts_on` (required)
- `event_type` (optional, validated set)
- `description`, `ends_on`
- `institution_id`, `academic_year`

### `PATCH /api/academic-calendar/:id`

Updates academic event metadata and dates.

### `DELETE /api/academic-calendar/:id`

--

## Detailed examples: Calendar & Module Items

These examples are extracted from the running backend route handlers in ILS-dev and show the concrete field names and typical shapes returned by the database queries.

### Example: `GET /api/events?from=2026-05-01&to=2026-05-31`

Response (array of event objects):

```json
[{
  "id": "assignment-due-123",
  "type": "assignment_due",
  "title": "Essay: Climate Change",
  "date": "2026-05-12",
  "starts_at": "2026-05-12T00:00:00",
  "ends_at": "2026-05-12T00:00:00",
  "all_day": true,
  "entity_type": "assignment",
  "entity_id": 123,
  "class_id": 45,
  "class_name": "Enviro 101"
},
{
  "id": "custom-77-2026-05-05",
  "type": "holiday",
  "title": "Mid-term Holiday",
  "date": "2026-05-05",
  "starts_at": "2026-05-05T00:00:00",
  "ends_at": "2026-05-05T23:59:59",
  "all_day": true,
  "entity_type": "calendar_event",
  "entity_id": 77,
  "class_id": null,
  "class_name": null,
  "description": "Campus closed",
  "frequency": "does_not_repeat"
},
{
  "id": "academic-3-2026-05-01",
  "type": "academic_holiday",
  "title": "Semester Break",
  "date": "2026-05-01",
  "starts_at": "2026-05-01",
  "ends_at": "2026-05-07",
  "all_day": true,
  "entity_type": "academic_calendar",
  "entity_id": 3,
  "description": "Semester break",
  "institution_name": "Springfield University",
  "academic_year": "2025-2026"
}]
```

Notes:
- The `GET /api/events` handler composes computed events (assignment due/open, quiz/exam due), expands recurring `calendar_events` via the `frequency`/`frequency_until` fields, and expands multi-day `academic_calendar_events` into one row per date.
- Query parameters `from` and `to` are required. Use `classId`, `studentId`, or `teacherId` to scope results.

### Example: `POST /api/events` (create custom event)

Request body:

```json
{
  "event_type": "custom",
  "title": "Study Group",
  "description": "Room 101",
  "starts_at": "2026-05-20T18:00:00",
  "ends_at": "2026-05-20T19:30:00",
  "all_day": false,
  "class_id": 45
}
```

Response: the inserted `calendar_events` row is returned (all columns present).

### Example: `GET /api/academic-calendar?from=2026-05-01&to=2026-05-31`

Response (expanded per-day academic events):

```json
[{ "id": "academic-3-2026-05-01", "type": "academic_holiday", "title": "Semester Break", "date": "2026-05-01", "starts_at": "2026-05-01", "ends_at": "2026-05-07", "all_day": true, "entity_type": "academic_calendar", "entity_id": 3, "description": "Semester break", "institution_name": "Springfield University", "academic_year": "2025-2026" }]
```

Validation:
- `POST /api/academic-calendar` validates `event_type` against a server list: `['holiday','exam_period','semester_start','semester_end','break','registration']`.

### Example: `GET /api/modules/:id/items` (module composition)

Response (ordered array):

```json
[{ "id": 501, "module_id": 34, "content_type": "assignment", "content_id": 123, "position": 10, "title": "Essay: Climate Change", "status": "published", "due_date": "2026-05-12", "points_possible": "100", "rubric_total_points": "40", "locked_by_previous": true, "unlock_on": "grade" },
{ "id": 502, "module_id": 34, "content_type": "quiz", "content_id": 88, "position": 20, "title": "Quiz 1", "status": "published", "due_date": "2026-05-05", "quiz_type": "formative", "item_count": "10", "locked_by_previous": false, "unlock_on": null }]
```

Supported module-item mutations:
- `POST /api/modules/:id/items` — add an item. Body: `{ content_type: 'assignment'|'quiz'|'project', content_id: number }`. Returns `201` with created row or `409` if already exists.
- `PATCH /api/modules/:id/items/reorder` — body: `{ items: [{ id, position }, ...] }` to atomically update positions.
- `PATCH /api/modules/:id/items/:itemId` — body may include `locked_by_previous` (boolean) and `unlock_on` (`submit`|`grade`|`pass`). Invalid `unlock_on` values return `400`.
- `DELETE /api/modules/:id/items/:itemId` — deletes the module_item row.

Implementation notes:
- The module-items queries coalesce related assignment/quiz metadata (title, due_date, points) into the response for easier UI rendering.
- `position` uses spaced increments (e.g., +10) and `POST` computes new position as `max_pos + 10`.


Soft-deletes an academic calendar event.

## Curriculum composer APIs

The curriculum route group supports period trees, course structure slots, module library selection, and class-to-course mappings.

- `GET /api/curriculum/courses/:courseId/structure`
- `GET /api/curriculum/modules/library`
- `POST /api/curriculum/courses/:courseId/periods`
- `PATCH /api/curriculum/periods/:periodId`
- `DELETE /api/curriculum/periods/:periodId`
- `PATCH /api/curriculum/courses/:courseId/periods/reorder`
- `POST /api/curriculum/courses/:courseId/structure`
- `PATCH /api/curriculum/structure/:id`
- `PATCH /api/curriculum/courses/:courseId/structure/reorder`
- `DELETE /api/curriculum/structure/:id`
- `POST /api/curriculum/modules/:moduleId/fork`
- `PATCH /api/curriculum/modules/:moduleId/library`
- `GET /api/curriculum/courses/:courseId/classes`
- `GET /api/curriculum/classes/available`
- `POST /api/curriculum/courses/:courseId/classes/:classId`
- `DELETE /api/curriculum/courses/:courseId/classes/:classId`

### Period templates

- `GET /api/period-templates` — list saved period templates with item counts
- `GET /api/period-templates/:id` — fetch one template with its full period tree
- `POST /api/period-templates` — create a new period template
- `PUT /api/period-templates/:id` — update an existing template and replace its items
- `DELETE /api/period-templates/:id` — remove a template
- `POST /api/period-templates/:id/apply` — apply a template to a course’s academic periods

## Student APIs

The student route group powers student-facing pages for work lists, curriculum, assignment details, submissions, and dashboard summaries.

- `GET /api/student/my-work`
- `GET /api/student/courses`
- `GET /api/student/courses/:courseId/curriculum`
- `GET /api/student/courses/:courseId/enrolled-modules`
- `GET /api/student/course-structure`
- `GET /api/student/assignments/:assignmentId`
- `POST /api/student/submissions`
- `PATCH /api/student/submissions/:id/submit`
- `GET /api/student/dashboard`

## AI quiz generation API

### `POST /api/ai/quiz/generate`

Generates quiz-question candidates from selected outcomes.
This endpoint returns quiz-item-compatible objects for quiz authoring flows.

## Class and user APIs

### `GET /api/classes`

Returns classes with module and assignment context for the admin view.

### `GET /api/classes/:id`

Returns detailed metadata for one class, including module, course, campus, and period context.

### `GET /api/classes/my`

Returns classes assigned to the current teacher (requires `teacher` role).

### `GET /api/classes/:id/students`

Returns students enrolled in a class along with enrollment status, cohort, and last submission timestamp.

### `GET /api/classes/:id/modules`

Returns modules assigned to a class, including assigned module teachers.

### `GET /api/classes/:id/projects`

Returns projects assigned to a class, including project status and due/available dates.

### `GET /api/classes/health`

Returns readiness and health metrics for all classes, or only the current teacher's classes when `mine=true`.

### `GET /api/users`

Returns users, including students and teachers.

## Rubric APIs

### `GET /api/rubrics`

Returns a list of rubrics with category metadata, criteria counts, and total points.

### `GET /api/rubrics/:id`

Returns a full rubric with criteria, ratings, and linked outcomes.

### `POST /api/rubrics`

Creates a rubric and nested criteria and ratings.

### `PUT /api/rubrics/:id`

Updates rubric metadata and replaces criteria and ratings when provided.

### `DELETE /api/rubrics/:id`

Deletes a rubric and its child criteria and ratings.

### `GET /api/rubrics/categories`

Returns rubric categories.

### `GET /api/rubrics/criteria`

Returns the full rubric criteria bank across all rubrics, including linked outcome metadata.

## Reference APIs

The backend also exposes support and lookup endpoints for curriculum setup:

- `/api/themes`
- `/api/outcomes`
- `/api/outcome-categories`
- `/api/frameworks`
- `/api/reference`

For calendar UI configuration, reference endpoints include:

- `GET /api/reference/event-types`
- `POST /api/reference/event-types`
- `PUT /api/reference/event-types/:id`
- `DELETE /api/reference/event-types/:id`

`GET /api/reference/event-types` supports optional query parameter `category` (`individual` or `academic`) for filtered event-type lists.
- `/api/assessment-types`
- `/api/periods`
- `/api/matrix`

`/api/matrix` returns curriculum mapping data used by the admin matrix page.

## Library APIs

The library route group provides content discovery and metadata for authoring workflows.

### `GET /api/library/usage`

Returns usage statistics for content items (assignments and quizzes) across modules.

Returns a JSON object mapping content identifiers to their usage information:

```json
{
  "assignment:12": {
    "usage_count": 3,
    "course_titles": ["Mathematics 101", "STEM 201"]
  },
  "quiz:45": {
    "usage_count": 1,
    "course_titles": ["Physics 110"]
  }
}
```

Use this endpoint to show authors how many modules use each piece of content.

### `GET /api/library/disciplines`

Returns a sorted list of distinct discipline values from assignments and quizzes.

This endpoint supports content filtering and categorization in library browsing interfaces.

## Admin maintenance APIs

Maintenance routes under `/api/admin` include:

- `/api/admin/seed-assessment-descriptions`
- `/api/admin/describe-module-teaching-methods`
- `/api/admin/describe-outcomes`
- `/api/admin/migrate-outcomes`

These administrative utility endpoints support schema inspection, seed data population, and migration support.
They are not part of the main teacher or admin workflows.


**Last updated:** 2026-07-08

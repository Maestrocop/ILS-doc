# Curriculum Composer

The Curriculum Composer is an admin page for managing course-level curriculum content.
It is implemented in `ILS-dev/frontend/src/pages/CurriculumComposerPage.jsx` and mounted at `/admin/curriculum`.
A newer version of the same workflow is available at `/admin/curriculum-v2` for the next-generation course blueprint editor.

<!-- TODO: Add a screenshot sequence for period tree editing, drag/drop ordering, and module slot placement. -->

## Admin UI

- Legacy curriculum route: `/admin/curriculum`
- Next-gen curriculum route: `/admin/curriculum-v2`
- Course-specific curriculum route: `/admin/curriculum/:courseId`

## Purpose

This page provides a workspace for composing curriculum content and reviewing course structure.
It is intended for admin users who need to manage course-level curriculum content outside the core course and module editors.

## Blueprint vs class confirmation

The Curriculum Composer is primarily a course blueprint tool. It defines what should be taught in a course: the planned modules, periods, and nested delivery structure.

These periods are course-specific and intentionally do not include real dates. They capture the structure of the curriculum — for example, Semester 1 contains three blocks or weeks — but not the institution’s official academic calendar.

A related teacher-facing workflow exists at the class level. Once a course blueprint is ready, a teacher can confirm it for a specific class by assigning actual teachers to each module and locking it into the class plan. This is not duplicate work — it is the moment the blueprint becomes a concrete class delivery plan.

The teacher-facing class setup workflow typically uses a blueprint panel that shows modules suggested by the Curriculum Composer. A manual module dropdown is a fallback for older classes without a blueprint or when a teacher needs an extra module that was not included in the course plan.

When a blueprint exists and is complete, the expected flow is:

1. Use `+ Add all` to bring the course blueprint into the class.
2. Assign a teacher to each module.
3. Review the resulting class plan and schedule.

The manual module dropdown should only be needed when the blueprint is missing, incomplete, or intentionally extended.

## Page behavior

The page supports:

- selecting a course or opening a course-specific curriculum workspace
- viewing curriculum content in a course context
- navigating between course-level curriculum items
- managing semester and period organization for course delivery

## Period hierarchy

The composer now supports a recursive academic period tree with unlimited nesting depth.
Any period can become a container by adding sub-periods, and each nested level adjusts its visual style automatically.

- Container periods render as `SemesterSection` at any depth.
- Leaf periods render as `PeriodSection` when they have no child periods.
- Containers can also hold direct module slots, shown at the top of the section.

The frontend helpers now support recursive nesting:

- `flattenPeriodSlots(periods)` recursively flattens slots at any depth
- `slotsByPeriod` recursively searches nested period trees
- `findSlotById` recursively finds a slot by ID
- `collapseAllPeriods` collects all collapsed IDs recursively
- `renamePeriod` updates nested periods optimistically in-place

In the UI:

- `SemesterSection` is collapsible and draggable
- depth styling changes with nesting (lighter backgrounds and borders at deeper levels)
- any leaf period can sprout sub-periods using `+ Add Sub-period`
- modules can be dropped directly onto any container period

The workflow is:

1. Create a regular period first (for example, `Semester 1`).
2. Inside that period, use `+ Add Sub-period` to convert it into a container period on the next load.
3. Drag nested sub-period cards to reorder them within their parent.
- Use indent/outdent controls to change a period's parent without losing its children.
- Drop modules directly on a container period or on child period cards.

This UI makes container periods act as grouping headers and nested periods as draggable cards that may themselves contain further sub-periods or direct modules.

### Period Templates

The system now supports reusable period templates to quickly populate course period structures.

- Templates are managed from the `Period Templates` tab on `/admin/periods`.
- Each template contains a nested period tree with names, parent/child structure, and display order.
- Templates can be created, renamed, reordered, duplicated, and deleted from the template editor.
- In Curriculum Composer V2, Step 2 includes an `Apply template` dropdown that copies the template into the course’s academic periods instantly.
- `Apply template` preserves existing course periods, so it is safe for incremental editing.
- `Replace` mode is also supported in the implementation, but it is only allowed when the course has no active periods that already contain assigned modules. When replace is used, the current course periods are soft-deleted before the template is re-applied.
- Applied templates are one-time copies. Template updates do not automatically sync to course period trees that have already been customized.

This feature is intended for program-level reuse:

- save standard year, semester, quarter, or block structures once
- apply the same structure to multiple courses
- adjust the result per course without rebuilding the whole tree

The template workflow is especially useful for multi-year programs and courses that share the same academic rhythm but differ in specific module assignments.

## Backend contract

The page likely relies on course and curriculum APIs such as:

- `GET /api/courses`
- `GET /api/courses/:id`
- `GET /api/curriculum/:courseId`

## Admin workflow

1. Open `/admin/curriculum`.
2. Select a course to review or edit curriculum content.
3. Use the course-specific route if available to load a particular course workspace.

## Notes

- This route is part of the current live admin routing configuration.
- It is separate from the core course and module editors and is intended for course-level curriculum composition.


**Last updated:** 2026-07-08

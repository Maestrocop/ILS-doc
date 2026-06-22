# Calendar (Phase 5) — Epic #122

Status: Implemented in current ILS-dev routes/pages (ongoing hardening)

## Purpose

Provide a time-based events layer that surfaces assignment, quiz, class, and academic-calendar events in role-specific calendar views.

## Who should use it

- Teachers: see upcoming due dates, filter by class, and identify scheduling conflicts.
- Students: view their personal timeline of due dates and class events.
- Administrators / Schedulers: overview of module-level timelines and cross-course events.
- Instructional coaches: identify pacing issues and clustered deadlines.

## How it works (overview)

The calendar shows assignment, quiz, class, and academic-calendar events in role-specific views based on what you need to see.

## Step-by-step (teacher)

1. Open the Calendar from your admin tools
2. Use the calendar to review assignment and quiz due dates
3. Add optional custom events (personal or class-linked) directly in the calendar UI
4. Use the class-specific calendar when scheduling within a single class

## Step-by-step (student)

1. Open your personal calendar
2. Review due dates and class events across your courses
3. Click any event to see details or navigate to the related assignment or quiz

## Expected outcomes & examples

The calendar maps source objects to event types and renders a unified timeline. Example:

| Source type | Source field | Event `type` | Example title | Visible in |
|-------------|--------------|--------------|---------------|------------|
| Assignment | due date | assignment due | Essay 1 | teacher/student/class |
| Assignment | available date | assignment open | Essay 1 (opens) | teacher/student/class |
| Quiz | due date | quiz due | Quiz 3 | teacher/student/class |
| Custom event | user-created | custom event | Parent meeting | teacher/class/personal |
| Academic event | institution-wide | academic event | Semester Start | institution-wide views |

Notes: events with missing source dates are not emitted by computed queries.

## UI labels & navigation

- Teacher calendar: accessible from admin tools
- Class calendar: accessible from class management
- Academic calendar: managed by coordinators/admins
- Student calendar: accessible from student dashboard

Event actions:
- Click assignment/quiz events to open the related item
- Use the calendar interface to manage custom and academic events

## Prerequisites

- Assignment and quiz dates must be populated in the system
- You must be authenticated to create, update, or delete events
- Student calendars show only events for classes they're enrolled in
- Teacher calendars show events for classes they teach

## Troubleshooting / common gotchas

- "Event not appearing": check the source item's `due_date` is set and saved.
- "Missing custom event": verify class/user filter scope (teacher/student/class) in the current calendar view.
- "Recurring event count looks wrong": confirm recurrence `frequency` and `frequency_until` values.
- Missing permissions: student calendars are enrollment-scoped; teacher calendars are class-assignment-scoped.

## Implementation notes (docs-only)

This page describes the Phase 5 calendar feature roadmap and current status as of June 2026.

---

_Last updated: Phase 5 implementation audit (Epic #122)_

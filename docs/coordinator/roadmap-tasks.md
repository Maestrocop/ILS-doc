# Coordinator Roadmap Tasks (living checklist)

This file is a living checklist of documentation-ready tasks derived from the Coordinator Weekly Workflow. These are documentation and product-focussed tasks — not code changes — to be used as a shared specification and acceptance checklist.

Each task includes: Owner, Priority, Effort, Acceptance criteria, Notes, Status.

---

## 1. Sessions Delivered vs Planned metric
- Owner: Product / Analytics (docs)
- Priority: High
- Est. effort: Medium
- Acceptance criteria:
  - Documentation describes required data sources: scheduled sessions, session 'held' events, cancellations.
  - Defines computed fields: planned_sessions, delivered_sessions, percent_delivered.
  - Example query and expected output shown.
  - UI acceptance: coordinator dashboard shows percent_delivered; modules with <80% flagged.
- Notes: map to existing timetable and session logs.
- Status: Todo

---

## 2. Intervention / Contact Note (spec)
- Owner: Product / UX (docs)
- Priority: High
- Est. effort: Medium
- Acceptance criteria:
  - Document data model fields: author, linked_student_id, linked_teacher_id, module_id, note_text, timestamp, visibility, tags.
  - Document permissions: who can create, edit, view, delete; retention rules for GDPR.
  - Include UI wireframe notes: create note flow, attach to student/teacher/module, list and filter notes.
  - Include example API payloads for create/read (documentation only).
- Notes: must include audit logging and retention policy.
- Status: Todo

---

## 6. Reminder engine & manual trigger (docs + spec)
- Owner: Product / Ops (docs)
- Priority: High
- Est. effort: Small → Medium (docs first)
- Acceptance criteria:
  - Document reminder thresholds and tone (`reminder-rules.md`).
  - Document escalation matrix (`escalation-matrix.md`).
  - Provide a manual trigger spec for admins to run the reminder job for testing.
  - Define `reminder_log` fields and acceptance criteria for one-shot reminders and escalation flags.
- Notes: start with manual endpoint; scheduler later.
- Status: Todo

---

## 3. Class-level Module Performance Report
- Owner: Product / Reporting (docs)
- Priority: Medium
- Est. effort: Medium
- Acceptance criteria:
  - Document report columns: module_id, cohort, average_grade, median_grade, submission_rate, sample_size.
  - Provide filter and export requirements (date range, cohort, module).
  - UI wireframe notes for coordinator view and drill-down to student list.
- Notes: clarify grade scale and handling of drafts.
- Status: Todo

---

## 4. Grading Backlog Widget (coordinator dashboard)
- Owner: Product / UX (docs)
- Priority: High
- Est. effort: Small
- Acceptance criteria:
  - Define what constitutes backlog (ungraded submissions older than X days).
  - Define widget data points: teacher, class, count, oldest ungraded date, link to teacher grading backlog.
  - Document expected interactions (filter by teacher, escalate action).
- Notes: reuse existing Teacher Grading Backlog data where possible.
- Status: Todo

---

## 5. Educational Quality Tracker
- Owner: Product / Curriculum (docs)
- Priority: Medium
- Est. effort: Medium
- Acceptance criteria:
  - Document signals captured (student survey flags, repeated low outcomes, cohort failure rates).
  - Define workflow for creating quality issues, assigning reviewers, and tracking remediation.
  - Provide sample reporting dashboard layout for quality metrics.
- Notes: this is a long-term feature; include initial MVP signals only.
- Status: Todo

---

## How to use this file
- Update `Status` as you progress.
- Expand any task into a dedicated spec file (link to `coordinator/` folder).
- Keep acceptance criteria concise and testable.

---

**Last updated:** 2026-07-06

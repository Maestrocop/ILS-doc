# Intervention / Contact Note — Spec

Purpose: define the data model, permissions, UI flows, and acceptance criteria for the Intervention / Contact Note feature (documentation-only spec).

## Overview

Coordinators, advisors, and authorised staff can log short intervention notes linked to students, teachers, modules, or classes. Notes serve as a durable record of contact and actions taken.

## Data model (docs)

- `id` (string)
- `author_id` (string) — staff user who created the note
- `author_role` (string) — e.g., Coordinator, Advisor
- `linked_student_id` (string, nullable)
- `linked_teacher_id` (string, nullable)
- `module_id` (string, nullable)
- `class_id` (string, nullable)
- `note_text` (text)
- `tags` (array of strings)
- `visibility` (enum: `private`, `staff`, `public`)
- `created_at` (timestamp)
- `updated_at` (timestamp)

## Permissions (docs)

- Who can create: Coordinators, Advisors, assigned Staff
- Who can view: Coordinators and the student's assigned advisors; teachers may see notes linked to their classes unless marked `private`.
- Who can edit/delete: author and site admins. Deletion must be auditable; prefer soft-delete.

## UI flows (docs)

1. Create note: coordinator opens student or module, clicks **Add intervention note**, fills `note_text`, selects links (student/teacher/module), sets visibility, saves.
2. List & filter: coordinator sees a paged list of notes with filters (student, teacher, module, tag, date range).
3. View: open a note to see full text, author, and audit trail.

## Audit & Retention (docs)

- All notes must be immutably logged in an audit table: who changed what and when.
- Retention: follow school's GDPR policy; document retention period (e.g., 7 years) and deletion workflow.

## Acceptance criteria

- Coordinator can create a note linked to a student and module and see it in the student's timeline.
- Notes appear in coordinator lists and are searchable by tag and text.
- Visibility rules enforced: `private` notes are not visible to teachers.
- Audit trail records create/edit/delete events.

## Example payloads (docs-only)

Create note payload (example):

```json
{
  "author_id": "staff_123",
  "linked_student_id": "student_456",
  "module_id": "module_789",
  "note_text": "Contacted student about missing assignments; arranged advisor meeting.",
  "tags": ["attendance","follow-up"],
  "visibility": "staff"
}
```

---

**Last updated:** 2026-07-06

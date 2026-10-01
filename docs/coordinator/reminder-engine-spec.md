# Reminder Engine — Manual Trigger Spec

Purpose: documentation-first spec for the manual reminder trigger and the `reminder_log` tracking model. This is a product/UI spec — no code changes are performed here.

## Overview

Start with a manual admin endpoint to run reminder logic for testing and validation. The endpoint will:

- Run all configured reminder rules (grading, attendance, BSA) against current data.
- Create `reminder_log` entries for each reminder sent.
- Return a summary payload of reminders generated (per teacher / per item).

## Manual trigger endpoint (docs)

- Method: `GET`
- Path: `/api/admin/jobs/run-reminders` (docs only)
- Permissions: admin only
- Behaviour: runs reminder rules once and returns a JSON summary. No scheduler invoked.

Example response (docs-only):

```json
{
  "run_at": "2026-07-07T10:00:00Z",
  "reminders": [
    {
      "teacher_id": "staff_123",
      "teacher_email": "peter@example.com",
      "items": [
        { "item_id": "sub_456", "type": "grading", "age_days": 27 }
      ]
    }
  ]
}
```

## `reminder_log` (docs)

Documented fields for tracking reminders and supporting escalation logic.

- `id` (string)
- `item_id` (string) — id of the object reminded about (submission id, attendance record id)
- `item_type` (enum: `grading`, `attendance`, `bsa`)
- `recipient_id` (string) — user id who was reminded (teacher / advisor)
- `channel` (enum: `in_app`, `email`)
- `reminder_stage` (integer) — e.g., 1 for first reminder, 2 for escalation
- `sent_at` (timestamp)
- `status` (enum: `sent`, `failed`)
- `actor` (string) — system or admin who triggered

## Rules to implement (docs)

- Grading: create in-app reminder at 14 days, escalate to email+coordinator at 21 days.
- Attendance: in-app reminder for patterns; escalate per escalation matrix.
- BSA: follow BSA rules in `escalation-matrix.md`.

## Acceptance criteria (docs)

- Admin can trigger `/api/admin/jobs/run-reminders` and receive a summary of reminders.
- `reminder_log` contains one entry per reminder sent; entries include stage and channel.
- Manual run does not schedule repeated sends; each item is considered per its age and previous reminders.

## Testing & Validation (docs)

- Provide a test dataset (documented) for QA: sample ungraded submissions of various ages.
- Document expected output for the test dataset.

---

**Last updated:** 2026-07-07

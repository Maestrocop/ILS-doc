# Escalation Matrix

Purpose: a single escalation matrix that applies consistently across grading, attendance, and BSA signals.

## Global escalation rules (recommended)

Columns: Signal | Stage | Condition | Action | Visibility

- Grading | Stage 1 | 14 days ungraded | In-app reminder to teacher (one-shot) | Teacher only
- Grading | Stage 2 | 21 days ungraded | Email to teacher; mark escalated to coordinator | Coordinator + Teacher
- Attendance | Stage 1 | 3 days attendance unmarked | In-app reminder to teacher | Teacher only
- Attendance | Stage 2 | Pattern of missed sessions | In-app reminder + coordinator flag | Coordinator + Teacher
- BSA | Stage 1 | At-risk detected | Advisor notified | Advisor + Coordinator

## Tracking

- `reminder_log` (documentation): each entry records item_id, reminder_stage, sent_at, channel, actor.
- Escalation flag: computed field `escalation_status` visible on Programme Health.

## Usage notes

- Start with manual triggers and observe noise rates before enabling automated daily jobs in production.
- Keep rules conservative to avoid over-notifying teachers.

**Last updated:** 2026-07-06

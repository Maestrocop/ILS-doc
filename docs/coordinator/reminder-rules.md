# Reminder Rules & Notification Philosophy

Purpose: document the recommended, documentation-first approach for reminders and escalation in ILS. This is a product and UX decision record — no code changes are included here.

## Principles

- Dashboard-first: the teacher dashboard is the primary source of truth.
- Email is escalation, not routine notification.
- Minimal, rare, and humane: avoid repeated nags; prefer single, actionable nudges.
- Student-first language: mention the student and context, not blame.

## Recommended thresholds (starter configuration)

### Grading
- 0–13 days: dashboard only (no reminders)
- 14 days: in-app reminder (one per item) — no repeat for same item
- 21 days: email to teacher + mark as escalated to coordinator

### Attendance
- Single missed session: dashboard only
- Multiple missed sessions or pattern (e.g., >3 days or 3 consecutive misses): in-app reminder
- Repeated pattern after reminder: escalate to coordinator and consider email

## Reminder behaviour

- One-shot: a single in-app reminder per item at the configured threshold.
- Escalation counter: track reminders sent per item to support escalation rules (e.g., 1 reminder → coordinator after X days).
- Manual trigger: allow admin to run the reminder logic manually for testing (no scheduler yet).

## Tone & content guidelines

- Subject line (email): "A student is still waiting for feedback"
- Body example:

  Hi Peter,

  Lotte de Vries has been waiting 27 days for feedback on "Praktijkopdracht — Onderzoekend Vermogen".

  Grade → [link]

  Please review and provide feedback. Thank you.

- Use student-first phrasing; avoid accusatory language.

## Operational notes

- Prefer an intervention log as priority: reminders without follow-up tracking are less useful.
- Start with a manual endpoint to validate tone and logic before enabling scheduled jobs in production.

**Last updated:** 2026-07-06

# Session Feedback — RFC / Specification (documentation only)

Purpose: specify a minimal, implementation-agnostic design for Session Feedback to include in product documentation and engineering discussions. This is docs-only; no changes will be made to `ILS-dev`.

## Goals

- Capture short, high-response student feedback tied to a specific session.
- Surface immediate signals to teachers and coordinators (small-N flags).
- Persist responses for analytics and longitudinal reporting.

## Key UX flows

1. Teacher triggers feedback for a session (button `Request Feedback` on session card).
2. Students receive a short prompt (in-app + optional email/SMS) and submit responses.
3. Aggregated results appear on session summary and in Intelligence Hub.

## Minimal survey (recommended)

1. Clarity: 1–5
2. Engagement: 1–5
3. Free-text: "What remains unclear?" (optional)

Keep total questions ≤ 3 to maximize response rate.

---

## Data model (docs-only)

- session_feedback
  - id: bigint PK
  - session_id: bigint FK -> sessions
  - student_id: bigint FK -> users
  - clarity_score: smallint
  - engagement_score: smallint
  - comments: text
  - created_at: timestamptz

- session_feedback_summary (materialized view / denormalized)
  - session_id
  - avg_clarity
  - avg_engagement
  - response_count
  - latest_comments (sample)

Notes: store scores as integers; keep comments nullable.

---

## Minimal API surface (docs-only)

- POST `/api/feedback/session/:sessionId/request`
  - Auth: teacher or admin
  - Action: mark session.feedback_requested = true; enqueue notifications; return 202

- POST `/api/feedback/session/:sessionId/response`
  - Body: `{ student_id, clarity_score, engagement_score, comments? }`
  - Auth: student (or system via secure token)
  - Action: insert `session_feedback` row; update summary

- GET `/api/feedback/session/:sessionId/summary`
  - Returns aggregated metrics and sample comments

Security: ensure only enrolled students can submit for the session.

---

## Analytics & Intelligence

- Real-time small-N flags: if response_count < 10 but avg_clarity <= 2, surface a coordinator alert.
- Trends: module-level aggregations across sessions and academic periods.
- CSV export for manual review.

---

## Suggested admin pages (docs-only)

- Session Feedback Dashboard: list recent sessions with avg scores, filter by class/module/teacher.
- Module Feedback Report: aggregate session feedback per module across a period.

---

## Migration notes (docs-only)

- New table `session_feedback` can be added via migrations; backfill is optional.
- Backfilling: if historical session-level feedback doesn't exist, start collecting going forward.

---

If you'd like, I will add example JSON payloads for the APIs and a sample migration SQL template in the docs. I will not modify `ILS-dev`.


**Last updated:** 2026-07-08

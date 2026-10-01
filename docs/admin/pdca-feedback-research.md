# PDCA Cycle & Feedback — Feedback & Research domain (proposal)

This page introduces the PDCA (Plan-Do-Check-Act) cycle and a proposed `Feedback & Research` domain for ILS. It's a product and documentation proposal only — `ILS-dev` will not be modified.

## Why PDCA for ILS?

PDCA (Plan → Do → Check → Act) gives a simple, repeatable continuous-improvement loop. For an education platform it maps naturally to curriculum design, teaching, feedback collection and curriculum updates.

High-level mapping:

- Plan: Curriculum Composer — design modules, blocks, learning outcomes
- Do: Teaching — classes, timetables, sessions
- Check: Session Feedback + Surveys — collect student & teacher evidence
- Act: Curriculum updates, rubric changes, remediation interventions

---

## Proposed product split

Split feedback into two related products:

1) Session Feedback (High priority)

- Trigger: a teacher or system action on a timetable session (e.g. teacher clicks `Request Feedback` on a session card).
- Student prompt (example):

  - How clear was today's lesson? (1–5)
  - How engaged were you? (1–5)
  - What remains unclear? (free text)

- Data flow: Session → Student Feedback → Teaching Quality Analytics → Intelligence Hub
- Usage: immediate teaching improvements, teacher coaching, small-N alerts in Intelligence Hub

2) Institutional Surveys (Lower priority / later)

- Module evaluation, Course evaluation, Wellbeing, Graduate survey, Teacher satisfaction
- Larger sample sizes, scheduled distribution, longer lifecycle, research-grade analysis

---

## Feedback & Research domain (recommended directory)

Create a future domain: `Feedback & Research` containing:

- Session Feedback (event-driven)
- Module Evaluations
- Course Evaluations
- Institutional Surveys
- Question Bank (reusable items)
- Survey Analytics & Reports

This domain should be logically separate from curriculum and timetable but integrate with them.

---

## PDCA in practice (example flow)

1. Plan: Designer defines Module A and expected outcomes in Curriculum Composer.
2. Do: Teacher delivers Session S for Module A (timetable session generated from schedule rules).
3. Check: Teacher requests session feedback; students respond; analytics surface low clarity or engagement scores.
4. Act: Designer updates Module A (re-sequencing, rubrics), or Teacher adjusts lesson plan; changes get re-deployed in Composer; PDCA repeats.

---

## Analytics & Intelligence

- Real-time indicators (small-N): per-session averages, teacher flags when < threshold
- Aggregated metrics: module-level satisfaction trends, course-level NPS-like scores
- Drilldown: filter by class, academic period, teacher, demographic segments

---

## UX suggestions (quick)

- Teacher flow: in session view, `Request Feedback` button that opens a lightweight modal for students to answer on mobile.
- Student flow: link in LMS or SMS/email with 1–3 taps to submit; keep it short to maximize response rate.
- Reporting: per-session dashboard card, weekly digest for coordinators, and signals in Intelligence Hub.

---

If you like, I'll add a short sample UI mockup and a one-page PDCA poster to include in onboarding docs. I will not change `ILS-dev` — only add documentation under `ILS-doc`.


**Last updated:** 2026-07-08

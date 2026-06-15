# Curriculum Effectiveness (CE01 / CE02 / CE03)

This page documents the existing Curriculum Effectiveness reports and the distinct questions they answer. It is a factual, read-only description of the three reports: CE01, CE02, and CE03. No changes are made to `ILS-dev`.

## Audience
This page is intended for:
- Curriculum designers
- Program managers
- Education managers
- Coordinators (in curriculum mode)

Not intended for: teachers, mentors/SLBs, or students (those users have Cockpit, Heatmap, Student Success, and BSA dashboards).

---

## CE01 — Module Pass Rates
Question answered: "Which modules have low pass rates?"

What exists:
- A module-level table showing module name, programme, enrolled student count, pass rate, and simple pass/at-risk/failing categories using the pass threshold (default 55%).
- Use case: curriculum teams inspect modules with low pass rates to ask curriculum questions (difficulty, prerequisites, assessment validity, materials, teacher effect).

Example (excerpt):
- Marketing & Strategie — pass 64.0%
- MOD - BIM Fundamentals & ISO 19650 — pass 42.6%

CE01 is an alarm: it highlights modules where students are not passing at expected rates.

---

## CE02 — Multi-Module Failure Summary (replaces previous student-centric view)
Question answered: "How large is the multi-module failure problem in the cohort?"

What to show (implemented here as documentation of the existing approach):
- A concise summary count of how many students are failing multiple modules, e.g.:
  - "9 students currently fail 3 or more modules."
  - "4 students fail 5 or more modules."
  - "2 students fail 7 or more modules."
- Short explanatory text: this aggregate signal may indicate curriculum overload, missing prerequisites, or cohort-wide learning difficulties. For student-level details, the Student Success Dashboard is the correct place.

Rationale: this view is curriculum-focused (cohort health) rather than student-focused; it measures problem size rather than listing individual students.

---

## CE03 — Failure Cascade Analysis
Question answered: "Which modules appear most often in multi-failure cases?"

What exists / should be presented:
- A ranked list/table of modules and how frequently they appear in the set of students failing N+ modules (the "appears in cases" metric). Example:
  - Marketing & Strategie — appears in 8 of 9 multi-fail cases (88.9%)
  - BIM Fundamentals — appears in 7 of 9 multi-fail cases (77.8%)
  - Ondernemen — appears in 6 of 9 (66.7%)
- Interpretation guidance: modules with high percentages are likely starting points in failure chains and therefore high-priority targets for curriculum investigation (prerequisites, sequencing, assessment design).

Why CE03 matters:
- CE01 finds weak modules (symptom detection).
- CE02 measures the impact (size of problem).
- CE03 begins to reveal root causes by identifying modules that commonly precede broader failure.

Examples of value:
- Two modules with identical pass rates can have very different curriculum importance when CE03 shows one appears disproportionately in multi-failure cases — that module is likely a bottleneck.
- A module with a poor pass rate but low CE03 presence may be a difficult but isolated course; it is less likely to be the systemic cause.

---

## Short guidance for use
- Keep CE01 as the module-level alarm.
- Replace the previous student-list CE02 with the aggregated "Multi-Module Failure Summary" counts.
- Expose CE03 as the curriculum lead: "Failure Cascade Analysis" to identify starting points for investigation.
- Always link CE02/CE03 to the Student Success Dashboard for student-level follow-up when needed.

This document records the intended report structure and existing signals. No code or data in `ILS-dev` is modified by this file.

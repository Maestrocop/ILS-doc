# Periods and Scheduling — Process for Admins, Designers, Teachers

This guide documents the correct step-by-step process and the three-layer defenses to prevent orphan/undated academic periods. This is read-only: no changes will be made to `ILS-dev`.

**Intent:** ensure `academic_periods` is the single source of truth and prevent Curriculum Composer or Timetable rules from referencing undated (orphan) periods.

---

## Quick summary (one-liner)

Always create dated periods in the Academic Calendar first; then build curriculum; then create timetable rules.

---

## Roles and responsibilities

- Admin: create academic years and dated periods on the Periods page; run health checks; fix existing orphaned periods.
- Designer (Curriculum Composer): assign modules to existing dated `academic_periods` only; do not create new period labels.
- Teacher: use timetables and session occurrences generated from dated periods; report missing sessions to Admin.

---

## Step-by-step process (for Admin)

1. Open Academic Calendar → create the academic year (e.g. 2025-2026) if missing.
2. Under that year, create child periods with concrete `start_date` and `end_date` (e.g. Semester 1 Sep 2025–Feb 2026).
3. Verify dates visually on the Periods page and confirm parent/child relationship.
4. Run the Setup Health check (see Health checks below) to find any undated periods and course_structure references.
5. If orphaned periods exist (undated): decide remediation strategy — either add dates and parent them to the correct year, or migrate referencing course_structure rows to the correct dated period IDs.

---

## Step-by-step process (for Curriculum Designer)

1. Before opening Curriculum Composer, confirm the target academic year and its dated periods exist on the Periods page.
2. In Curriculum Composer, use the period-picker dropdown and choose from the dated academic_periods only.
3. Do not create or type new period labels in the Composer; if the needed period is missing, stop and request Admin to create it.
4. Save the course structure and verify the course_structure rows reference the correct `academic_periods` IDs (Admin can verify with Health page if needed).

---

## Step-by-step process (for Teacher)

1. Use the class timetable and session list derived from schedule rules.
2. If expected sessions are not generated: notify Admin with the class id and a screenshot. Admin will run the Health check to confirm periods used by the course structure are dated.
3. For cancellations, makeups and one-off edits, prefer editing the session occurrence (not the curriculum) to avoid accidental structural changes.

---

## Three layers of defense (product + infra)

1. UI: make the wrong thing impossible

- Curriculum Composer period picker must only list `academic_periods` where `start_date IS NOT NULL`.
- No in-place “create period” option inside Composer. If missing, direct users to Periods page.
- Timetable rule modal and schedule matrix should filter out undated periods.

2. API: validate at the boundary

- All API endpoints that create or update `course_structure` or `timetable_schedule_rules` must validate the referenced `academic_periods` have non-null `start_date` and `end_date`.
- If validation fails, return `400 Bad Request` with message: "Period has no dates. Set dates in Academic Calendar first."

3. Health/Setup checks: surface and help remediate existing damage

- Admin Setup Health page should include checks:
  - `academic_periods` rows where `start_date IS NULL` → label `Undated period`
  - `course_structure` rows referencing undated periods → list modules and course ids
  - `timetable_schedule_rules` referencing undated periods → list rules generating 0 sessions
- Health page should offer remediation hints: add dates (if the period is legitimate), or migrate course_structure references to a correct dated period.

---

## Remediation options (how to fix existing orphan records)

Option A — Add dates and parent to correct year

1. If the orphan label (e.g. Period-1) was intended to be part of 2025-2026, add `start_date`/`end_date` and set parent to the 2025-2026 year.
2. Run health check and re-run timetable generation for the affected class.

Option B — Repoint course structure to existing dated periods

1. If the course actually uses Semester 1 + Semester 2, update the `course_structure` entries to reference the semester period IDs.
2. Verify by running timetable generation; sessions should appear for the date ranges.

Option C — Delete orphan periods (only if safe)

1. If an orphan period is unused except for a small number of mistaken course_structure rows, consider migrating those rows then deleting the orphan record.
2. Always backup DB and run migration scripts defensively.

---

## Policy (process rule to include in onboarding)

ALWAYS in this order:

1. Academic Calendar → create year + dated periods
2. Curriculum Composer → assign modules to those dated periods
3. Timetable → create rules referencing those dated periods

If Step 1 is skipped, Steps 2–3 must be blocked by UI/API validation.

---

## Suggested rollout order (practical roadmap)

1. Implement UI filter in Composer (prevent new orphans) — highest impact
2. Add API validation for course_structure and rules — defensive
3. Add Health checks and remediation UI — visibility and cleanups

---

## FAQ

Q: Who owns the decision to create Periods vs Semesters for a given program?

A: Academic Admin (Registrar/Program Lead). Designers must follow the academic calendar established by Admin.

Q: Can Curriculum Composer create periods if missing?

A: No. Composer must not create periods. It should only reference dated `academic_periods` — this prevents ghost periods.

---

If you want, I can also add a short checklist page for day-to-day Admin health checks and a sample SQL query to find orphan periods. I will not change `ILS-dev` — only write docs under `ILS-doc`.

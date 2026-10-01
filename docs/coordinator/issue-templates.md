# Coordinator Issue Templates

Copy these issue templates into your issue tracker when creating implementation work for coordinator roadmap tasks.

## Sessions delivered vs planned — Issue template

**Title:** Implement sessions-delivered-vs-planned metric

**Description:**

Goal: compute `planned_sessions`, `delivered_sessions`, and `percent_delivered` per module and expose on the Coordinator Programme Health page.

**Acceptance criteria:**
- Backend computes fields and stores or exposes via API.
- Coordinator UI shows percent_delivered per module and flags modules with <80%.
- Example API response included in spec.

**Notes:** Data sources: timetable events (planned), session held events (delivered), cancellations.

## Intervention note — Issue template

**Title:** Add Intervention / Contact Note model + UI

**Description:**

Goal: enable coordinators and advisors to create, view, and search intervention notes linked to students, teachers, and modules.

**Acceptance criteria:**
- Data model fields implemented as in spec.
- UI flows for create/list/view implemented.
- Permissions enforced and audit log in place.

## Class-level module performance report — Issue template

**Title:** Add class-level module performance report

**Description:**

Goal: provide average grade per module per cohort, filterable by date range and exportable as CSV.

**Acceptance criteria:**
- Report columns: module_id, cohort, average_grade, median_grade, submission_rate, sample_size.
- Accessible from Coordinator Programme Health with drill-down to student list.

---

Use these templates as starting points; adjust owners and estimates per your workflow.

**Last updated:** 2026-07-06

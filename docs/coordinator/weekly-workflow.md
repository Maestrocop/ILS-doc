# Coordinator Weekly Workflow

**Mission:** Ensure that teaching, learning, and curriculum delivery remain on track across the programme.

## Role Definition

The coordinator is responsible for the health of their programme — not for doing the work, but for ensuring the work is being done. They intervene when teachers, students, or the curriculum fall behind.

They operate at programme level, not class level. They do not grade, do not mark attendance, do not teach. They watch, detect, and act.

---

## Monday Morning — Weekly Review

### 1. Teaching Operations
*Attendance • Grading • Session delivery*

| Signal | Threshold | Action |
|---|---:|---|
| Attendance not marked for a session that happened | Any | Contact teacher — "Please mark attendance for [Class] on [Date]" |
| Grading backlog per teacher | > 14 days old | Contact teacher — escalate if no response in 48h |
| Sessions cancelled without notice | Any | Follow up with teacher |

**Decision:** For each overdue item — contact teacher or escalate to programme manager.

---

### 2. Student Progress Check
*BSA cases • Advisor coverage • Attendance trends*

| Signal | Threshold | Action |
|---|---:|---|
| Attendance rate dropping for a student | < 80% this period | Trigger advisor conversation |
| Student has missed 3+ consecutive sessions | Any | Flag for SLB advisor, create intervention note |
| Student has unsubmitted assignments past due | Any | Advisor contacts student |
| BSA at-risk students | Any in red zone | Schedule progression review |

**Decision:** For each at-risk student — assign to advisor, schedule review, or log intervention.

---

### 3. Curriculum Delivery Check
*Planned coverage • Actual coverage • Module pacing*

| Signal | Threshold | Action |
|---|---:|---|
| Sessions delivered vs planned for a module | < 80% of planned | Meet with teacher — is module on track? |
| Module falling behind schedule | Any | Discuss with academic owner — reschedule or compress |
| Class performance on a module significantly below average | Cohort avg < 5.5 | Review with module owner — curriculum or delivery issue? |

**Decision:** For each gap — meeting with teacher or curriculum review.

---

## End of Week — Programme Health
**Question:** What do I need to flag before next week?

- Any unresolved grading backlogs?
- Any students who missed the entire week?
- Any BSA cases that need a formal review scheduled?
- Any module significantly behind?

If yes → create a task, schedule a meeting, or escalate. If no → programme is healthy.

---

## Educational Quality (Fourth Check)

This check is about continuous improvement, not operations.

Examples:
- Students consistently rate Assignment X as unclear.
- Module X has a 40% failure rate across three cohorts.
- One learning outcome is never being achieved.
- Exit/Reflection forms indicate confusion around the same topic.

Action: log issues for curriculum review and schedule an educational-quality review meeting.

---

## What the Coordinator Does NOT Do

- Does not grade submissions
- Does not mark attendance
- Does not contact students directly about academic content (that is the teacher's job)
- Does not manage individual lesson plans
- Does not assign assignments
- Does not build the timetable (Admin responsibility)

These are teacher or admin responsibilities. The coordinator only intervenes when the teacher or system fails to act.

---

## Mapping to ILS — What Exists vs What Is Missing

Maintain this as a living architecture document: when a feature is implemented, update the status here.

| Workflow step | ILS feature | Status |
|---|---|---:|
| See grading backlog per teacher | Dashboard → Teacher Grading Backlog | ✅ Exists |
| See attendance not marked per class | Monitoring page → Class Attendance | ✅ Exists (Rate = —) |
| See at-risk students | BSA Dashboard | ✅ Exists |
| Schedule progression review | Progression Reviews | ✅ Exists |
| See student attendance trend | Student Attendance page | ✅ Exists |
| See sessions delivered vs planned | — | ❌ Missing |
| Log intervention / contact note | — | ❌ Missing |
| See class performance per module | — | ❌ Missing |

---

## Conclusion for the Monitoring Page

The monitoring page should be organised around the three checks above — Teaching Operations, Student Progress, Curriculum Delivery — plus Educational Quality.

Each section must answer: **"What do I do if this number is red?"**

If that answer is clear and actionable inside ILS, build the section. If the answer is "email the teacher outside the system," that section belongs on the dashboard as an alert, not on a dedicated reporting page.

---

## Suggested Tasks (Roadmap starter)

1. Implement "Sessions delivered vs planned" metric for modules (backend + UI heatmap).
2. Add an "Intervention / Contact Note" model and UI to log coordinator actions and link to students, teachers, and modules.
3. Add class-level module performance reports (average grade per module per cohort).
4. Surface grading backlog widget per teacher on the coordinator dashboard (drill-down to student list).
5. Add an Educational Quality tracker to capture qualitative signals (student survey items, exit reflections).

---

**Last updated:** 2026-07-06

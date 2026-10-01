# Classroom Intelligence

Classroom Intelligence is the interpretive report that follows the Heatmap.
It is implemented in `ILS-dev/frontend/src/pages/ClassroomIntelligencePage.jsx` and mounted at `/admin/classroom-intelligence`.

[Classroom Intelligence Screenshot: cohort health summary with pattern detection and interventions]

## What Classroom Intelligence does

The page turns the class mastery matrix into a teacher-ready summary.
It highlights:

- how many students have enough graded evidence
- how many are below the target threshold
- whether the class is ready for cohort-level recommendations
- whether the class shows technical or polarized performance patterns

## Backend and UI sources

Classroom Intelligence uses:
- `GET /grading/classes` — class list
- `GET /modules` — module list for the selected course
- `GET /classes/:classId` — class metadata
- `GET /campuses/:campusId/reporting-rules` — campus thresholds
- `GET /heatmap/classes/:classId?moduleId=...` — core classroom data

## Page controls

- **Class selector** — choose the class to analyze.
- **Module selector** — when available, filter the report to a specific module.
- **Explain Decisions** — toggle to reveal the rule evidence behind recommendations.

## Key report sections

### Section 0 — Outcome Breakdown (Weak Area Highlights)

When outcome score data exists, Classroom Intelligence now shows an outcome breakdown table before Cohort Health.
It is ordered worst-first (highest percent-below-threshold first) so teachers can identify weak areas quickly.

This section includes:

- outcome code and name
- class average per outcome
- percent of students below threshold
- a status badge (`Critical`, `Attention`, `Watch`, `On track`)

For urgent cases, alert cards are shown for the top outcomes with high below-threshold pressure.

### Section 1 — Cohort Health

This section shows:

- total students
- graded students
- students below the success threshold
- whether re-teach is recommended
- a confidence level based on graded coverage

### Re-teach decision: Required (exact meaning)

`Re-teach decision: Required` means the class has crossed the campus re-teach policy threshold, so the teacher should pause progression and re-teach the weak outcomes before moving on.


Decision logic used in practice:

- **success threshold:** minimum mastery target (example: `6.0`)
- **re-teach threshold:** maximum allowed share of students below target (example: `40%`)
- **actual below-threshold share:** computed from graded students only.

Formula:

Re-teach if (below_threshold_count / graded_students) * 100 >= reteach_threshold

Example (general):

- class: `15` students total
- graded students: `15` (all graded)
- below success threshold: `14`
- calculated: `(14/15)*100 = 93%` below threshold
- policy threshold: `40%`
- result: `93% >= 40%` → `Re-teach decision = Required`

Example (WILISE1A — SM-BASIS):

- Course: `SM-BASIS - Service Management Basis`
- Success threshold: `6.0`
- Re-teach threshold: `40%`
- Total students: `15`
- Graded students: `4`
- Below threshold: `1`
- Calculated below%: `(1/4)*100 = 25%`
- Result: `25% < 40%` → `Re-teach decision = Not required`

Notes:

- Only **graded students** are counted in the denominator. Ungraded students do not affect the below-threshold percentage.
- The report also surfaces per-outcome breakdowns (class averages and % below) to guide which outcomes to re-teach first even when a full-class re-teach is not triggered.

How to interpret severity in this case:

- this is a high-severity signal, not a borderline trigger
- weak-area cards showing outcomes with very low class averages (for example around `1.0/10`) indicate substantial cohort learning gaps

Teacher next steps (recommended):

1. Pause progression to new content for this outcome cluster.
2. Verify grading completeness (all expected submissions graded, no missing recent assessments).
3. Re-teach the weakest outcomes first (the top rows in Outcome Breakdown).
4. Run a short formative reassessment on the same outcomes.
5. Re-open Classroom Intelligence and Heatmap after reassessment to confirm the below-threshold share drops under policy level.

Possible root causes to check:

- content was not fully taught before assessment
- students attempted work but did not understand the targeted outcomes
- grading/data completeness issue (less likely when most of the class is already graded)

For a step-by-step operational checklist, see [Re-teach Decision Playbook](reteach-decision-playbook.md).

### Section 2 — Pattern Detection

The page looks for patterns such as:

- **Polarized cohort** — a large gap between stronger and weaker students.
- **Technical weakness cluster** — technical outcomes are lagging.
- **Active at-risk cluster** — students below threshold who are still submitting work.

These patterns help teachers choose the right response.

### Outcome Gaps (what this means)

Outcome Gaps are the outcomes where too many students are still below the class target threshold.
They help teachers see where the cohort is not meeting expected mastery yet.

Each Outcome Gap row represents one outcome and usually includes:

- class average for that outcome
- percent of students below threshold
- number of students below threshold

Use Outcome Gaps to prioritize reteach focus and intervention planning.
If an outcome has both a low class average and a high percent below threshold, it is a high-priority teaching gap.

### Section 3 — Teaching Insights

The report can generate narrative observations such as:

- which outcome categories are strongest or weakest
- whether the cohort is near the threshold
- whether the class is under pressure from borderline students

### Section 4 — Suggested Interventions

The page recommends actions such as:

- focused modelling workshops
- peer-supported group work
- formative reassessment
- maintaining current pacing when no active trigger exists

When Explain Decisions is enabled, the report also shows supporting evidence values and rule outputs.

## What the report is for

Use Classroom Intelligence after the Heatmap.
It is the best place to move from outcome patterns to instructional decisions.

- Open it when the Heatmap shows broad outcome gaps.
- Open it when the class is near a re-teach warning.
- Use it to confirm whether a recommended action is supported by enough evidence.

## How it fits with other teacher views

- **Student Cockpit** shows immediate student actions.
- **Heatmap** shows outcome mastery across the class.
- **Classroom Intelligence** interprets the class signal and recommends what to do.
- **Grading** creates the evidence behind the report.
- **Interventions** explains how to act on the recommendation.

## UI guidance: Summary cards (compact layout + tooltips)

Recommendation: use the compact card layout (Option B) with concise labels on the cards and explanatory tooltips for evidence and trends. This keeps the dashboard visually consistent while ensuring teachers can inspect the evidence quickly.

- Card rules:
	- Keep card body short (one-line facts). Example: `Graded` → `8 / 12 outcomes`; `Avg Score` → `8.0 ↓ Declining`.
	- Surface evidence/confidence via hover tooltips rather than verbose card text.
	- Add a short inline evidence line above the Outcome Breakdown: `Scores based on 8 graded assignments` so context is available without hover.

- Tooltip examples:
	- Graded tooltip: “Scores based on 8 graded assignments · 4 outcomes still unassessed.”
	- Avg Score tooltip: “Down 1.0 point from previous assessment snapshot.” (Clarify what “previous” means in campus settings.)

- Rationale:
	- Consistent card heights improve scanability and alignment with `Pending`/`Overdue` cards.
	- Tooltips provide depth without clutter; inline evidence above the outcome table places trust context where teachers need it most.

Note: This is documentation guidance only — do not modify `ILS-dev` code from the docs repository.

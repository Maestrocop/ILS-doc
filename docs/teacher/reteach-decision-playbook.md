# Re-teach Decision Playbook

This page explains how to act when Classroom Intelligence shows a re-teach decision.

## What "Re-teach decision: Required" means

A `Required` decision means your class crossed the campus policy limit for students below the success threshold.
You should pause progression for the affected outcomes and run a re-teach cycle.

## Decision rule

Use this rule:

- success threshold: the minimum target score (example: `6.0`)
- re-teach threshold: the maximum allowed share of students below target (example: `40%`)
- actual below-threshold share: students below target divided by graded students

Formula:

- `below_percent = (students_below / graded_students) * 100`
- if `below_percent > re-teach_threshold`, then decision is `Required`

## Worked example

Given:

- graded students: `15`
- students below threshold: `14`
- re-teach threshold: `40%`

Calculation:

- `below_percent = (14 / 15) * 100 = 93.3%`

Interpretation:

- `93.3% > 40%` so the decision is `Required`

## Severity interpretation

When the below-threshold percentage is very high (for example above 80%) and outcome averages are very low, treat this as a high-severity cohort issue.

This usually indicates one or more of the following:

- outcomes were assessed before adequate instruction
- students attempted work but did not yet master the outcomes
- grading completeness or setup issue (less likely when most students are already graded)

## Immediate teacher action plan

1. Pause progression for the weak outcome cluster.
2. Confirm grading completeness for the class and selected module.
3. Prioritize the worst outcomes first (top rows in Outcome Breakdown).
4. Deliver focused re-teach activities on those outcomes.
5. Run a short formative reassessment.
6. Re-check Heatmap and Classroom Intelligence before advancing.

## Minimum evidence check before acting

Confirm all three checks:

- graded coverage is broad enough for the class
- major submissions for this unit are already graded
- outcome links in rubric criteria align with what was taught

If any check fails, fix data completeness first, then reassess the decision.

## What success looks like after re-teach

You can resume normal pacing when:

- class below-threshold share drops below the campus re-teach threshold
- weakest outcomes move from critical pressure toward watch/on-track
- reassessment results show improvement trend, not only one-off gains


**Last updated:** 2026-07-08

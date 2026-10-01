# Snapshot lifecycle

Snapshots are the historical records that power ILS trend analysis and reporting.

## What is a snapshot?

- A snapshot records a student’s mastery score for a single outcome at a specific moment.
- It includes the outcome, student, mastery value, timestamp, and any confidence metadata.

## When snapshots are created

- A snapshot is created when a relevant submission is graded.
- If the outcome’s mastery score changes, the system writes a new snapshot or updates an existing one.
- Snapshots capture the state of learning progress over time.

## Why snapshots matter

- They allow the system to compare current performance to historical performance.
- They are the foundation for trend direction and trend confidence.
- They support retrospective reporting and intervention decisions.

## Typical lifecycle

1. Grade is recorded for a submission linked to one or more outcomes.
2. The system aggregates rubric ratings into an outcome mastery value.
3. A snapshot is stored with the student, outcome, mastery score, and timestamp.
4. Later snapshots are compared against previous snapshots to compute trends.

## Practical notes

- Snapshots are not the same as raw grades; they are normalized mastery measures.
- The snapshot model keeps historical context even as new work is completed.
- A snapshot reflects a point-in-time mastery value for a student/outcome pair.
- New snapshots do not overwrite history; they extend it.

## Quiz evidence and source separation

Quiz evidence is recorded as outcome snapshots too, but it is kept conceptually separate from assignment evidence.
- Quiz questions that are linked to outcomes are aggregated per outcome within the quiz submission.
- The system writes a single outcome snapshot for that quiz submission and outcome combination.
- These quiz-origin snapshots are tagged with `source_type = 'quiz_question'` (or equivalent) so reporting can distinguish formative pulse from summative mastery.

This separation is important because it allows the cockpit and heatmap to remain stable while quiz evidence is added as its own intelligence layer.

## Example timeline

- Week 1: Student scores 70% on an outcome-linked assignment; mastery snapshot is created.
- Week 3: Student improves to 85%; a new snapshot is stored with the updated mastery value.
- Week 5: Snapshot history is used to determine whether the student is trending up or down.

## Using snapshots

- Snapshots are used by progress reports and trend calculations.
- They are the source data for the student detail and teacher cockpit screens.
- Snapshot history helps distinguish one-off low grades from sustained decline.


**Last updated:** 2026-07-08

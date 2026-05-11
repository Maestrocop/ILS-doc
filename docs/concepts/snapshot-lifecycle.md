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

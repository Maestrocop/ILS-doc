# Snapshot lifecycle

This page explains how snapshots are generated, updated, and used in the ILS analytics pipeline.

- Snapshots capture a student’s mastery score for a single outcome at a specific point in time.
- They are the basis for trend computation and historical analysis.
- A new snapshot is created or updated whenever a submission is graded and the outcome aggregation changes.

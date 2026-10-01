# Decision Layer Guidelines

This short guideline defines the three decision layers and which pages belong in each. Use this as the source of truth when designing coordinator-facing features.

## Layers

- Dashboard — Today (Reactive)
  - Purpose: immediate operational alerts requiring action now.
  - Keep content minimal: overdue counts, critical alerts, links to fix items.

- Programme Health — This week (Analytical)
  - Purpose: weekly oversight and investigations; trends and breakdowns.
  - Content: attendance trends, grading backlog trends, sessions delivered vs planned, curriculum delivery diagnostics.

- Intelligence — This semester / strategic (Strategic)
  - Purpose: long-term insight, cohort comparisons, curriculum effectiveness.

## UI placement rules
- Alerts (item needs action now) → Dashboard only.
- Trends and history → Programme Health.
- Cohort comparisons & predictive signals → Intelligence.

## Data source guidance
- For each page, document required data sources and owner (e.g., timetable events, submission events, survey responses).

**Last updated:** 2026-07-06

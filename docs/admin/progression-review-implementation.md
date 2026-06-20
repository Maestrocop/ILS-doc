# Progression Review (BSA) — Overview

Progression reviews are used to document and track student progress decisions. The system supports multiple review types and decision workflows.

## What you can do

Progression reviews support:

- Creating and configuring review types for your institution
- Recording support measures, warnings, and formal decisions
- Tracking review status and outcomes for each student
- Generating coordinator dashboards with progression statistics
- Enforcing policy requirements before binding decisions

## Review components

**Timeline & Evidence** — Records of support and notifications
- Development meetings
- Warnings and formal notifications
- Follow-up meetings
- Decision meetings
- Student acknowledgments
- Counselor referrals
- Deferrals and special cases

**Improvement Plan & Actions** — Planned work for students
- Planned meetings
- Assignment submissions
- Score improvement targets
- Counselor appointments
- Internal coordinator notes

## Decision stages

The review process typically follows:

1. **Mentor Recommendation** — mentor recommends outcome
2. **Committee Review** — committee reviews evidence
3. **Final Decision** — binding decision issued

## Policy enforcement

The system enforces policy requirements before allowing negative or binding decisions, such as:

- Warning must be issued
- Development meeting must be held
- Student must be informed
- Decision meeting must be documented
- Deferral eligibility must be checked

## Institution configuration

Each institution can configure:

- Review type names and descriptions
- Decision thresholds and stages
- Required evidence and decision policies
- Event and action types
- UI labels and policy documents
- Applicable academic years
- `ILS-dev/backend/scripts/backfill_outcome_snapshots.cjs`
- `ILS-dev/frontend/src/pages/ProgressionReviewsPage.jsx`
- `ILS-dev/frontend/src/pages/MyBSAReviewPage.jsx`
- `ILS-dev/frontend/src/pages/BSACoordinatorDashboard.jsx`
- `ILS-dev/frontend/src/components/ProgressionReviewDefinitionsTab.jsx`

## Validation and notes
- This document describes existing code and artifacts only. All writable documentation edits are under `ILS-doc/docs/`.

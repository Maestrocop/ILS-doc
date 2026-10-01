# Reporting Rules

This page documents the campus-level reporting rules implementation in ILS. Reporting rules define the thresholds used by classroom intelligence and heatmap analytics.

## What Reporting Rules are

Reporting rules are campus-scoped thresholds that determine when students are considered:
- inactive (`low_activity_days`)
- below success mastery (`success_threshold`)
- triggering a re-teach alert (`reteach_threshold`)

These values are configured per campus and used by multiple intelligence flows in ILS.

## Admin UI

- Admin path: `/admin/settings?tab=reporting-rules`
- Redirect path: `/admin/reporting-rules` redirects to the settings tab
- Frontend files:
  - `ILS-dev/frontend/src/pages/ReportingRules.jsx`
  - `ILS-dev/frontend/src/pages/SettingsPage.jsx`

### Settings behavior

The Reporting Rules UI:
- loads campus list via `GET /api/campuses`
- selects one campus at a time
- loads that campus's rules via `GET /api/campuses/:campus_id/reporting-rules`
- displays fields for low activity, success threshold, and re-teach threshold
- validates input values before saving
- saves changes with `POST /api/campuses/:campus_id/reporting-rules`

### Form fields and validation

`ReportingRules.jsx` enforces:
- `low_activity_days` must be an integer between `1` and `30`
- `success_threshold` must be a number between `0.0` and `10.0`
- `reteach_threshold` must be an integer between `0` and `100`

Validation is driven by `ILS-dev/backend/validation/reporting-rules.js` and mirrored in the UI.

## Backend API

The campus reporting rules endpoints are implemented in `ILS-dev/backend/routes/campus.js`.

### Endpoints

- `GET /api/campuses/:campus_id/reporting-rules`
- `POST /api/campuses/:campus_id/reporting-rules`

### Behavior

- `GET /api/campuses/:campus_id/reporting-rules` returns the saved rule set.
- If no rule row exists for the campus, the backend creates a default rule record automatically:
  - `low_activity_days`: `7`
  - `success_threshold`: `6.0`
  - `reteach_threshold`: `40`
- `POST /api/campuses/:campus_id/reporting-rules` upserts the rules and returns the saved row.

### Validation and payload

`validateReportingRulesPayload` enforces the same field constraints on the backend.

Accepted payload fields:
- `low_activity_days`
- `success_threshold`
- `reteach_threshold`

A failed validation returns HTTP `400` with error details.

## Intelligence integration

Campus reporting rules are used throughout the ILS intelligence layer:
- `HeatmapPage.jsx` applies `success_threshold`, `reteach_threshold`, and `low_activity_days` to classify student matrix statuses.
- `ClassroomIntelligencePage.jsx` loads the same campus rules for narrative generation, at-risk counting, and support recommendations.
- `backend/routes/cockpit.js` resolves campus reporting rules for class-level health and student cockpit summaries.

### Default fallback behavior

When reporting rules are missing from the database, the backend falls back to safe defaults so reporting and cockpit services continue to operate.


**Last updated:** 2026-07-08

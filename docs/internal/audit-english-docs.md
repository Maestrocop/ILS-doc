# English Documentation Audit — Initial Report

Purpose: capture the current state of English documentation, list issues to fix, and provide a prioritized next-step checklist.

Scan summary (2026-07-08):
- Site builds with `mkdocs build --strict`, but several doc files exist that are not included in `nav` (see below).
- There were links expecting an anchor `#grades`; `admin/data-exchange.md` now contains that anchor.

Unlisted documentation files (candidates to review and either add to nav or archive):
- TODO.md
- admin/curriculum-effectiveness.md
- admin/end-to-end-walkthrough.md
- admin/institution-review-definitions.md
- admin/intelligence-hub.md
- admin/pr-summary.md
- admin/progression-review-design.md
- admin/progression-review-implementation.md
- admin/progression-review-ui.md
- admin/security-and-compliance.md
- admin/setting-up-mentor.md
- admin/ui-issue.md
- internal/account-and-password-management.md
- internal/assistant_workflow_preferences.md
- internal/cookie-policy.md
- internal/known-ui-issues.md
- internal/privacy-and-your-data.md
- internal/school-data-processing-agreement.md
- internal/terms-of-service.md
- session-notes/assistant-logs-2026-06-06.md
- sessions/ils-session-2026-06-23-090000.md
- teacher/quickstart.md

Initial priorities
1. Add missing high-value pages to nav: `admin/security-and-compliance.md`, `internal/privacy-and-your-data.md`, `teacher/quickstart.md`.
2. Fix or remove low-value/unmaintained pages (e.g., old session notes) — move to `docs/internal/archived/` if needed.
3. Run a link-check pass across all docs and fix anchor mismatches.
4. Standardise `Last updated` header placement and create `docs/internal/glossary.md` and `docs/internal/style-guide.md`.

Suggested immediate tasks (this sprint)
- Add `teacher/quickstart.md` to the Teacher Guide nav (already exists but unlisted). Confirm placement.
- Review and add `admin/security-and-compliance.md` to Admin Guide nav.
- Create `docs/internal/glossary.md` (starter file) to begin standardising terminology.

Next steps I will take after your confirmation
- Execute a full link-check and generate a CSV of broken links.
- Add `docs/internal/glossary.md` starter file.

**Last scanned:** 2026-07-08


**Last updated:** 2026-07-08

# Gradebook

Overview: manage grades, rubric breakdowns, publish grades, and export gradebooks.

Steps:
- Open `Course` → `Gradebook`.
- Edit grades inline or download CSV for bulk edits (`Data Exchange` → `Export` → `Gradebook Template`).
- Publish grades: select `Publish` to make visible to students.

Tips: use filters to view by module, assignment, or student.

Last updated: 2026-07-08

Example CSV template (see `docs/admin/templates/gradebook_template_v1.csv`):

- Columns: `student_id`, `student_email`, `assignment_code`, `grade`, `comment`

Upload flow for bulk edits:
- Export current gradebook via `Data Exchange` → `Export` → `Gradebook`.
- Edit CSV, keep `student_id` and `assignment_code` unchanged.
- Re-import via `Data Exchange` → `Import` and choose `Gradebook Template`.

Publishing policies
- Draft vs Published grades: grades saved as draft are only visible to teachers. Use `Publish` to make visible to students.

Grade overrides & audits
- All grade edits create an audit entry. To override a published grade, edit and re-publish; the audit log records user, timestamp, and previous value.

Screenshot placeholders
- [screenshot: gradebook-inline-edit]
- [screenshot: gradebook-export]

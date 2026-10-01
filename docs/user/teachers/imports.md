# Importing Data (Teachers)

Use `Data Exchange` → `Import` to upload grades or outcomes CSVs. Follow the ImportShell flow:
- Upload: choose CSV and template
- Map: match CSV columns to system fields
- Validate: resolve row-level errors
- Preview: review sample rows
- Confirm: commit the import and view report

Last updated: 2026-07-08

Templates:
- Gradebook template: `docs/admin/templates/gradebook_template_v1.csv`
- Outcomes template: `docs/admin/templates/outcomes_template_v1.csv`

Validation tips:
- Ensure `student_id` or `student_email` match existing users.
- Scores must be numeric and within rubric ranges.

Detailed ImportShell steps

1) Upload
- Click `Data Exchange` → `Import` → choose `Gradebook` or `Outcomes` template.
- Select the CSV file and click `Upload`.

2) Map
- For each CSV column, choose the matching system field. Required fields: `student_id` or `student_email`, `assignment_code`, and the score/grade column.

3) Validate
- The system shows per-row validation. Common errors:
	- `Unknown student_id`: the student does not exist — correct `student_id` or use `student_email`.
	- `Invalid score`: non-numeric or out-of-range value.

4) Preview
- Review a sample of successfully parsed rows and any flagged rows.

5) Confirm
- Confirm to persist changes. A job report will be available under `Data Exchange` → `Reports`.

Screenshot placeholders
- [screenshot: import-upload]
- [screenshot: import-map]
- [screenshot: import-validate]

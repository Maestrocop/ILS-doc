# Outcomes Importer — API Contract

Purpose: define the HTTP API surface for server-side importer integration with the ImportShell front-end.

Base endpoint
- `POST /api/admin/imports/outcomes` — start an import job

Request (multipart/form-data)
- `file` — CSV or XLSX upload (required)
- `mapping` — JSON object mapping uploaded columns to target fields (optional)
- `mode` — one of `create_only`, `create_or_update`, `replace` (default: `create_or_update`)
- `notify` — boolean, whether to send async completion notification (default: false)

Response (201 Created)
- Body: `{ "job_id": "<uuid>", "status": "queued" }`

Status polling
- `GET /api/admin/imports/outcomes/{job_id}` — returns job progress and preview
- Sample response:
```
{
  "job_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "running", // queued | running | finished | failed
  "progress": 42, // percent
  "preview": [{ "row": 1, "status": "OK", "message": null }],
  "summary": { "total": 100, "ok": 88, "warnings": 8, "errors": 4 }
}
```

Fetch report
- `GET /api/admin/imports/outcomes/{job_id}/report` — returns CSV/JSON report with row-level statuses

Re-run failed rows
- `POST /api/admin/imports/outcomes/{job_id}/replay` with body `{ rows: [1,5,7] }` to retry only failed rows.

Webhooks / Notifications
- POST to configured webhook when job finishes with a minimal payload: `{ job_id, status, summary }`.

Errors
- Use standard problem+json responses with `type`, `title`, `status`, `detail`.

Security
- Require `Admin` or `Designer` role; CSRF protections; file size limits and virus scanning on upload.

Rate limits & quotas
- Enforce per-org concurrent import job limits (configurable).

See also: `admin/outcomes-importer-spec.md`, `admin/import-report.md`, `admin/import-shell.md`.

**Last updated:** 2026-07-07

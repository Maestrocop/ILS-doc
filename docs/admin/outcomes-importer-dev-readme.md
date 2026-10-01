# Outcomes Importer — Developer README

Purpose: implementation notes and sample code patterns to wire the Outcomes importer job, report generation, and webhooks.

Architecture overview
- HTTP API accepts upload and returns a `job_id`.
- A background worker processes the file: parsing, validating against `schemas/outcomes-import-schema.json`, preview generation, and applying DB changes.
- Worker emits progress events and final report; job state stored in `imports_jobs` table (or queue metadata store).
- Optional webhook or notification on completion.

Recommended components
- Controller: handle multipart upload, save file to object store, enqueue job, return `job_id`.
- Worker: dequeue job, stream-parse file, validate each row, write preview rows to `import_preview_rows` table (or cache), apply changes in a transaction per-batch.
- Reporter: compile final report CSV/JSON and store in object store; expose `GET /report` endpoint.
- Replay endpoint: accept row list and re-enqueue only failed rows.

Example worker pseudocode (Node.js-like):

```
async function processJob(job) {
  const stream = openFileStream(job.filePath);
  const parser = csvParser(stream);
  let rowNum = 0;
  for await (const row of parser) {
    rowNum++;
    const valid = validateRow(row, outcomesSchema);
    if (!valid) {
      savePreviewRow(job.id, rowNum, 'Error', getErrors(valid));
      continue;
    }
    const result = await applyRowToDb(row, job.mode);
    savePreviewRow(job.id, rowNum, result.status, result.message);
    updateProgress(job.id, calculateProgress());
  }
  const report = await compileReport(job.id);
  saveReportToStore(job.id, report);
  notifyWebhook(job.webhookUrl, { job_id: job.id, status: 'finished', summary: report.summary });
}
```

Validation and acceptance tests
- Use `schemas/outcomes-import-schema.json` with a JSON Schema validator (Ajv for Node, jsonschema for Python).
- Provide unit tests that feed valid, warning, and error CSV rows and assert preview statuses and final report counts.

Transaction strategy
- Batch writes (e.g., 100 rows) inside transactions to limit rollback blast radius.
- For `create_or_update` mode, perform `UPSERT` semantics keyed by `code`.

Security and operational notes
- Scan uploaded files for viruses before processing.
- Enforce max file size and row limits (configurable).
- Record audit trail: who uploaded, timestamp, job_id, actions performed.
- Rate limit per-organization concurrent imports.

Observability
- Emit metrics: jobs_started, jobs_failed, rows_processed, avg_row_latency.
- Store processing logs per job for troubleshooting.

Retry and idempotency
- Design `applyRowToDb` to be idempotent; use `code` as natural dedupe key.
- Replay endpoint should accept row indices and run the same validation/apply logic.

See also: `admin/outcomes-importer-api.md`, `admin/schemas/outcomes-import-schema.json`, `admin/outcomes-sample-responses.md`.

**Last updated:** 2026-07-07

# Outcomes Importer — Sample Server Responses

Queued response (201):

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "job_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "queued"
}
```

Polling response (running):

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "job_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "running",
  "progress": 42,
  "preview": [
    { "row": 1, "status": "OK", "message": null },
    { "row": 2, "status": "Warning", "message": "framework not found" },
    { "row": 3, "status": "Error", "message": "code missing" }
  ],
  "summary": { "total": 3, "ok": 1, "warnings": 1, "errors": 1 }
}
```

Report download (CSV) — `GET /api/admin/imports/outcomes/{job_id}/report`

```
row,status,message
1,Imported,
2,Imported,framework not found - created as draft
3,Error,code missing
```


**Last updated:** 2026-07-08

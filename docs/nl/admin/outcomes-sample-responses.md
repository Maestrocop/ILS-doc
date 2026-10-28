# Outcomes Importer — voorbeeldantwoorden van de server

Antwoord bij in de wachtrij plaatsen (201):

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "job_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "queued"
}
```

Antwoord bij opvragen van de voortgang (bezig):

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

Rapport downloaden (CSV) — `GET /api/admin/imports/outcomes/{job_id}/report`

```
row,status,message
1,Imported,
2,Imported,framework not found - created as draft
3,Error,code missing
```


**Laatst bijgewerkt:** 2026-07-08

# Pre‑September Setup Checklist

Status: use this checklist to track the last tasks before an academic intake (September).

Done ✅

- Academic Calendar — holidays, breaks, exam periods
- Academic Periods — Academic Year 2026‑2027 defined
- Classes created — WILISE1A etc.
- Timetables → sessions generated (holiday‑aware)

Current step — You are here

- Enroll students into classes (required before grading, cockpit, intelligence)

How to enroll

- The backend exposes an admin API to enroll students:

- POST `/api/classes/:id/students` (admin only)
- Implementation: see the backend file `ILS-dev/backend/routes/classes.js` (lines ~200–246) for the SQL/behavior. The endpoint inserts into `class_enrollments` and uses `ON CONFLICT` to reactivate existing enrollments.

Example (admin token required):

```bash
curl -X POST "http://localhost:4000/api/classes/123/students" \
  -H "Authorization: Bearer <ADMIN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"user_id":456}'
```

Bulk enrollment (CSV)

If you need to enroll many students at once, prepare a CSV file and batch the API calls. The backend endpoint accepts a single `user_id` per request (the `class_id` is supplied in the URL). Preferred CSV format:

```
user_id
456
457
458
```

PowerShell (Windows) — batch enroll from `students.csv`:

```powershell
# Set your admin token in an environment variable first
#$env:ADMIN_JWT = '<ADMIN_JWT>'
$csv = Import-Csv -Path "students.csv"
foreach ($row in $csv) {
  $body = @{ user_id = [int]$row.user_id } | ConvertTo-Json
  Invoke-RestMethod -Method Post -Uri "http://localhost:4000/api/classes/123/students" `
    -Headers @{ Authorization = "Bearer $env:ADMIN_JWT"; "Content-Type" = "application/json" } `
    -Body $body
  Start-Sleep -Milliseconds 200
}
```

Bash (Linux / WSL / Git Bash) — simple loop:

```bash
ADMIN_JWT="<ADMIN_JWT>"
while IFS=, read -r user_id; do
  curl -s -X POST "http://localhost:4000/api/classes/123/students" \
    -H "Authorization: Bearer $ADMIN_JWT" \
    -H "Content-Type: application/json" \
    -d "{\"user_id\":${user_id}}"
  sleep 0.2
done < students.csv
```

Notes and gotchas

- Replace `123` with the target class id (e.g., the id for `WILISE1A`).
- If you only have emails, you must resolve `user_id` first (the project may expose a user lookup endpoint; otherwise use the admin UI).
- The server enforces `enrollment_type` exclusivity for some classes — attempting to enroll a user who already has an exclusive enrollment elsewhere will return `409` with an explanatory message.
- To unenroll a student use: `DELETE /api/classes/:id/students/:userId` (admin only).
- Add small sleeps between requests to avoid hammering the dev server.
Notes & gate

- Without student enrollments the rest of the flow (submissions, grading, cockpit, heatmap) will not produce meaningful results.
- Admin UI availability for enrolling students is not confirmed in ILS‑dev — the server endpoint exists, see the code link above.

Next steps (in order)

1. Enroll students into class WILISE1A (you are here)
2. Assign curriculum (courses/modules) to the class
3. Assign teachers to the class
4. When sessions occur: mark sessions held, create assignments, students submit, teachers grade
5. Intelligence layer (snapshots, heatmap, cockpit) will begin producing insights as graded evidence accumulates

Editable slot suggestion

- If you need to correct a timetable slot (time or day), see the proposed API & UI in the Slot Edit Proposal: `admin/slot-edit-proposal.md`.

Safety

- Reminder: do not modify `ILS-dev` source code directly during documentation changes. This checklist documents current status and suggested changes only.


**Last updated:** 2026-07-08

# Periods Playbook — Clear, Friendly Cheat Sheet

This is a short, friendly, actionable playbook for Admins / Designers / Teachers. Read-only: I will not modify `ILS-dev`.

## One-line rule

Create dated periods first (Academic Calendar), then build curriculum, then create timetable rules.

---

## Quick checklist (what to do now)

- Admin: Run the `Orphan periods` SQL (below). If any rows show up, pick Remediate A or B.
- Designer: Always use the Period picker in Composer — do not type new period labels.
- Teacher: If sessions missing, send screenshot + class id to Admin.

---

## Example SQL (copy-paste)

Find undated periods:

```sql
SELECT id, name, parent_id FROM academic_periods WHERE start_date IS NULL OR end_date IS NULL ORDER BY id;
```

Find course_structure pointing at undated periods:

```sql
SELECT cs.id AS cs_id, cs.course_id, cs.module_id, ap.id AS period_id, ap.name
FROM course_structure cs
JOIN academic_periods ap ON ap.id = cs.period_id
WHERE ap.start_date IS NULL OR ap.end_date IS NULL;
```

---

## Remediation — two safe options

Option A — Add dates (preferred when period was intended):

1. Open Admin → Periods → Edit the orphan period.
2. Set `start_date` and `end_date` and `parent_id` = the academic year.
3. Run timetable regen for the class and confirm sessions appear.

Option B — Repoint course_structure (preferred when semesters are used):

1. Update `course_structure.period_id` to the correct semester id (via UI or API).
2. Verify `course_structure` slot shows the semester name in Composer.
3. Re-run timetable generation and confirm.

---

## Example API remediation (curl)

Add dates to period id 185:

```bash
curl -X PATCH "http://localhost:4000/api/curriculum/periods/185" \
  -H "Content-Type: application/json" \
  -d '{"start_date":"2025-09-01","end_date":"2026-02-28","parent_id":123}'
```

Repoint a course_structure slot (id 999) to semester id 32:

```bash
curl -X PATCH "http://localhost:4000/api/curriculum/structure/999" \
  -H "Content-Type: application/json" \
  -d '{"period_id":32}'
```

> Note: Always backup DB before running API changes against production.

---

## Small illustration — data flow

Periods (Academic Calendar) → Course Structure (Composer) → Timetable Rules → Sessions

If any arrow points to an undated period, sessions will not generate.

---

## Day-to-day admin health quick steps

1. Weekly: run the `undated periods` SQL; fix new rows immediately.
2. Before each semester: confirm periods for the year exist and are dated.
3. After composer edits: run `GET /api/curriculum/courses/:courseId/structure` and inspect `period` names.

---

If you want, I'll also add a small migration script template (docs-only) to bulk remap orphan `course_structure` rows. I will not change any code in `ILS-dev`.


**Last updated:** 2026-07-08

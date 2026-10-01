# Admin Health Checks — Find & Fix Orphan Periods

This page lists quick health checks for Admins to find orphan/undated academic periods, inspect course structure references, and remediate safely. Read-only: `ILS-dev` will not be changed by these docs.

## Quick checklist

- Run the `Orphan periods` query and review results.
- Identify `course_structure` rows referencing undated periods.
- Decide remediation approach: Add dates & parent, re-point course_structure, or delete orphan.
- Backup DB before making any destructive changes.

---

## Example SQL queries (read-only helpers)

1) Find undated academic_periods (orphans)

```sql
SELECT id, name, parent_id
FROM academic_periods
WHERE start_date IS NULL OR end_date IS NULL
ORDER BY id;
```

2) Find course_structure rows pointing to undated periods

```sql
SELECT cs.id AS course_structure_id, cs.course_id, cs.module_id, ap.id AS period_id, ap.name
FROM course_structure cs
JOIN academic_periods ap ON ap.id = cs.academic_period_id
WHERE ap.start_date IS NULL OR ap.end_date IS NULL
ORDER BY cs.course_id;
```

3) Find timetable rules referencing undated periods

```sql
SELECT tsr.id AS rule_id, tsr.class_id, tsr.academic_period_id, ap.name
FROM timetable_schedule_rules tsr
JOIN academic_periods ap ON ap.id = tsr.academic_period_id
WHERE ap.start_date IS NULL OR ap.end_date IS NULL;
```

---

## Implementation notes (what to look for in the code)

These reflect current `ILS-dev` behavior so you can correlate Health check results with the pages and APIs:

- Composer creates course-owned periods via `POST /api/curriculum/courses/:courseId/periods` and may leave `start_date`/`end_date` null if entered that way.
- Course structure creation endpoints (`POST /api/curriculum/courses/:courseId/structure`) accept a `period_id` and will insert rows linking modules to that period id; these writes do not validate that the period has dates on the API boundary.
- Use the Admin Periods UI (Periods page) which calls `GET /api/periods` and `GET /api/periods/tree` to view and edit periods; updates use `PUT /api/periods/:id` or `PATCH /api/curriculum/periods/:periodId` for course-scoped periods.

If you want, I can add the exact endpoint examples (curl + request body) to help Admins perform remediation via API. I will not change `ILS-dev`.

---

## Safe remediation steps

1. Backup DB (dump or create a migration that copies affected rows).
2. If the orphan period was intended for the correct year: set `start_date` and `end_date` and set `parent_id` to the academic year row.
3. If the orphan should be removed: migrate `course_structure` references to the correct dated period ids, test, then delete orphan period.
4. Re-run timetable generation for the affected classes and verify sessions appear.

---

## Automated health guidance (what to show on Health page)

- Count of undated periods.
- List of `course_structure` entries referencing undated periods (course, module, period id).
- List of `timetable_schedule_rules` referencing undated periods and whether they generate zero sessions.

---

If you'd like, I can also add a small admin-facing checklist UI mockup and a suggested migration script template to help with bulk remapping. I will not modify `ILS-dev` — only update docs in `ILS-doc`.


**Last updated:** 2026-07-08

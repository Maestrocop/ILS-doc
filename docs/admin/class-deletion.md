# Deleting a Class — Admin Guide

Before you delete a class you must ensure certain related records are cleared. The UI only supports some operations; others require manual intervention or are cleaned automatically.

## Required manual clearing before delete

- Enrolled students
  - Where: Class detail → Students tab → unenroll each student
- Submissions
  - Note: Submissions cannot be deleted from the UI — this requires a direct DB action (DB team/coordinator only)
- Progression reviews
  - Where: Admin → Progression Reviews → delete each review linked to the class
- Internship campaigns
  - Where: Admin → Internships → unlink or remove campaigns associated with the class

## Auto-cleaned on delete (no action needed)

The following are automatically cleaned up when a class is deleted:

- Timetable sessions & slots
- Class teachers, class modules
- Calendar events, outcome snapshots, quiz attempts, project assignments

## Recommended procedure

1. Export any required data for archives (grades, submissions metadata).
2. Unenroll all students via Class detail → Students tab.
3. Remove or unlink internship campaigns and progression reviews tied to the class.
4. If submissions must be removed, coordinate with the DB team (this is not supported in the UI).
5. Proceed to delete the class in Admin once the above are clear.

## Notes

- Do NOT attempt to delete submissions from the UI; it will fail or leave orphaned records.
- If you need a UI enhancement to allow safe deletion of submissions or assign bulk-unenroll, raise a docs/feature request and track it in `Active-ILS-doc.md`.


**Last updated:** 2026-07-08

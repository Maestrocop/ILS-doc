# Classes

Classes are academic sections that group students together for a course. Use the Classes page to manage sections, enroll students, and organize your teaching groups.

## What you can do

Go to **Classes** in the admin menu to:

- View all class sections
- Create a new class for a course or module
- Edit class details (name, schedule, teacher assignments)
- Enroll students individually or in bulk via CSV
- Remove classes that are no longer needed

## Class details

When you create or edit a class, you'll set:

- **Class name** — the section name students will see
- **Course or module** — what this class is teaching
- **Schedule** — days and times (optional)
- **Teacher assignments** — who teaches this section

## Enrolling students

**Individual enrollment:**
1. Open a class
2. Click "Add student"
3. Select the student from the list

**Bulk enrollment via CSV:**
1. Open a class
2. Click "Import from CSV"
3. Upload your student roster file
4. Review the preview (shows which students will be created or enrolled)
5. Confirm to complete enrollment

The system will:
- Create new student accounts if they don't exist
- Skip students already enrolled in that class
- Show a summary after import (created, enrolled, skipped)

## Admin workflow

1. Navigate to `/admin/classes`.
2. Review active sections and their course/module relationships.
3. Create or update class details as needed.
4. Delete classes that are no longer required.

## Notes

- Classes are a core administrative entity that links courses, teachers, and students.
- Class records are used to scope assignment distribution and progress tracking.

## Recent changes (June 2026)

- CSV bulk-enroll now supports creating new student records during import and shows clearer per-row warnings for students already enrolled in overlapping classes. If a student appears in two classes for the same module, the UI warns before finalizing the import.
- A single-click cohort enroll option was added to enable quick enrollment of entire cohorts into a class.


**Last updated:** 2026-07-08

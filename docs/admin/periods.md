# Periods

The Periods page manages the academic time structure used across classes and reporting.

## What you can do

Go to **Periods** in the admin menu to:

- View all active academic periods
- Create and update periods with start/end dates
- Delete outdated or unused periods
- Define nested academic period hierarchy (semesters, blocks, units)
- Manage reusable period templates for courses and programs
- Work with academic calendar events (holidays, exams, closures)

## Academic Calendar Events

Academic Calendar Events are separate from Academic Periods. They capture schedule exceptions and special dates such as:

- Holiday
- Exam
- Closure
- Event

Events can be scoped to institution, campus, or class. They include flags such as:
- Is this a teaching day?
- Visible to students?
- Visible to teachers?

These events are independent calendar annotations that affect visibility and daily teaching status.

## Official Academic Periods vs Course Blueprint Periods

**Academic Periods** are the institution's official calendar skeleton. They are:
- Dated, school-wide declarations
- Do not describe weeks, modules, or course-specific delivery details

Example structure:
- Academic Year 2025-2026 (Sep 2025 → Jun 2026, institution-wide)
  - Semester 1 (Sep 2025 → Jan 2026)
    - Block 1 (Sep → Oct 2025)
    - Block 2 (Nov → Jan 2026)
  - Semester 2 (Feb 2026 → Jun 2026)
    - `Block 3 (Feb → Mar 2026)
    - Block 4 (Apr → Jun 2026)

**Key rule:** Academic Periods are institution-level and date-based. They represent the official published school calendar.

**Course-specific curriculum structure** belongs in Curriculum Composer V2. Those periods are course blueprint structure only: they describe the order and nesting of delivery blocks or weeks, but they do not carry real dates or institution-level scope.

This separation keeps:
- **Academic Periods** = official school calendar dates
- **Curriculum Composer periods** = course blueprint structure without dates

## Period Templates Tab

A **Period Templates** tab is available alongside Academic Periods.

### What you can do with templates

- Build reusable period structures once and save them as named templates
- Templates capture the nested period tree
- Edit with drag/indent/rename controls
- Saved templates are reusable across courses and curriculum workflows
- Apply a template to a course to populate the course's period tree instantly
- Applied templates are detached copies: later changes to the template do not sync to an already-applied course

### When to use templates

- When multiple courses share the same period structure
- To quickly set up new courses with standard semester/block patterns
- To maintain consistency across programs

### How templates work

- Applying a template preserves any existing periods in the course
- Full replace mode is available but blocked when the course already has modules assigned to active periods
- If a course period tree has been customized after apply, edit it directly in Curriculum Composer V2 rather than relying on template re-sync

## Period Hierarchy

The academic period model supports unlimited nesting. Any period can become a container by adding sub-periods, and containers can also hold modules directly.

Example:
- Semester 1 (parent)
  - Period 1 (child of Semester 1) — may link to Module "Basics"
    - Unit 1 (child of Period 1) — may link to Module "Basics Week 1"

## Admin workflow

1. Open `/admin/periods`.
2. Add new academic periods for the current term or year.
3. Adjust start/end dates as needed.
4. Retire old periods when they are no longer relevant.

## Notes

- Periods provide a time dimension for classes, course sections, and progress reporting.
- They are commonly used to scope assignments and evaluate student cohorts.

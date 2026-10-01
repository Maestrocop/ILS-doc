## Milestone: Usage Awareness & Archival (Critical Safeguards)

As the system transitions from CRUD to a true curriculum platform, implement these safeguards before further growth:

### Usage Awareness ("Where is this used?")
Before allowing destructive actions (delete assignment, edit blueprint, archive module item), always check:

- In how many modules is this asset used?
- In how many active classes?
- How many submissions reference it?
- Is it scheduled in any timetables?

This prevents accidental curriculum breakage and catastrophic data loss as reuse increases.

### Soft Delete / Archive Only
For assignments, quizzes, modules, and other curriculum assets:

- Avoid hard deletes — always archive or soft-delete.
- This preserves analytics, submissions, snapshots, and timetable references for historical integrity.

**Summary:**
Assets, placements, lineage, and usage must all coexist. Usage awareness and archival are critical for safe curriculum evolution and platform stability.
## End-to-End QA: Session Summary & Architecture Steps

All 8 steps below were completed in this session:

### Steps 1–3 — Curriculum Asset Architecture
- **Migration 0070:** Added `origin_module_id` to assignments (records which module birthed each assignment)
- **Assignment form:** Added cascading Course → Module selector to set origin on save
- **POST/PUT:** Both create a `module_items` placement automatically when `origin_module_id` is provided
- **Migration 0071:** Added `is_blueprint`, `blueprint_id`, `derived_from_id` to assignments (schema live, UI deferred until after #64)

### Steps 4–6 — DIS-BASIS Content
- **SM-BASIS Quiz 1 (id=11):** 10 ITIL MCQ questions, 30-min limit, published
- **DIS-A1–A5 (ids 23–27):** PowerShell Basics, Python Fundamentals, SQL Queries, Automation Script, Data Analysis — all linked to DIS-BASIS via `origin_module_id` + `module_items`
- **DIS Quiz 1 (id=12):** 12 questions (4 PowerShell, 4 Python, 4 SQL), published

### Steps 7–8 — Classes & Timetable
- **Modules assigned:** SM-BASIS and DIS-BASIS assigned to both WILISE1A and WILISE1B via `class_modules`
- **Timetables created:**
  - WILISE1A: Mon 9–11 / Wed 13–15 / Fri 10–12 → 63 sessions
  - WILISE1B: Tue 9–11 / Thu 13–15 / Fri 13–15 → 63 sessions
  - Semester 1: Sep 7, 2026 – Jan 29, 2027

**Note:** The backend must be restarted to pick up the two model changes (`origin_module_id`, `is_blueprint`, `blueprint_id`, `derived_from_id`).

---
This summary captures the full end-to-end QA and curriculum entry process for both admin and teacher roles, including all model and UI changes, content creation, and scheduling.
## Step 3 — Assignment & Quiz Creation, Module-Class Linking, Timetable Scheduling

Follow these steps in order for each module (repeat for SM-BASIS and DIS-BASIS):

### 1. Assignments
- Go to: Admin sidebar → Assignments → + New Assignment
- For each module, create 5 assignments:
  - SM-BASIS: A1–A4 plus Service Management Simulation
  - DIS-BASIS: A1–A4 plus Mini Information System
- For each assignment:
  - Fill in the title, due date, points/scale, and link to the correct module and outcomes as per the curriculum card.
  - Save and confirm the assignment appears in the module’s assignment list.

### 2. Quizzes
- Go to: Admin sidebar → Quizzes → + New Quiz
- For each module, create the quiz:
  - SM-BASIS: Service Management Quiz 1
  - DIS-BASIS: Digital Information Systems Quiz 1
- Fill in the title, due date, points/scale, type (multiple choice), and link to the correct module.
- Save and confirm the quiz appears in the module’s quiz list.

### 3. Assign modules to classes
- Go to: Admin sidebar → Classes → [Select class: WILISE1A or WILISE1B]
- In the class detail page (teacher class plan view), assign both modules (SM-BASIS and DIS-BASIS) to each class.
- Confirm both modules are listed for each class.

### 4. Timetable scheduling
- Go to: Admin sidebar → Timetable (or Class detail → Timetable tab)
- Schedule sessions for both classes starting September, matching the module schedules (e.g., SM-BASIS: Monday 09:00–11:00, DIS-BASIS: Tuesday 09:00–11:00).
- Add recovery/evaluation week as Week 9.
- Confirm all sessions are visible in the timetable/calendar view for each class.

---
Paste each step you complete below using the QA format for traceability.
## Step 2 — Module 1: Service Management Basis (full entry example)

This section documents a complete example of entering Module 1 (Service Management Basis) in the Module Form, capturing all fields and sections as seen in the UI.

### Identity
- Course: ICT System Engineer
- Duration: 9 Weeks (8 sessions + 1 recovery)
- Module Code: SM-BASIS
- Level: N4
- Module Name: Service Management Basis
- Description: Introduction to ICT service management, ITIL processes and service management tools. Students handle incidents, communicate with users and work according to SLAs.

### Themes (linked)
- Seed Theme B
- Smoke Theme - edited123
- Seed Theme A
- Smoke Theme API
- Seed Theme A (edited)
- Service Management
- Communication Skills
- ITIL

### Module Objectives
1. ITIL Foundations — Introduce core ITIL service management processes
2. Tool Proficiency — Develop practical skills with a service management tool (TopDesk)
3. Professional Communication — Apply communication techniques in ICT support contexts

### Module Structure (by week)
| Week | Topic                              | Activity                | Output / Deliverable      |
|------|------------------------------------|-------------------------|---------------------------|
| 1    | Introduction to ITIL & Service Mgmt | Lecture                 | Reading + notes           |
| 2    | Communication with Users           | Lecture + role play     | Assignment 1              |
| 3    | SLAs — theory                      | Lecture                 | Report, exercises…        |
| 4    | SLAs — practice + Quiz             | Workshop                | Assignment 2 + Quiz       |
| 5    | Incident Management                | Lecture                 | Report, exercises…        |
| 6    | TopDesk — hands on                 | Lab                     | Assignment 3              |
| 7    | Problem solving & escalation       | Workshop                | Assignment 4              |
| 8    | Project preparation                | Self-study              | Report, exercises…        |
| 9    | (Recovery / evaluation)            | Lecture, workshop…      | Assignment 5              |

### Assessment
| Type       | Description                                 | Weight (%) |
|------------|---------------------------------------------|------------|
| Assignment | 4 individual assignments (A1–A4)            | 40         |
| Quiz       | Multiple choice — Service Management Quiz 1 | 20         |
| Project    | Service Management Simulation (A5 + pres.)  | 40         |
| **Total**  |                                             | **100**    |

### Advanced / Pedagogy
- workshop
- Lecture
- Seminar
- Self-study
- Lab

---
Paste each step you complete (save, assign, etc.) below using the QA format for traceability.
# Curriculum Entry — OP1 (Admin+Teacher E2E Checklist)

This page is a working checklist and data-capture template for entering the Curriculum Reference Card "OP1 — ICT Support and Systems · Year 1 · September 2027" into the ILS admin UI. Use it while you perform the end-to-end test; after each UI step paste the result into the assistant using the prescribed QA step format and the assistant will convert it into the final user guide text.

Curriculum Reference Card — OP1

- Course: ICT Support and Systems (code: 23405)
- Shared Outcomes:
  - SO-1: Clarify and document user needs in plain language
  - SO-2: Present a technical solution to a non-technical audience

Module 1 — Service Management Basis (SM-BASIS)
- Hours OP1: 16h (8 × 2h sessions)
- Hours total: 34h
- Schedule: Monday 09:00–11:00 · Week 9 = recovery
- Outcomes:
  - SM-O1: Apply ITIL concepts and service management processes in daily ICT work
  - SM-O2: Register and handle incidents using a service management tool (TopDesk)
  - Shared: SO-1 ✓, SO-2 ✓
- Assignments:
  - A1 — Intro to ITIL & Service Management — Due Week 2 (2027-09-12) — 10 pts (/10) — Linked: SM-O1
  - A2 — Communication with Users — Due Week 4 (2027-09-26) — 20 pts (/20) — Linked: SO-1
  - A3 — Working with SLAs — Due Week 6 (2027-10-10) — 15 pts (/20) — Linked: SM-O1, SM-O2  
    - Note: points/scale mismatch (15 pts listed, scale /20). Confirm whether the intended scale is `/15` or the points should be `20`.
  - A4 — Incident Handling in TopDesk — Due Week 8 (2027-10-24) — Pass/Fail — Linked: SM-O2
  - A5 — Service Management Simulation — Due Week 9 (2027-11-01) — 100 pts (/100) — Linked: all outcomes

- Quiz (closes A2): Service Management Quiz 1 — Due Week 4 (2027-09-26) — 10 pts (/10) — Multiple choice

Module 2 — Digital Information Systems Basis (DIS-BASIS)
- Hours OP1: 16h (8 × 2h sessions)
- Hours total: 34h
- Schedule: Tuesday 09:00–11:00 · Week 9 = recovery
- Outcomes:
  - DIS-O1: Write and execute basic scripts using PowerShell or Python
  - DIS-O2: Query and interpret data from a database using SQL
  - Shared: SO-1 ✓, SO-2 ✓
- Assignments:
  - A1 — What is Digital Information? — Due Week 2 (2027-09-12) — 10 pts (/10) — Linked: DIS-O1
  - A2 — Basic Scripting — Due Week 4 (2027-09-26) — 20 pts (/20) — Linked: DIS-O1
  - A3 — Logic & Decisions in Scripts — Due Week 6 (2027-10-10) — 15 pts (/20) — Linked: DIS-O1
  - A4 — Database Basics & SQL Queries — Due Week 8 (2027-10-24) — Pass/Fail — Linked: DIS-O2
  - A5 — Build a Mini Information System — Due Week 9 (2027-11-01) — 100 pts (/100) — Linked: all outcomes

- Quiz (closes A3): Digital Information Systems Quiz 1 — Due Week 6 (2027-10-10) — 10 pts (/10) — Multiple choice

Pre-entry checks (confirm before starting)

- Confirm the `Course` exists ("ICT Support and Systems"). If not, create it in Admin → Courses with Code `23405`.
- Decide how to handle the A3 point/scale mismatch noted above.
- Have an admin account with course/module creation rights and a teacher account (if separate) for verification.

Step 1 — Create Module (Module 1: Service Management Basis)

- UI path: Admin sidebar → Modules → + New Module
- Fill fields (populate exactly as below):
  - Name: Service Management Basis
  - Code: SM-BASIS
  - Course: ICT Support and Systems (select from list)
  - Hours OP1: 16
  - Hours total: 34
  - Schedule: Monday 09:00–11:00 (add week notes: Week 9 = recovery)
  - Outcomes: add SM-O1, SM-O2, and link SO-1 and SO-2 as shared outcomes
  - Assignments: create the assignment skeletons (A1–A5) with due weeks and scales as listed above

After you click Save, report back using this QA step format (one step per entry):

- Role: Admin | Teacher
- Page / UI: (e.g., Modules → Service Management Basis)
- Action: (create, save, assign, upload, etc.)
- Input/data used: (exact values, files uploaded)
- Expected result: (what should happen)
- Actual result: (what happened; paste error messages if any)

Example report (fill this after saving Module 1):

- Role: Admin
- Page / UI: Modules → + New Module → Service Management Basis
- Action: Click Save
- Input/data used: Name=Service Management Basis, Code=SM-BASIS, Course=ICT Support and Systems, Hours OP1=16, Hours total=34, Schedule=Mon 09:00–11:00
- Expected result: Module saved and visible in Modules list; appears in Course editor as selectable module
- Actual result: (leave blank if OK, otherwise paste error/screenshot)

Notes for the assistant

- I will convert each report you paste into a concise step for the Admin+Teacher manual and add troubleshooting notes where actual ≠ expected.
- I will not change `ILS-dev`; this is read-only documentation and QA capture only.

## Step 1 — Result (recorded)

- Role: Admin
- Page / UI: Admin → Courses
- Action: Verify existence of course "ICT Support and Systems" (create if missing)
- Input / data used: Name = ICT Support and Systems, Code = 23405
- Expected result: Course exists or is created and visible in Courses list; selectable when creating a Module.
- Actual result: Completed without issue (user reported). Please confirm whether the course already existed or was created, and paste the exact display name if it differs from "ICT Support and Systems".

## Course Creation — ICT System Engineer (recorded)

- Role: Admin
- Page / UI: Admin → Courses → + New Course
- Action: Create course and Save
- Input / data used:
  - Full Name: ICT System Engineer
  - Code: Crebonr. 27016
  - Short Code: ISE-N4
  - Level: MBO 4
  - Duration: 3 Years
  - Description: Brief description of this course…
  - Settings: Status = Draft, Enrollment = Open Enrollment, Credits (ECTS) = e.g. 240
  - Course Color: #92a30f
  - Partner Institutions: BIM Institute of Technology
- Expected result: Course saved and visible in Courses list; selectable when creating Modules.
- Actual result: Course created (user reported). Please confirm the exact displayed course name and code as shown in the Courses list, and whether the status remained `Draft` after saving.



**Last updated:** 2026-07-08

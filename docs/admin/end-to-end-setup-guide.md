# ILS — End-to-End Setup Guide

This guide provides a complete workflow for setting up a new academic year, course, and curriculum. Intended for Admins, Curriculum Designers, and Teachers.

## Phase 1 — One-time Setup (Admin)

### Step 1 — Create an Institution
- Go to: **Institutions** → New
- Fields: Name, code, country, logo

### Step 2 — Create a Campus
- Go to: **Campuses** → New
- Fields: Name, code, city, link to institution

### Step 3 — Create Academic Periods
- Go to: **Periods** → New
- Create the academic year first (type: Year), then child periods (type: Period)
- Example: Academic Year 2026-2027 → Period-1, Period-2, Period-3, Period-4
- Set school weeks on each period (actual teaching weeks, excluding holidays)

## Phase 2 — Build the Course

### Step 4 — Create a Course
- Go to: **Courses** → New Course
- Fields: Full Name, Code, Level (MBO/HBO), Duration, Description, Status, Credits (ECTS), Course Color
- Link to Partner Institutions if needed
- Save

### Step 5 — Create Modules
- Go to: **Modules** → New Module
- Fields: Module Name, Module Code, Course, Planned Weeks (drives schedule), Level, Description
- Add Themes, Objectives, Weekly Structure, Assessment breakdown (weights must total 100%)
- Repeat for every module in the course
- **Planned Weeks is critical** — this drives the Gantt bar width in the student schedule

### Step 6 — Create Assignments (for each module)
- Go to: **Assignments** → New Assignment
- Fields: Title, Description, Instructions, Points Possible, Due Date, Submission Type
- Link Rubrics if grading criteria are needed
- Set status to Published when ready for students

### Step 7 — Create Quizzes (for each module, optional)
- Go to: **Quizzes** → New Quiz
- Add questions: MCQ (set correct answer!) or Open/Essay
- MCQ quizzes auto-grade on submit — only works if correct answer is set on every question

## Phase 3 — Design the Curriculum

### Step 8 — Open the Curriculum Composer
- Go to: **Curriculum Composer** → select the course

### Step 9 — Build the Period Structure (Step 2 in Composer)
- Create the hierarchy: Year-1 → Period-1, Period-2, Period-3, Period-4
- The period names must match the calendar periods exactly (e.g., "Period-1") so scheduling syncs correctly
- Or apply a template if one exists

### Step 10 — Assign Modules to Periods (Step 3 in Composer)
- Drag modules from the library into the correct period
- Set Start Week (week within that period, 1 = first school week)
- The "Also assign to active classes?" checkbox is checked by default — leave it checked if the class already exists, uncheck if you want to assign manually later
- Modules from other courses can be added here (cross-course sharing)

## Phase 4 — Set Up the Class

### Step 11 — Create a Class
- Go to: **Classes** → New Class (or use Step 4 inside the Curriculum Composer)
- Fields: Name (e.g., WIL-ISE1A - Year-1 BOL4), Code, Period (link to the academic year period), Campus, Enrollment Type
- Link to Course

### Step 12 — Assign Modules to the Class
- Go to: **My Classes** → [class name] (Teacher Class page)
- The curriculum blueprint suggests modules from the course structure
- Add modules one by one or accept suggestions
- Assign a teacher to each module
- Save
- **Note:** If you used the "Also assign to active classes?" checkbox in Step 10, modules are already here. This step is for review and teacher assignment only.

### Step 13 — Enroll Students
- Go to: **Classes** → [class name] (Class Detail page)
- In the Students panel, search for students by name or student number
- Select them and click Enroll N selected
- Set Enrollment Type per student if needed (BOL, BBL, etc.)
- Save Changes

## Phase 5 — Student Experience

### What the student sees after login:

#### Curriculum Tab
- Select their course from the dropdown
- Modules grouped by Academic Year → Period (collapsible)
- Each module shows its assignments with submission status and scores
- Quiz scores shown as X.X / 10

#### Schedule Tab
- Gantt chart grouped by Academic Year → Period
- Each period shows exactly its school weeks (not more)
- Modules shown as colored bars starting at their week_from
- If a module overflows into the next period, it shows › in the first period and ‹ continued in the next
- Clicking a bar jumps to that module in the Curriculum tab

---

## Key Rules to Remember

| Rule | Why |
|------|-----|
| course_structure = pedagogy layer | What the designer planned |
| course_timeline = scheduling layer | When it actually runs |
| class_modules = delivery layer | What each class teaches |
| These three are NOT auto-synced | Each class can deviate from the curriculum design |
| planned_weeks on the module | Controls Gantt bar width |
| school_weeks on the period | Controls Gantt column count |
| correct_answer must be set on MCQ questions | Otherwise quiz auto-grades as 0 |
| Removing a module from the Composer removes it from the student view | But NOT from class_modules — the class still "has" the module |

---

# Session Summary — 2026-05-28 (Technical/Developer Reference)

## Bug Fixes
- Quiz grading page now shows all quizzes; MCQ-only quizzes are labeled “Auto-graded.”
- Fixed duplicate students in grading (now only latest submission per student is shown).
- Quiz scores in student curriculum now display correctly (shows latest attempt per module item).

## Major Architecture: `course_timeline` (Migration 0075)
- **course_structure**: Pedagogy (Composer UI — module ordering, grouping, hierarchy)
- **course_timeline**: Scheduling (when modules run — academic_period_id, study_year, week_from)
- Added `school_weeks` to `academic_periods`.
- Created 4 real calendar periods under Academic Year 2026-2027 with Dutch academic calendar dates.
- Populated `course_timeline` from existing curriculum data.

## Student Schedule Tab — Full Rebuild
- Academic years are collapsible headers.
- Each period shows only its own school weeks.
- Modules spanning periods are visually continued (›/‹ bars).
- Empty periods are shown for overflow display.

## Curriculum Composer → `course_timeline` Sync
- All Composer changes (move, delete) update `course_timeline`.
- Removing a module from Composer removes it from the student view.

## Cross-Course Module Sharing
- Modules from other courses can be added to a curriculum via the Composer.
- “Also assign to active classes?” checkbox: checked = assign to all active classes, unchecked = design only.

## Architecture Decision: Three-Layer Delivery Model
- **Design**: `course_structure` / `course_timeline` (curriculum designer)
- **Offer**: `course_module_offerings` (future, Phase 4+)
- **Deliver**: `class_modules` (what each class actually teaches)
- The “assign to active classes” checkbox is a temporary bridge; future versions will use `course_module_offerings` for flexible delivery.
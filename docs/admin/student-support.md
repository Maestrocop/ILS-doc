# Student Support Module — Session Summary (June 2026)

## Authentication

- **institution_id added to JWT** — login now looks up `Campus.institution_id` and embeds it in the token + response body. Progression review definitions filtered by institution on API level.

## Student Advisor Assignment (#194)

- **New table**: `student_advisors` (migration 0096) — `student_id`, `user_id`, `advisor_type`, `class_id` (optional scope), `is_primary`, `start_date`, `end_date`
- **Advisor types**: mentor, counselor, career_advisor, internship_coach
- **Bulk assignment** — assign an advisor to all enrolled students in a class in one click; skips students already assigned for that type
- **Page**: `Student Advisors` — collapsible class groups, shows advisor badges per group header, active-only by default with history toggle
- **Access**: admin-only (management task)

### Who this is for

- Primary audience: Student Support officers / counselors, SLB / mentor coordinators, program coordinators.
- Secondary audience: Teachers (for referral flows) and BSA teams.

### Quick practical note — No SQL, no migrations

Support staff do NOT need to know migration numbers, raw SQL table names, or internal IDs. The technical note above (`student_advisors`, migration 0096) is for reference only. What matters to you is how to use the UI and which fields affect your day-to-day work (see below).

### What Support needs to know (practical fields)

- `student_id`: which student the assignment applies to — use the student card in the UI.
- `user_id`: which staff member is the advisor — shows as the advisor contact in the UI.
- `advisor_type`: role (mentor, counselor, career_advisor, internship_coach) — determines routing and responsibilities.
- `class_id` (optional): scope of the assignment when relevant to a cohort or class.
- `is_primary`: primary advisor flag — primary receives first-line alerts and owns the caseload.
- `start_date` / `end_date`: assignment validity — used for rotations and historical reporting.

### Typical support actions

- Find a student's current primary advisor on the student card.
- View your active caseload (filter by `is_primary` and active date range).
- Bulk-assign advisors to a class via the `Student Advisors` page; the system skips existing assignments for that advisor type.
- Schedule handovers by setting `start_date`/`end_date` when reassigning.


## SLB Dashboard

- **Wired to student_advisors** — "At Risk" section now shows only the logged-in user's assigned students, not all at-risk students school-wide
- **"My role" column** added — shows mentor/counselor/etc. per student

## Progression Reviews

- **"+ Start Review" button** hidden for teachers — coordinator + admin only (UI + backend enforced)
- **"Owner" renamed to "Assigned to"** — clearer label
- **Auto-fill on create** — when a review is created, `review_owner_id` is auto-populated from `student_advisors` (primary advisor first, fallback to any active advisor for that student+class)

## Access matrix (Student Support)

Feature | Admin | Coordinator | Teacher
---|---:|---:|---:
BSA Dashboard | ✅ | ✅ | ❌
SLB Dashboard | ✅ | ✅ | ✅
Progression Reviews (view) | ✅ | ✅ | ✅
Progression Reviews (create) | ✅ | ✅ | ❌
Student Advisors | ✅ | ❌ | ❌

---

Notes: This document records observed behavior from `ILS-dev`. No changes were made to `ILS-dev` as part of this documentation update.

## SLB (Student Loopbaan Begeleider) — Architecture & Feature Summary

### What is an SLB?

An SLB (Student Career Counselor / Mentor) is a support staff member responsible for guiding individual students through their academic journey. The role exists under different names depending on school type. Key design decision: SLB is a responsibility, not a hard role — a teacher can act as SLB for some students while a dedicated SLB may have no teaching duties. The system models this via the `student_advisors` assignment table.

### Data model

#### `student_advisors` table
The foundation of the SLB system. Decouples who has permission (roles) from who is responsible (assignments).

```
student_advisors
	id            — primary key
	student_id    → users(id)       — the student
	user_id       → users(id)       — the advisor (teacher, SLB, coordinator)
	advisor_type  — mentor | counselor | career_advisor | internship_coach
	class_id      → classes(id)     — NULL = permanent, set = scoped to one year/class
	is_primary    — true = main contact for this student
	start_date    — when responsibility started (audit trail)
	end_date      — when it ended; NULL = still active
	created_at / updated_at
```

Why `class_id` is optional: a student can have a permanent counselor across all years (`NULL`) and a class-specific mentor that changes each year (set).

Why `start_date` / `end_date`: enables audit questions like “who was the student's mentor when the BSA decision was made?”

Why `is_primary`: many screens need one main contact; this avoids ad-hoc logic elsewhere.

### Advisor types
Type | Meaning | Reused by
---|---|---
`mentor` | Academic mentor, day-to-day contact | Progression Reviews, cockpit
`counselor` | Wellbeing / personal guidance | Future: wellbeing module
`career_advisor` | Career planning, graduation | Future: career guidance
`internship_coach` | Internship supervision support | Future: internship module

### Features built

#### Student Advisors page (`/admin/student-advisors`)

- Access: admin only (coordinator + teacher see results, not the management page)
- Bulk assign: select class → see enrolled student count → pick advisor + type → one click assigns all students
- Skip logic: students who already have that advisor type in that class are skipped (shown in amber warning)
- Individual override: edit any assignment per student
- Collapsible class groups: grouped by class, all collapsed by default — scales to 600+ students
- Active-only by default: ended assignments hidden; "Show history" toggle reveals them
- Soft delete: "Unassign" sets `end_date = today` — assignment disappears from active list but stays in history

#### SLB Dashboard (`/admin/slb-dashboard`)

- Access: teacher + coordinator + admin
- My Open Reviews: reviews where the logged-in user is `slb_id` or `review_owner_id`, status not decided
- My Students — Action Required: students assigned to me (via `student_advisors`) with avg score

### Access matrix (summary)

Feature | Admin | Coordinator | Teacher
---|---:|---:|---:
Student Advisors (manage) | ✅ | ❌ | ❌
SLB Dashboard | ✅ | ✅ | ✅
Progression Reviews (view) | ✅ | ✅ | ✅
Progression Reviews (create) | ✅ | ✅ | ❌

### What this unlocks (not yet built)

Feature | Depends on
---|---
SLB Dashboard → "all my students" panel (not just at-risk) | `student_advisors`
Cockpit intelligence → show primary advisor name | `student_advisors`
Internship module → internship_coach assignment | `student_advisors`
Wellbeing / career guidance | advisor_type = `counselor` / `career_advisor`
Graduation guidance | `career_advisor` type
History queries like "who was responsible during internship?" | `start_date` / `end_date`

===================
Note: Do not touch `ILS-dev`; this page documents observed implementation only.

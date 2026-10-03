# Grading & Rubrics

## Recent changes (June 2026)

- A student-centric grading view and module grouping have been added to make it easier to review and grade work per student and per module.
- Rubric behavior: save-button state and multi-student grading UX were improved to avoid data loss and keep the grader informed when changes are pending.
- Returned submissions are now reflected consistently in the UI when a grader marks work as returned.
## Why this matters

Grading is the core step that turns student work into mastery evidence.
When teachers score rubric criteria, the system can show better class-level and student-level progress.
# Grading & Rubrics

The grading page is the teacher grading cockpit. It presents a three-column workflow: assignment list, student list, and rubric panel.

## What the grading page does

The page guides teachers through three steps:

1. Choose a class.
2. Choose an assignment.
3. Choose a student and score their work.

The workflow is divided into three areas:

- **Assignments** — work items for the class.
- **Student submissions** — student list and submission status.
- **Rubric grading** — score each criterion.

## How the rubric table works
## How the rubric table works

Each rubric row is a criterion and each column is a rating option.
Click a rating to mark that criterion for the student.

- selected ratings show which score is chosen
- the total score updates as ratings are chosen
- a progress indicator shows how many criteria are scored

[Rubric Screenshot: criterion rows with selected ratings and progress bar]

## Draft and finalize grading

The grading cockpit supports both simple and advanced assessment modes.
In advanced mode, teachers may be able to save drafts before finalizing.

- Use **Save Draft** when grading is still in progress.
- Use **Finalize** when the score is complete and ready to be recorded.

In simple mode, there is one **Save Grade** button, and it writes the final score immediately (submission becomes `graded`) — the student is notified right away that their work has been graded.

### Return and reset workflows
The grading cockpit also supports returning a graded submission to the student for revision, and resetting a finalized grade.

- **Return for revision** — sends the submission back to the student (status becomes `returned`, score cleared to pending) with your feedback, and notifies the student to review and resubmit
- **Reset grade** — clear a grade to allow re-grading

Both **Save Grade** and **Return for revision** trigger a student notification — they differ in whether the work is considered done (`graded`) or needs more work (`returned`).

## Grade status badges

The page shows status badges such as:

- graded
- pending
- returned
- not graded

These labels help teachers understand submission readiness.

## AI grading assistance ("Ibn Rushd")

The rubric panel has a **"✦ Suggest with AI"** button. It reads the assignment's own text (description, objectives, instructions, case study), the rubric, the student's submitted files, and — as of October 2026 — any **Resources you've linked to the assignment** (e.g. an escalation procedure or reference sheet), so it can check the student's work against real reference material, not just judge internal consistency.

- Only PDF, plain text, JPG, and PNG are readable by the AI — for both student submissions and linked Resources. Word/Excel/PowerPoint files are silently skipped; convert them to PDF first if you want them considered.
- The AI's suggestions (per-criterion rating + justification, plus overall feedback) are never saved automatically — you review and apply them, or ignore them and grade manually. Nothing changes until you click Save/Finalize yourself.
- If a linked Resource or submission file can't be read, you'll see a note listing which files were skipped.

## Resubmission clears the previous grade

If a student resubmits after you've already graded their work, the old score and rubric selections are cleared automatically (not left showing stale results against the new file) — the submission goes back to "pending" so you know it genuinely needs a fresh look.

## Outcome alignment

Each rubric criterion may show the linked outcome or learning target.
This helps teachers see how each score maps to outcome mastery and classroom intelligence.

## Teacher workflow

1. Select your class.
2. Pick the assignment with student submissions.
3. Open a student from the list.
4. Select a rating for each rubric criterion.
5. Add grader notes if needed.
6. Save or finalize the grade.

## Step-by-step Grading Guide (detailed)

### 1 — Open Grading

1. From the Teacher menu select **Grading** or open `/teacher/grading`
2. Choose the class you are grading from the left-hand class selector
3. Select the assignment you want to grade from the assignments list

### 2 — Review Submissions

1. The student list shows submission status (submitted, late, not submitted)
2. Click a student to view their submission files and previous feedback
3. If a file fails to open, download and inspect it locally
4. The header shows **"Last submitted"** — the actual time the student's file was uploaded, not when you last graded it, so it stays accurate even after grading

### 3 — Apply the Rubric

1. The rubric panel displays criteria as rows and rating options as columns
2. Click the rating cell for each criterion to select it (ratings highlight when chosen)
3. The total score updates automatically as you select ratings
4. Add grader comments in the feedback box if required

### 4 — Save, Draft, Finalize

- **Save Draft** — stores your current rubric selections without making the score final. Use when you plan to continue later.
- **Finalize** — locks the grade (subject to institution policy) and notifies the student if notifications are enabled.
- **Return for Revision** — if the student needs to rework the submission, return it with comments.

### 5 — Bulk Grading (if enabled)

1. Use multi-select in the student list to choose multiple students
2. Apply the same rubric rating to all selected students for criteria where the same rating applies
3. Save or finalize each student's grade as required

### 6 — Viewing Outcome Alignment

1. Each rubric criterion may display a linked outcome code
2. Click the outcome code to open the Outcome page (teacher view) and see its mastery threshold and description

### 7 — Troubleshooting

- "My rubric changes didn't save": check network connectivity and the unsaved-changes indicator. Save again or try Save Draft.
- "I lost progress": drafts are saved per-assignment; if drafts are missing, contact your admin.
- "Student can't see feedback": ensure you finalized the grade or returned the submission with feedback; otherwise, drafts stay private.

---

**Last updated:** 2026-10-03

## Practical teacher notes

- Prioritize submissions that are ungraded or marked pending.
- Use the progress bar to confirm you have scored all rubric criteria.
- Existing scores appear when a student has already been graded.
- When available, save drafts and finalize after review.
- After grading, check the Heatmap and Student Cockpit to see how mastery updates.

## Why this matters

Grading is the core step that turns student work into mastery evidence.
When teachers score rubric criteria, the system can show better class-level and student-level progress.

# Quizzes

Use the Quizzes page to create and manage quiz assessments for students.

## What you can do

Go to **Quizzes** in the admin menu to:

- View all quizzes
- Create new quizzes
- Edit quiz content, questions, and scoring settings
- Delete or archive quizzes

## Attempt and return behavior

Quiz attempts are controlled by the `Attempts allowed` setting on the quiz form. Teachers can increase this value to give all students additional retries.

Returning a student’s submission is a separate, per-student action:

- A returned submission is sent back to the student with feedback.
- The returned attempt does not block the student from starting the next attempt when it is available.
- Attempt numbers always increment across returns (`Attempt 1`, `Attempt 2`, `Attempt 3`), so the retry history remains clear.
- Unlimited quizzes (`attempts_allowed = -1`) remain unrestricted.
- The return action is gated: teachers can only return a submission if the student still has attempts remaining. This prevents a teacher from returning a submission on a one-attempt quiz that was genuinely exhausted.

For site-wide extra retries, the teacher should increase `Attempts allowed` on the quiz form. For a single student who needs another chance, the teacher can return that student’s submission instead.

### Practical retry logic

- On auto-graded quizzes, students can start again immediately whenever attempts remain.
- On rubric/open-question quizzes, a student with status `submitted` waits for the teacher to grade; no retry button is shown yet.
- Once the teacher grades and/or returns the submission, retries become available if attempts remain.
- If the student still has attempts left but the quiz is pending grading, the UI should show a clear notice explaining that retry is available after teacher review.

## Workflow

1. Open Quizzes
2. Review existing quizzes or create a new one
3. Edit quiz content, question order, and outcome tagging
4. Save changes and confirm the quiz is available to students

## Quizzes vs Assignments

- Quizzes are for MCQ / auto-graded assessments
- Pure MCQ quizzes use the quiz score as outcome evidence (no rubric needed)
- Rubrics are only required for essay or short-answer questions
- Mixed quizzes can combine auto-graded scores and rubric-scored open questions

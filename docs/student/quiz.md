# Student Quiz

The Student Quiz page displays a quiz item for the learner.

## What the page does

This page shows the quiz instructions, questions, and submission flow for the student.

## Page behavior

The page typically supports:

- displaying quiz instructions and timing information
- presenting quiz questions and answer inputs
- submitting quiz responses
- showing quiz status and feedback after completion

## Quiz evidence for learning outcomes

Quiz results contribute to your learning outcome scores, just like assignment work does.
## Attempts and returns

Students may have multiple quiz attempts depending on the quiz settings.

- `Attempts allowed` is set on the quiz form and determines how many retries are available.
- A returned submission does not consume an attempt slot, so the student can try again even if the quiz attempts setting was unchanged.
- Attempt numbers always increase (`Attempt 1`, `Attempt 2`, `Attempt 3`), even across returned submissions, preserving a clear attempt history.
- Quizzes with `attempts_allowed = -1` are unlimited and remain unrestricted.

If the teacher wants every student to have more tries, they should increase `Attempts allowed` on the quiz. If a single student needs one more try, the teacher can return that student’s submission instead.

### Retry behavior for rubric quizzes

For quizzes with open questions or rubric scoring, the retry flow is:

- **submitted** — student is waiting for the teacher to grade. No retry button appears yet.
- **graded + attempts left** — the student can retry if the quiz has extra allowed attempts.
- **returned** — the teacher explicitly sent it back, and the student can retry immediately.
- **attempts_allowed = -1** — unlimited retries are still allowed and are not blocked by this flow.

If a student has attempts remaining but the quiz is still submitted, the system shows a clear message like "Awaiting grading — retry available after teacher reviews" so the student understands why they cannot start again yet.

## Student workflow

1. Open the quiz from your course or assignments
2. Review the quiz instructions and any time limits
3. Complete the questions and submit the quiz.
4. Review any immediate feedback or result summary.

## Notes

- This page is part of the student-facing assessment experience.
- It is accessed directly from the curriculum or assignment navigation.

# Teacher FAQ

This FAQ answers common teacher questions about using the ILS analytics system.

## What is the difference between mastery and a grade?

Mastery is a normalized learning outcome score.
A grade is a raw assignment score or rubric total.
Mastery is designed to compare performance across different assignments and outcomes,
while grade values are tied to a specific assignment or rubric.

## What is Classroom Intelligence?

Classroom Intelligence is the interpretive report that follows the Heatmap.
It uses the same class mastery data plus campus reporting rules to turn that data into cohort health signals, confidence labels, and suggested intervention actions.
See the [Classroom Intelligence page](classroom-intelligence.md) for detailed guidance.

## Why does the Heatmap sometimes say there is insufficient graded data?

The app only makes strong cohort recommendations when enough students have graded outcome evidence.
If few students are graded, the system waits for more data before reporting patterns or re-teach signals.

## How should I use trend confidence?

Trend confidence helps determine whether a direction signal is reliable.
High confidence means the movement is supported by sufficient snapshot history.
Low confidence means the signal should be interpreted cautiously.

## Why is an outcome at risk?

An outcome is at risk when the mastery score is below the campus success threshold.
The Student Cockpit, Heatmap, and Classroom Intelligence use this threshold to identify students and outcomes that need attention.

## What if a student has mixed performance?

Use the Heatmap, Student Cockpit, and Classroom Intelligence together.
Look for patterns across outcomes, whether the student has ungraded work, and whether the class signal recommends targeted action.

## How do I know when to reteach?

Reteach when many students show low mastery on the same outcome,
especially if the Heatmap row is consistently low and Classroom Intelligence shows threshold pressure or re-teach eligibility.
If the report recommends a formative reassessment, use that as the first follow-up.

## What does "Re-teach decision: Required" mean?

It means the class has crossed the campus re-teach policy threshold.
In practical terms, progression should pause and the weak outcomes should be re-taught.

Rule of thumb:

- compare the class below-threshold percentage to the campus re-teach threshold
- if class below-threshold percentage is higher, the decision is `Required`

Example:

- re-teach threshold: `40%`
- class below threshold: `93%` (`14/15` students)
- result: `Required`

In this case, first verify grading completeness, then re-teach the weakest outcomes and reassess before resuming normal pacing.

See also: [Re-teach Decision Playbook](reteach-decision-playbook.md) for the complete decision and action flow.

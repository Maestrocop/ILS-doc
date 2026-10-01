# Heatmap

The Heatmap is the classroom matrix for outcome mastery.

[Heatmap Screenshot: student vs outcome mastery matrix with filters visible]

## What the Heatmap shows

- **Outcomes** across the top.
- **Students** down the side.
- **Scores** inside each cell.
- **Pending grading indicators** for submitted work that has not yet been graded.
- **Trend arrows** when there is enough recent evidence.

## Data the Heatmap uses (non-technical)

The Heatmap shows student scores, pending submissions, and campus reporting thresholds (such as success and re-teach levels). These are loaded automatically for the class you select — you do not need to configure APIs or technical settings to use the page.

## Page controls and filters

### Class selector

Choose a class first.
Until a class is selected, the page prompts for class selection.

### Module selector

If the class is associated with multiple modules, a module selector appears.
Use it to focus the Heatmap on one module’s outcomes.
If only one module is available, the page uses that module by default.

### Search and status filters

Use the search box to find students by name or student number.
Use the status filter to isolate students by:

- `All statuses`
- `Not graded`
- `Graded`
- `Needs revision`

### Outcome grouping

The page may group outcomes by category to help scan high-level skill clusters before drilling into individual outcomes.

### Reporting rule badges

The page displays campus reporting thresholds such as:
- success threshold
- inactivity cutoff (`low_activity_days`)
- re-teach warning threshold

These badges help interpret whether the current class has enough graded evidence.

## What the colors mean

The Heatmap uses color and score values to show mastery:

- **Red** — low mastery
- **Amber** — developing mastery
- **Yellow / Gold** — progressing
- **Green** — strong mastery
- **Gray** — no score available

If a cell has a pending submission and no final score, you will see a pending indicator instead of a final score.

## What a heatmap cell can tell you

- A colored number is the student’s current mastery score for that outcome.
- A trend arrow shows whether the outcome is improving, declining, or stable.
- A pending icon means the student has submitted work but it still needs grading.
- Click a pending cell to open grading or navigate to the student submission detail.

[Cell Screenshot: pending icon and trend arrow in the heatmap]

## Re-teach and graded coverage

The Heatmap also signals whether the class has enough graded evidence to support a recommendation.

- If graded coverage is low, the page warns that the class is not ready for a reliable decision.
- If enough data exists, the page will show whether re-teach is recommended.

## Practical teacher actions

- Scan for outcomes with many red or amber cells.
- Use filters to isolate students with pending or revision work.
- Click pending cells to grade and refresh the class picture.
- Use module selection to focus on a single teaching unit.
- Open Classroom Intelligence for narrative guidance once the class has enough graded evidence.

## Why this matters

The Heatmap helps you see what is happening across the class.
It highlights outcome mastery, grading gaps, and whether the class is ready for a broader teaching decision.
Use it together with Student Cockpit and Classroom Intelligence for the clearest picture.

## Recent changes (June 2026)

- Reporting thresholds are now configurable per campus; you may see slightly different success/re-teach guidance when viewing classes on different campuses.
- The Heatmap UI now highlights weak outcome clusters more clearly and links directly to Classroom Intelligence for narrative guidance when sufficient graded evidence exists.
- If a cell shows a pending indicator, click to open grading and refresh the view after saving to update the class picture.


**Last updated:** 2026-07-08

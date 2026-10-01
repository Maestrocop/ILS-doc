# Outcomes — Teacher Guide

This page explains how teachers read and work with learning outcomes in ILS: what the labels mean, how to duplicate an outcome, and how CSV import affects teachers.

## Reading an outcome card

When viewing an outcome, you will see:

- **Code** — short identifier (e.g. `LO-IBDK.1`) shown at the top
- **Mastery** — the mastery threshold in points (e.g. "Mastery: 2 pts")
  - If no threshold is set, this line is hidden
  - Meaning: the number of points students must reach to be considered "mastered" on this outcome
- **Title & Description** — what the outcome means in practice
- **Context labels** — curriculum area (e.g. Strategic Management), level (e.g. HBO)
- **Trend / Average** — current class-level trend (if available)

Why this matters: mastery thresholds are a target teachers use to judge whether students have achieved the intended skill. The UI now shows a clear label so there is no guesswork.

## Evidence History (note for teachers)

The Evidence History section formerly showed placeholder data (for example "1 students") and could be misleading. It has been removed until we can display real, reliable `student_outcome_snapshots` data.

If you need to see which students have evidence for an outcome today, use the Grading or Submissions pages where rubric-linked evidence is shown per assignment.

## Duplicating an outcome (recommended workflow)

Why duplicate? You usually duplicate an outcome when you want to create a similar one but modify the wording, mastery threshold, or assignment mapping.

Workflow:
1. On the **Outcomes** page, locate the outcome you want to copy
2. Click **Duplicate**
3. The system opens the new copy directly in **Edit mode** (this saves a click)
4. Edit the code, friendly name, and description to make the copy meaningful
5. Save the new outcome and assign it where needed

Notes:
- The copy is given a temporary name (e.g. `LO-IBDK.1-copy`) — rename it immediately
- Opening the copy in Edit mode prevents confusing identical outcomes from appearing in the list

## CSV import — what teachers should know

Administrators and coordinators can import outcomes in bulk via CSV. Teachers should be aware of the following:

- The import is intended for adding many outcomes at once (from a curriculum or standards list)
- Supported columns in Step 1: `code`, `friendly_name`, `description`, `level`, `type`, `mastery_threshold`, `calculation_method`
- **Mastery levels** (the point-to-label mapping such as Exemplary=3, Proficient=2) are not imported in Step 1. Mastery levels are defined globally by the institution and must be set in **Settings → Mastery Levels**
- The import preview shows a subset of fields (code, name, description, level, type). More advanced fields (e.g. `calculation_method`) are imported even if not shown in the preview

If your admin imports outcomes and you expect a different mastery scale, ask them to either set the mastery levels first or to update the imported outcomes after import.

## Quick Troubleshooting

- "I duplicated an outcome but it isn't visible": ensure you saved the copy and that it's not archived. Check the outcome list filters (Active / Archived).
- "Mastery label missing": the outcome has no threshold set; open Edit and set `Mastery threshold` if required.
- "Evidence history missing": this is intentional — check Grading/Submissions for evidence tied to assignments.

---

**Last updated:** 2026-07-03

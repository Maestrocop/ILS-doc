# Module Composer

The Module Composer provides a workspace for building and editing individual modules.

## What you can do

Go to **Module Composer** in the admin menu to:

- Create and edit module content
- Select module outcomes and teaching methods
- Review module metadata and schedule settings
- Set up item locking and prerequisites
- Save module composition changes

## Workflow

1. Open Module Composer
2. Create a new module or open an existing module
3. Add module descriptions, outcomes, and instructional details
4. Configure item locks and prerequisites if needed
5. Save the updated module composition

## How Module Composer differs

- Module Composer focuses on module-level curriculum design
- Distinct from the main course editor
- Complementary to Course Composer (which handles course-level structure)
 
## Item locking & prerequisites

Module Composer supports locking and prerequisites on per-item rows (assignments, quizzes). This controls when the next item becomes available to students based on the selected condition.

### What each condition means

- **Submitted** — unlocks the next item as soon as the student clicks *Submit*. Use when you only require the student to attempt the work before moving on.
- **Graded** — the teacher must grade the submission before the next item unlocks. Use when instructor feedback is essential before proceeding.
- **Passed (≥55%)** — same as *Graded*, but the graded score must be 55% or higher. If the student scores below the threshold they must resubmit (if attempts allow) and pass to unlock the next item. The 55% threshold is fixed for now.

### When it unlocks (quick reference)

| Condition | When it unlocks |
|-----------|-----------------|
| Submitted | Student clicks Submit |
| Graded    | Teacher grades the submission |
| Passed    | Teacher grades and score ≥ 55% |

### UI behavior and example

Each item row is rendered as a single inline row; the lock/unlock toggle and the prerequisite dropdown appear inline with the item. The first item in a sequence has no lock icon. Example:

[1]  [A]  Assignment One     draft                    ⋮    ← no lock (first item)  
[2]  [Q]  Quiz Two           published   🔓            ⋮    ← unlocked, click to lock  
[3]  [A]  Assignment Three   draft       🔒 submitted  ⋮    ← locked, with dropdown  

Click 🔓 to lock, click 🔒 to unlock, and change the dropdown when locked to switch between `submitted` / `graded` / `passed`. The next item unlocks according to the selected condition.

### Hover help for teachers

Browser `<option>` elements are inconsistent for hover tooltips across platforms. The Module Composer shows a short explanation by placing a dynamic `title` on the `<select>` itself (the tooltip reflects the currently selected option and updates when the teacher changes it). Hover the dropdown to see the brief explanation for the selected prerequisite.

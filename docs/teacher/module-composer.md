# Module Composer

This guide explains how teachers create and structure a Module (the central hub for lessons, resources, and assignments).

## Purpose

The Module Composer lets you define the sequence and resources for a module, attach learning outcomes, and add assignments.

## Steps

1. Open **Modules** from the Teacher menu.
2. Click **Create Module** to start a new module or click an existing module to edit.
3. Fill the module header: title, code, start/end dates, and visibility.
4. Use the **Weeks & Topics** area to add sections. Each section can contain:
   - Lessons (sessions)
   - Resources (files, links)
   - Activities (quizzes, assignments)
5. Add assignments via **Add assignment** — link them to this module so reporting and progress maps work.
6. Link outcomes and themes using the **Outcomes** panel; choose mastery thresholds where applicable.
7. Save the module. Use **Publish** to make it visible to students depending on your release policy.

## Best practices

- Keep modules focused (3–6 weeks) for better progress tracking.
- Use outcome links liberally — they power heatmaps and reporting.
- Attach rubrics to assignments at creation time for smoother grading.

## Troubleshooting

- "I can't add an assignment": confirm you have permission and the module has a valid `start_date`.
- "Outcomes not visible": outcomes are global; search by code or use filters.

**Last updated:** 2026-07-04
# Module Composer — Sequencing & Locks

The Module Composer lets you build ordered learning sequences in a module and set rules for when students can access each item.

## What you can do

- **Add items** (assignments, quizzes, projects) to a module
- **Reorder items** — drag to arrange the sequence
- **Set locks** — hide items until the previous item is completed, graded, or passed
- **Lock conditions** — choose when an item unlocks (submit, grade, or pass)

## How to add items

1. Open **Module Composer**
2. Select the **module** you want to build
3. Click **Add Item**
4. Choose the type: **Assignment**, **Quiz**, or **Project**
5. Select the content to add
6. Save

The item appears at the end of the module.

## How to reorder items

1. Open the module
2. Use **drag and drop** to rearrange items, OR
3. Use the **up/down arrows** to move items one position at a time
4. Save

The sequence determines the order students see items.

## How to lock items

Locking an item means students can't access it until they complete a prior item.

### Setting a lock

1. Open the module
2. Click an item to edit it
3. Toggle **"Locked by previous"** ON
4. Choose the unlock condition:
   - **Submit** — unlock when the previous item is submitted
   - **Grade** — unlock when the previous item is graded
   - **Pass** — unlock when the previous item is graded and meets the pass threshold (usually 55%)
5. Save

### What students see

- **Locked items** appear as "unavailable" or disabled in the student view
- **Unlocked items** become active once the condition is met
- The message tells students what they need to do to unlock the next item

## Use cases

### Sequential mastery

1. Lesson (assignment) → students submit
2. Practice quiz → unlocks after lesson is submitted
3. Graded assessment → unlocks after quiz is graded and passed

### Guided learning paths

Build a module where each item must be completed before the next appears, ensuring students follow the intended sequence.

### Conditional progression

Use the **"pass"** condition to ensure students who didn't understand the material must review before moving on.

## Tips

- Start simple: use Submit for initial practice
- Use **Pass** conditions only for critical knowledge gates
- Always test locks with a student account to confirm behavior
- Communicate the sequence clearly to students (add descriptions explaining why items are locked)

## What students need to know

In the student view, locked items show a message like:
- "Available after you submit [previous item]"
- "Available after [previous item] is graded"
- "Available after you pass [previous item]"

This helps students understand what they need to do next.

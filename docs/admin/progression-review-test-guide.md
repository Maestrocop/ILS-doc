# Progression Review — End-to-End Test Guide

## Prerequisites
Before starting, confirm you have:

- At least one **Class** with enrolled students
- At least one **Progression Review Definition** configured (Settings → Progression Review Types). If none exist, create one (e.g. "BSA Review", type: BSA)
- You are logged in as **admin** or **coordinator**

---

## Step 1 — Open the Progression Reviews page
Navigate to **Admin → Progression Reviews** (`/admin/progression-reviews`)

**What to verify:**

- The page loads with 5 KPI cards at the top: Total, Pending, In Progress, Decided, and **Overdue**
- Overdue card is grey (0) until you create a past-due review

---

## Step 2 — Create a new review
Click **+ New Review** (top right).

In the modal, fill in:

FieldWhat to selectReview TypeThe definition you have (e.g. "BSA Review")ClassAny class with studentsStudentAny enrolled studentDue Date**Yesterday's date** — this will trigger the overdue detectionClick **Create Review**. You should be redirected automatically to the review detail page.

**What to verify:**

- Review was created and detail page opens
- Status shows **Pending**

---

## Step 3 — Work the review
On the detail page you will see panels on the right side. Test each one:

**a) Add a note**
Type something in the Notes panel → Save. Verify it persists if you refresh.

**b) Log an event** (if visible)
Select an event type, add a note → Save.

**c) Set a recommendation** (if the definition has a decision policy)
Work through any required checklist items before the decision becomes available.

---

## Step 4 — Record a decision
In the **Decision Panel**:

1. Set **Status** to `In Progress`, save — verify the KPI card on the list page updates
2. Set **Decision** to `Continue` → save. Verify the decision card appears with green styling.
3. Come back and change Decision to **`Exit`**

When Exit is selected:

- A **Primary Reason** dropdown must appear (required — marked with red asterisk)
- **Contributing Factors** checkboxes must appear (optional)

Select:

- Primary Reason: `Wrong Program Choice`
- Contributing Factors: check `Academic Performance` + `Motivation`

Click **Save Decision**.

**What to verify:**

- Save is blocked if Exit is chosen but no reason selected — error message appears
- After save, the decision card shows: decision label, primary reason, factor pills
- Status on the list page changes to **Decided**

---

## Step 5 — Verify overdue detection
Go back to **Progression Reviews** list.

**What to verify:**

- The **Overdue** KPI card shows **1** (red background)
- Clicking it filters the list to show only the overdue review
- The overdue row has a red tint and an **Overdue** badge on the due date
- The filter tag "Overdue only" appears in the filter bar with an X to clear it

---

## Step 6 — Verify the data feeds the hub
Go to **Intelligence Hub → Programs tab**.

**What to verify:**

- The student you marked as Exit now appears in the **Dropout Rate by Program** table
- Their program shows `total_exits: 1`

---

## What to report back
For each step tell me:

1. Did it work as described?
2. If not — what did you see instead?
3. Any fields missing, buttons not working, or unexpected errors

------------------------

## Policy enforcement note (observed behavior)

When you attempt to save an Exit decision and the system blocks it, the UI will explain what's missing. Example enforcement checklist:

RequirementStatusMeaning
Warning on record✓Done — someone logged a warning action
Intervention documented!Missing — no intervention action logged yet
Student acknowledgment!Missing — student hasn't signed/acknowledged the warning

To unlock the Exit decision, ensure both are recorded:

1. Go to the **Actions** section → add an action of type `Intervention`
2. Go to the **Audit Trail** section → log an event of type `Warning Acknowledged`

Once both are logged, return to the Decision panel → select Exit → Save Decision — it should succeed.

This enforces the BSA process: an institution cannot formally exit a student without documented evidence that they were warned and acknowledged it.

---

## Verified results (example)

- The test passed completely: Final Decision: Exit, Decided 6/6/2026 — the decision succeeded after all requirements were met.

Issues noted during verification:

1. The Decision panel remains editable after saving — it should be read-only or hidden once a decision is recorded.
2. Contributing factors on the decided card display mixed content and need clearer separation/labels.

---

*Do not touch ILS-dev.*

---

## Passing-but-Outcome-Gap (note)

The Progression Review side-panel should surface "Passing but outcome gap" alerts (when a student passes overall but has at least one outcome below the diagnostic threshold). Include a one-click path from the side-panel to add a remediation plan for the flagged outcome. This side-panel entry is currently missing from the implementation and should be included in future updates.


**Last updated:** 2026-07-08

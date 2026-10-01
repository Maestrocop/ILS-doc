# Periods Playbook — Step-by-step

Practical step-by-step guide for admins to apply a period template to a course and link modules to a class.

## Prerequisites

- You are logged in as an admin or coordinator
- You know the course and class you will configure

## Step A — Apply a Period Template to the Course

1. Open Curriculum Composer for your course
2. Proceed to **Step 2 — Periods**
3. Click **Apply template** and choose the structure you want (example: `Year-1 Periods N-4` for a 4-block structure)
4. Click **+ Add** next to the chosen template and confirm
5. Verify the new periods appear in the Composer

## Step B — Add Modules to the Course

1. In the Composer proceed to **Step 3 — Modules**
2. Add the modules you need from the library using search or the module selector
3. Confirm module order and durations align with the period blocks

## Step C — Link Modules to Your Class

1. Proceed to **Step 4 — Classes**
2. Select your class from the list
3. Assign the module set to the class and save
4. Review the complete configuration
5. Save the Composer settings

## Quick-Add Alternative (Class Setup)

1. Go to **Classes** and select your class
2. In the **Curriculum** tab click **+ Add module manually**
3. Add modules one-by-one
4. Click **Save**

## Verification Checklist

- Class curriculum tab shows the assigned modules
- Periods for the course are visible in Composer
- Module order matches your intended sequence

## Multi-Year Programmes (Study Years)

A single programme (e.g. "ICT system engineer BBL") can span multiple years (Year 1, Year 2, Year 3) as one continuous curriculum, instead of creating a separate programme per year. This matters because several cohorts of the same programme run concurrently — e.g. a Year-1 class and a Year-2 class, both active in the same real school year.

**How it works:**
- Every module in the Composer's Modules step has a **Study Year** field (1, 2, 3, ...). This is what actually controls delivery — assigning a class to the programme with a given Study Year only delivers that year's modules to it, never another year's, regardless of how many years' worth of content the programme already contains.
- Periods are just for scheduling/display, not delivery. A common convention: number periods continuously across the whole programme (Periode 1-4 = Year 1, Periode 5-8 = Year 2, Periode 9-12 = Year 3). The Modules step groups its tabs by parsing this numbering automatically.
- Classes also carry a Study Year field (set when assigning them to the programme, editable afterward), used to decide which modules they receive.

**Rolling into a new school year:** create brand-new period rows with the new year's real dates — **never edit an existing period's start/end date in place.** This keeps historical reporting reliable (e.g. comparing a specific student's performance period-by-period, even years later) — reusing/overwriting a period's dates would make it stop reliably representing what a past cohort actually experienced. See [ILS-dev#399](https://github.com/Maestrocop/ILS-dev/issues/399) for the full reasoning and the still-open follow-up (linking individual submissions to a specific period for quarter-level reporting — not built yet; year-level comparison via Study Year is already possible today).

**Last updated:** 2026-09-20

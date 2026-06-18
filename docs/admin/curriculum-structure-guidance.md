# Curriculum Structure Guidance — Clear names & separation of concerns

This guidance explains the language and UX changes recommended to prevent confusion between curriculum structure (what) and the academic calendar (when). Read-only: no changes will be made to `ILS-dev`.

## Problem summary

The word "Period" is currently used for two different concepts:

- Academic Period — a dated calendar range (Semester 1, Period 3)
- Curriculum Period — a curriculum grouping or block (Foundation, Theme A)

Using the same term guarantees confusion for designers, admins and teachers.

---

## Key principle

Separate the WHAT (curriculum structure) from the WHEN (academic calendar). Keep distinct, clear names in the UI.

---

## Recommendations (exact wording to use)

- Curriculum Composer: rename top-level concept from `Periods` → `Structure`.
- Replace `+ Add Period` with `+ Add Block` (or `+ Add Theme` / `+ Add Phase`).
- Add helper text near the composer controls:

  "Organise modules into curriculum blocks. Blocks help structure the learning journey and group related modules. Blocks do not define dates or schedules. Scheduling is managed separately through the Academic Calendar and Timetable."

---

## Why this helps (short)

- Designers will no longer accidentally create undated calendar entries when they mean to group modules.
- Admins will understand that scheduling belongs to the Academic Calendar UI.
- Timetables and session generation become deterministic because curriculum structure is not overloaded with date semantics.

---

## Example UX copy

Composer header:

```
Curriculum Structure

Organise modules into curriculum blocks or themes. Blocks do not define dates.
```

Composer action button:

```
⚡ Apply Template   + Add Block
```

Slot label inside Composer:

```
Foundation Block — Week from: 1 — Planned weeks: 8
```

---

## Future-proofing

If in future a block needs to map to multiple academic periods (e.g., Foundation Block runs in Period-1 + Period-2), this mapping should live in a separate assignment step or in the Timetable generator; do not change the curriculum structure when the schedule changes.

---

If you want, I will add a short visual mockup (PNG or ASCII) demonstrating the revised Composer UI and the helper text. I will not modify `ILS-dev` — only update docs in `ILS-doc`.

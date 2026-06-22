# Process Engine (Phase 5) — Epic #127

Status: Partially implemented in current ILS-dev (module-item sequencing and prerequisite unlock rules confirmed)

## Purpose

The Process Engine layer governs progression rules between learning items so students unlock the next item only after meeting the required condition on the previous item.

## Who should use it

- Teachers: define progression rules for class pacing.
- Curriculum designers: encode sequence prerequisites in module flow.
- Students: follow guided progression where access depends on prior completion outcomes.
- Coordinators: validate that progression rules are consistent across modules.

## Current implementation status

### Confirmed functionality

- Module item sequencing with lock/unlock rules
- Unlock conditions: submitted, graded, or passed (score >= 55%)
- Lock controls available in Module Composer
- Student unlock logic based on submission status and scores

### Not yet implemented

- Dedicated process engine for workflows beyond module sequencing
- Generic workflow or state machine UI
- Advanced process definition and instance management

## Unlock conditions

| Condition label (UI) | Stored value | Unlocks when |
|---|---|---|
| Submitted | `submit` | Student has a submission with status in `submitted`, `graded`, or `returned` |
| Graded | `grade` | Student has a submission with status `graded` |
| Passed (>=55%) | `pass` | Student has graded submission and score >= 55 |

The first item in a module sequence has no previous-item dependency and is not lock-gated by this rule.

## Step-by-step tasks (teacher/designer)

1. Open Module Composer
2. Build the sequence of assignments and quizzes for your module
3. For each item after the first, enable a lock if progression should be gated
4. Choose the unlock rule: submitted, graded, or passed
5. Save and verify the sequence order and lock settings

## Expected outcomes and example

Example sequence:

| Position | Item | Lock setting | Result |
|---|---|---|---|
| 1 | Quiz A | none | Always available |
| 2 | Assignment B | locked, `grade` | Opens after Quiz A is graded |
| 3 | Quiz C | locked, `pass` | Opens after Assignment B is graded and >= 55 |

Student-facing behavior: the next item remains locked until the condition is satisfied on the previous item.

## UI navigation labels

- Access Module Composer from admin tools
- Sequence controls: lock toggle and unlock condition dropdown
- Unlock options: submitted, graded, passed

## Troubleshooting

- Item never unlocks: verify previous item has a matching submission status/score for the selected rule.
- Wrong rule behavior: confirm stored `unlock_on` value (`submit`, `grade`, `pass`) matches intended UI option.
- First item lock confusion: first item is not governed by previous-item lock rule.

## Implementation references

This page describes the Phase 5 Process Engine feature roadmap and current module-sequencing implementation status.

---

_Last updated: Process Engine implementation audit (Epic #127)_

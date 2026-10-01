# Internship Lifecycle: Triangular Actor Model

## The core insight

Internship management is not about forms, assignments, or checklists. It's about **process + timeline + multiple actors working together**.

ILS models internships as a state machine with three independent assessors:
- **Student** (applies, logs, uploads work)
- **Teacher** (monitors, intervenes, evaluates)
- **Company Supervisor** (validates real-world performance independently)

No LMS has this triangular model. This is the competitive edge.

---

## What makes this different

### Traditional LMS approach
- Internship = assignment with a due date
- Supervisor feedback = optional comment field
- No visibility into real-world activity
- Single-actor assessment (teacher only)

### ILS approach
- Internship = process with state machine (Preparation → Placement → Execution → Evaluation)
- Supervisor is a first-class actor with independent assessment
- Real-time activity logs feed intelligence layer
- Multi-actor feedback reveals institutional insights

---

## The lifecycle (state machine)

```
PREPARATION
├─ CV Created
├─ Motivation Letter
├─ Applications Sent
└─ Interview

PLACEMENT
├─ Accepted
└─ Internship Confirmed

EXECUTION
├─ Internship Started
├─ Weekly Activities Logged
├─ Assignments / Projects Completed
└─ Supervisor Feedback

EVALUATION
├─ Final Assessment
├─ Reflection
└─ Completed
```

Each state transition can be guarded by:
- Student actions (apply, log activity)
- Teacher actions (approve, intervene)
- Supervisor actions (confirm, give feedback)
- System rules (minimum activity threshold, dates)

---

## Triangular assessment: The real power

Three independent perspectives on the same performance:

| Actor | View | Input | Outcome |
|-------|------|-------|---------|
| Student | My work, feedback from both | Activities, reflections | Completion record |
| Teacher | Class-level oversight | Monitoring, interventions | Student mastery signal |
| Supervisor | Real-world work quality | Performance rating, presence | Outcome evidence |

### What you get from this

**Grading gap detection**: Supervisor gives 85% → Teacher gives 60%
- Signal: student performs better in real world than in class
- Or: supervisor is lenient (calibration needed)
- Or: real-world context amplifies performance

**Early intervention**: Student applied to 2 companies in 3 weeks
- System flags low application activity
- Teacher contacts student before placement
- Early intervention prevents failure

**Institutional intelligence**: Weekly activity + supervisor scores + teacher assessment
- Reveals gaps between curriculum and real-world expectations
- Identifies best-performing internship partners
- Tracks outcomes through external context

---

## How it connects to ILS architecture

The internship is **not a module**. It's a separate entity that:

1. **Uses the Process Engine** (#127) for lifecycle state management
2. **Links to modules and outcomes** (for intelligence connection)
3. **Captures external feedback** (supervisor assessment)
4. **Feeds activity data** into the intelligence layer

```
Internship
├─ owns the process states
├─ links to Outcomes (intelligence)
├─ links to Modules (curriculum context)
└─ receives Company Supervisor feedback
    └─ feeds Snapshot engine for mastery tracking
```

---

## The hardest technical problem

**Supervisor authentication**: Company supervisors don't have system accounts.

**Recommended approach**: Token-based link
- Supervisor gets a unique, shareable URL
- No account creation or login required
- Validates and gives feedback directly
- Highest adoption rate

This single decision determines whether supervisors actually use the system. If it's too complex, they won't.

---

## Why schools will adopt this

Not for modules. Schools already have curriculum tools.

**Schools will adopt you for internship control + visibility.**

- Internship coordination is currently email + spreadsheet
- No tool integrates student, teacher, and supervisor
- ILS becomes the single source of truth
- Intelligence layer proves student success in real-world context

---

## Campaign angles

### For institutions
- *"Turn internship programs into data"*
- *"Coordinate with company partners without email"*
- *"Know the gap between classroom and workplace"*

### For student recruiting
- *"See how your students succeed in real companies"*
- *"Early warning system for at-risk internships"*
- *"Industry feedback built into your curriculum"*

---

## MVP features required

- [ ] Internship entity with process states
- [ ] Student, teacher, and supervisor views (independent)
- [ ] Weekly activity log capture
- [ ] Supervisor feedback (token-based, no account)
- [ ] Outcome linking and mastery tracking
- [ ] Grading gap detection and reporting
- [ ] Early-warning activity flags

---

## Why this is killer

Internship management is a **real, unmet market need** that institutions will pay for, and it's something no LMS currently offers.

The triangular actor model + real-world intelligence layer = undefendable competitive advantage.


**Last updated:** 2026-07-08

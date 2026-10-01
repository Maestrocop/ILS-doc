# Internship Lifecycle Management: Triangular Actor Model

## Core differentiator
- ILS treats internships as a **process with multiple actors**, not just assignments.
- Traditional LMS platforms view internships as forms, documents, or assignments with due dates.
- ILS introduces the **triangular actor model**: student, teacher, and company supervisor all participate in assessment and feedback.

## The triangular actor model

Three independent perspectives on internship performance:

### Student
- Applies to companies
- Logs activities weekly
- Uploads work and reflections
- Receives feedback from both supervisor and teacher

### Teacher
- Monitors progress across placements
- Can intervene early if activity is low
- Evaluates student performance
- Receives supervisor feedback

### Company Supervisor
- Validates real-world work quality
- Provides independent performance ratings
- Confirms presence, engagement, and deliverables
- Operates outside the traditional classroom

## The internship lifecycle (state machine)

Not a form. A process:

1. **Preparation** — CV created, motivation letter, applications sent, interviews conducted
2. **Placement** — Accepted, internship confirmed, start date set
3. **Execution** — Started, activities logged weekly, assignments/projects completed, feedback received
4. **Evaluation** — Final assessment, reflection, completion, outcome mastery recorded

## Why no LMS has this

Traditional systems:
- Treat internship as another assignment or checklist
- Have no real-world actor (supervisor) with independent voice
- Can't detect disagreement between teacher and supervisor
- Miss recency and engagement signals from activity logs

ILS difference:
- Models internship as its own entity using the **Process Engine**
- Links to outcomes and modules for **intelligence connection**
- Captures bilateral assessment: supervisor + teacher independently
- Detects institutional calibration gaps (supervisor 85% vs teacher 60%)

## Intelligence layer: real-world signals

Weekly activity logs + supervisor feedback = new data source for outcome mastery:

- **Recency/engagement**: frequency and timeliness of activity logs
- **Real-world performance**: supervisor scores as outcome evidence
- **Gap detection**: teacher vs supervisor disagreement signals performance mismatch
- **Early risk**: low application activity before placement starts

Example:
```
Student applied to 2 companies in 3 weeks
→ Low activity flag
→ System alerts teacher
→ Teacher intervenes early
→ Placement success improves
```

## Critical technical decision: Supervisor authentication

Hard problem: Company supervisors don't have system accounts.

Recommended approach:
- **Token-based link** — supervisor gets unique URL, no login required
- Validates/gives feedback directly
- Lowest friction, highest adoption

Avoid: complexity that prevents supervisor participation.

## Campaign positioning

### For schools
- "Track real-world learning with company partners"
- "First LMS with built-in supervisor feedback loop"
- "Detect student performance gaps before they matter"

### For institutions
- "Turn internship programs into data"
- "Coordinate with external partners without extra tools"
- "Identify and improve teaching-workplace alignment"

## Why schools will adopt this

Not for modules. For **internship control + visibility**.

- Schools already struggle with internship coordination
- Current tools are email + spreadsheet
- ILS becomes the single source of truth for all stakeholders
- Intelligence layer justifies the investment

## Key features to build (MVP)

1. Internship entity with process states (prep → placement → execution → evaluation)
2. Three-actor dashboard (student, teacher, supervisor views)
3. Weekly activity log capture
4. Independent supervisor assessment (without full account)
5. Outcome linking and mastery tracking
6. Grading gap detection and reporting

## Why this is a killer feature

Internship management is a **real, unmet market need** with institutional value and a clear competitive moat.

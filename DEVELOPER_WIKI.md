# ILS Developer Wiki

## ⛔ DOCUMENTATION REPO ONLY ⛔

This file is in `ILS-doc`. The assistant may ONLY edit files in `ILS-doc`.

**The assistant is FORBIDDEN from editing any file in `ILS-dev`.**

If you see this message, you are in the correct directory (`ILS-doc`). Do not cross into `ILS-dev`.


markdown
# ILS Developer Wiki

This is the developer reference documentation for the ILS system.

## 1. System Overview

The ILS (Intelligent Learning System) is a modular learning platform with:
- **Vertical hierarchy**: Institution → Campus → Course → Module → Assignment → Class
- **Horizontal intelligence layer**: Outcomes, rubrics, criteria, trends, heatmaps

## 2. Technology Stack

### Backend
- Node.js with Express
- Sequelize ORM
- PostgreSQL database
- Migration-based schema management

### Frontend  
- React 18
- Vite build tool
- Tailwind CSS
- MkDocs for documentation

## 3. Data Model

### Core Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| Institution | Top-level organization | id, name |
| Campus | Physical location | id, name, institution_id |
| Course | Academic course | id, name, campus_id |
| Module | Course unit | id, title, course_id |
| Assignment | Graded work | id, title, module_id |
| Class | Student cohort | id, name, assignment_id |

### Intelligence Entities

| Entity | Purpose |
|--------|---------|
| Outcome | Measurable learning objective (0-10 mastery scale) |
| Rubric | Scoring criteria for assignments |
| Criteria | Individual rubric row items |
| Theme | Higher-level outcome grouping |
| Snapshot | Historical mastery score record |

### Junction Tables
- `module_outcomes` - Links modules to outcomes
- `assignment_outcomes` - Links assignments to outcomes  
- `assignment_rubrics` - Links assignments to rubrics
- `module_themes` - Links modules to themes

## 4. API Endpoints

### Core Routes
/api/institutions
/api/campuses
/api/courses
/api/modules
/api/assignments
/api/themes
/api/outcomes
/api/assessment-types

text

### Module Endpoints
- `GET /api/modules` - List all modules
- `GET /api/modules/:id` - Get single module
- `POST /api/modules` - Create module
- `PUT /api/modules/:id` - Update module
- `DELETE /api/modules/:id` - Delete module
- `GET /api/modules/:id/items` - Get module structure items

### Assignment Endpoints
- `GET /api/assignments` - List assignments
- `GET /api/assignments/:id` - Get single assignment
- `POST /api/assignments` - Create assignment
- `PUT /api/assignments/:id` - Update assignment
- `DELETE /api/assignments/:id` - Delete assignment

## 5. Key Workflows

### Grading → Snapshot → Trend

1. Teacher grades submission using rubric criteria
2. Ratings saved to `submission_ratings` table
3. Backend aggregates to outcome mastery scores (0-10)
4. `student_outcome_snapshots` created/updated
5. Trend calculation compares snapshots:
   - `trend_direction`: Up/Down/Flat
   - `trend_confidence`: High/Medium/Low
   - `delta`: Score change amount

### Teacher Cockpit Dashboard

The cockpit displays:
- At-risk students (mastery below threshold)
- Outcome heatmap grid
- Trend indicators per student/outcome
- Intervention recommendations

## 6. Development Setup

### Prerequisites
- Node.js 18+
- PostgreSQL 14+
- Git

### Backend Setup
```bash
cd ILS-dev/backend
cp .env.example .env
# Edit .env with your database credentials
npm install
npm run create-db
npm run migrate
npm run dev  # Runs on port 4000
Frontend Setup
bash
cd ILS-dev/frontend
npm install
npm run dev  # Runs on port 5173
Documentation Server
bash
cd ILS-doc
pip install mkdocs-material
mkdocs serve  # Runs on port 8000
7. Database Migrations
All schema changes must be SQL migrations in backend/migrations/

Migrations must be idempotent (can run multiple times safely)

sequelize.sync() is disabled in all environments

Soft deletes use deleted_at timestamp

8. Testing
bash
# Backend tests
cd ILS-dev/backend
npm run test:reporting

# Frontend tests  
cd ILS-dev/frontend
npm run test:playwright
9. Known Limitations
BigInt values are serialized as strings in API responses (JSON limitation)

No cross-ownership in vertical hierarchy (entities belong to exactly one parent)

Horizontal entities (outcomes, themes) are global, not owned by modules/courses

No new tables without approval (stabilization phase)

10. Troubleshooting
Database connection errors
Verify PostgreSQL is running

Check .env DATABASE_URL

Run npm run create-db to ensure database exists

Migration failures
Check migration order (by timestamp)

Verify no duplicate migration names

Check for destructive operations without rollback

API returns BigInt as string
This is expected behavior

Frontend handles conversion automatically

Related Documentation
Teacher Guide - UI workflows for teachers

Student Guide - Student assignment submission

Admin Guide - System administration

API Reference - Complete API documentation

text

---

## File 3: `C:\Users\0102663\Projects\bim\ILS-dev\.github\agents\speckit.docs.agent.md`

**Purpose:** Minimal agent instruction (just the role, no analysis)

```markdown
# Documentation Agent

## Role
Documentation scribe for ILS project.

## Responsibility
Read `ILS-dev` codebase and write/update documentation in `ILS-doc`.

## Rules

### Allowed Actions
- Read any file in `ILS-dev` (routes, models, components, pages)
- Create or edit Markdown files in `ILS-doc/docs/`
- Run `mkdocs build --strict` to validate documentation

### Forbidden Actions
- Suggesting code changes to `ILS-dev`
- Analyzing architecture or proposing improvements
- Creating "missing features" documentation
- Giving development advice
- Acting as a product manager or architect

## Behavior Pattern

For each documentation request:

1. **State intent:** "I will document [specific file/section] from ILS-dev"
2. **Read source:** Examine the actual code in ILS-dev
3. **Write documentation:** Update the corresponding file in ILS-doc
4. **Validate:** Run `mkdocs build --strict` if applicable
5. **Stop:** No additional comments, suggestions, or analysis

## Reset Mechanism

If the agent begins giving advice or analysis instead of documenting, the user will say:

**"DOCUMENT ONLY"**

Upon hearing this phrase, the agent must immediately:
- Stop any analysis or suggestions
- Respond with: "Documenting. What should I work on?"
- Resume documentation-only behavior

## Context Files

Documentation tasks are tracked in:
- `ILS-doc/Active-ILS-doc.md` - Task checklist
- GitHub Projects board: `https://github.com/users/Maestrocop/projects/5`

## Examples

### Correct behavior
User: "Document the grading workflow"
Agent: "I will document the grading workflow from ILS-dev/backend/routes/grading.js"
[Reads file, updates ILS-doc/docs/teacher/grading.md]
Agent: "Done. docs/teacher/grading.md updated."

### Incorrect behavior (should never happen)
User: "Document the grading workflow"  
Agent: "You should also consider adding a notification system for..." ← WRONG

## Remember
Document what EXISTS. Nothing else.

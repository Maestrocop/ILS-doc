# Active ILS-doc

This file tracks the active documentation project for `C:\Users\0102663\Projects\bim\ILS-doc`.

## Project context

- **Project root:** `C:\Users\0102663\Projects\bim\ILS-doc`
- **Current branch:** `docs/phase-a-structure`
- **Documentation tool:** MkDocs with Material theme
- **Project board:** GitHub Projects 5 (`https://github.com/users/Maestrocop/projects/5`)

## What we are building

We are building a developer-focused documentation site for the Intelligent Learning System (ILS) platform.
This docs project is separate from the application repository and is intended to capture the system design, setup, and core workflows.

### Scope

- Developer reference and architecture decisions for ILS
- Data model relationships and key entities
- Setup and local development environment guidance
- Workflow descriptions for grading, snapshots, trends, and teacher intelligence
- Concept pages for ILS-specific analytics and interpretation

## Source application

- **Primary source app:** `C:\Users\0102663\Projects\bim\ILS-dev`
- **Source app type:** Node.js backend + React frontend application
- **Source repo purpose:** the active ILS application under development, not the docs themselves

## Audience

- Primary: current and future maintainers of the ILS platform
- Secondary: technical stakeholders who need to understand architecture, data flows, and developer setup
- Not targeted at end users or non-technical learners at this phase

## Project objectives

1. Establish a clean, separate documentation repo for ILS that does not modify `ILS-dev`.
2. Build a Phase A developer reference site using MkDocs Material.
3. Document the ILS architecture, data model, developer environment, and key analytics workflows.
4. Create an explicit project structure for Phase A and Phase B content in GitHub Project 5.
5. Keep docs developer-focused; end-user manuals will come later when the product is stable.

## Current priorities

- Phase A: developer reference and documentation structure
- Phase B: concept-level explanation of ILS analytics features

## Working rules

- Do not change keys or code in `ILS-dev` unless explicitly requested.
- Keep documentation changes within `ILS-doc` only.
- Use `docs/phase-a-structure` for active Phase A authoring.
- Keep the docs repo self-contained with its own branch, files, and project tracking.

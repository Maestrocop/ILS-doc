
# ILS Developer Guide

> **Welcome to the ILS Developer Guide**

This guide is your authoritative reference for developing, extending, and maintaining the Intelligent Learning System (ILS). All content is based strictly on the live implementation in `ILS-dev`.

---

## Guide Structure

The Developer Guide is organized into clear, focused categories. Use the sidebar to navigate, or explore the summaries below:

!!! info "Guide Categories"
		**Architecture & Model**  
		System architecture, backend/frontend split, domain separation, and the data model (entities, junction tables, snapshots).

		**Curriculum Design**  
		Course, class, and module authoring, outcome links, and teaching method support.

		**Developer Workflows**  
		Grading, snapshot, heatmap, and cockpit lifecycles. API reference for backend routes and high-value endpoints.

		**Setup & Support**  
		Local preview, application setup, troubleshooting, and release validation.

		**Decisions & Terms**  
		Technical decisions, rationale, and a glossary of ILS terminology.

---

## Quick Navigation

<table>
	<tr>
		<td><strong>Architecture & Model</strong></td>
		<td>
			<ul>
				<li>Architecture: system principles, backend/frontend split</li>
				<li>Data Model: entities, junctions, snapshots</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td><strong>Curriculum Design</strong></td>
		<td>
			<ul>
				<li>Institutions: top-level organization and admin flow</li>
				<li>Campuses: campus list and reporting rule support</li>
				<li>Course Creation: authoring, metadata</li>
				<li>Classes: session setup, module assignments, enrollment</li>
				<li>Themes: learning themes and module linking</li>
				<li>Outcomes: learning goals, mastery, and calculation rules</li>
				<li>Module Creation: authoring, outcomes, teaching methods</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td><strong>Developer Workflows</strong></td>
		<td>
			<ul>
				<li>Workflows: grading, reporting, intelligence</li>
				<li>Users: account management, roles, and campus assignment</li>
				<li>Heatmap: classroom mastery matrix and drilldown evidence</li>
				<li>Reporting Rules: campus intelligence thresholds and save validation</li>
				<li>Teacher Roster: teacher class roster, student activity, and cockpit links</li>
				<li>Student Cockpit: action list for at-risk students</li>
				<li>Classroom Intelligence: report interpretation and cohort patterns</li>
				<li>Grading Cockpit: submission scoring and rubric evaluation</li>
				<li>Assignments: assignment authoring and rubric linking</li>
				<li>Rubrics: rubric authoring, criteria, and rating management</li>
				<li>Criteria Bank: cross-rubric criterion visibility and outcome links</li>
				<li>Mapping Matrix: assignment–outcome coverage audit</li>
				<li>API Reference: backend routes, requests</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td><strong>Setup & Support</strong></td>
		<td>
			<ul>
				<li>Setup: local preview, app reference</li>
				<li>Troubleshooting: build/runtime support</li>
				<li>Release Plan: validation, release prep</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td><strong>Decisions & Terms</strong></td>
		<td>
			<ul>
				<li>Decisions: design rationale</li>
				<li>Glossary: ILS terminology</li>
			</ul>
		</td>
	</tr>
</table>

---

## Repo Boundaries

This documentation covers only the docs repository (`ILS-doc`). The application code is in `ILS-dev`.

- **ILS-doc**: documentation site content, navigation, and authoring
- **ILS-dev**: application source code, backend, frontend, and migrations

> Only make documentation changes in `ILS-doc` unless explicitly asked to modify `ILS-dev`.


**Last updated:** 2026-07-08

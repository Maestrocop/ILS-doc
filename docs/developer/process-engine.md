# Process Engine (Developer)

The repository includes a process-engine foundation used to implement lifecycle flows such as internships and placement transitions. This is a developer-facing area of the docs.

## Recent changes (June 2026)

- A generic state-machine foundation was added (migrations and models) to power lifecycle flows such as internships. Developer readers can inspect `backend/migrations/*process_engine*.sql` and models `ProcessDefinition`, `ProcessInstance`, `ProcessState`, and `ProcessTransition` for implementation details.


**Last updated:** 2026-07-08

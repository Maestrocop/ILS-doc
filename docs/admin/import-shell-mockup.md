# ImportShell UI mockup

This page shows a recommended UI flow and wireframe notes for the ImportShell.

Pages / Panels:
- Upload panel: drag-and-drop, file type, file metadata, progress bar
- Mapping panel: detected headers, target fields, sample values, save mapping
- Validation panel: summary counts, rule breakdown, row-level badges
- Preview panel: paginated table, inline edit for simple fixes, skip/retry actions
- Confirm panel: import mode (create/merge/replace), scheduling option
- Report panel: downloadable CSV/JSON with row statuses

Wireframe notes (desktop):
- Left column: step list with icons and progress
- Main column: contextual content per step
- Right column: help & examples (link to `admin/templates-guidelines.md`)

Accessibility notes:
- Keyboard-navigable mapping table
- Clear ARIA roles for progress and error regions

Interaction examples:
- Detect common date formats and show parsing preview
- Highlight rows with errors in red and allow row-level note

Link to templates: see `admin/templates-guidelines.md` for downloadable CSVs.

**Last updated:** 2026-07-07

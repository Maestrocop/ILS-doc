# Release Plan

This page describes the process for publishing the ILS documentation site.

## Goals

- Keep the docs repo stable and reviewable.
- Publish Phase A and Phase B content through controlled commits and PRs.
- Verify the site locally before any public release.

## Release steps

1. Finalize docs content in `ILS-doc`.
2. Run `mkdocs build` from the repository root.
3. Review the generated site under `site/` and confirm the navigation and pages work.
4. Commit changes to the current branch (`docs/phase-a-structure`).
5. Open a pull request for review.
6. After approval, merge to the main docs branch or release branch.

## Quality checks

- Ensure `mkdocs build` completes without errors.
- Confirm the Developer Guide menu and concept pages are accessible.
- Validate that no `ILS-dev` source files are modified.
- Keep the `Active-ILS-doc.md` plan in sync with actual progress.

## Release outputs

- A merged docs branch that contains the current site structure.
- A built site that can be previewed locally.
- A plan for Phase B concept expansion and release readiness.

## Future release considerations

- Add diagrams and architecture visuals once core content is stable.
- Add API examples and troubleshooting notes before a broader release.
- Document the publish target and deployment mechanism when the hosting path is finalized.


**Last updated:** 2026-07-08

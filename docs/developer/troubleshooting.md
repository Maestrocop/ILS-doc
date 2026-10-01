# Troubleshooting

This page captures common issues when working on the ILS documentation site and how to resolve them.

## Local preview

If the site is not loading correctly:

- Confirm you are running `mkdocs serve` from `C:\Users\0102663\Projects\bim\ILS-doc`.
- Do not run the server from `ILS-dev`.
- Use `http://127.0.0.1:8000/` as the local preview URL.
- If the browser returns a 404, refresh the page and confirm the path is `ILS-doc` not `ILS-dev`.

## Build issues

Run:

```powershell
mkdocs build
```

If there is a build failure:

- Check `mkdocs.yml` for invalid nav syntax.
- Confirm referenced markdown files exist in `docs/`.
- Verify the file paths use forward slashes and are relative to the repo root.

## Navigation problems

If a page is missing from the site:

- Ensure the page is included in `mkdocs.yml` under `nav:`.
- Confirm the file exists at the path referenced in the nav entry.
- If a page is intentionally not in the menu, the build will still include it unless it is absent from `docs/`.

## Phase B content review

- Keep Phase A separate from Phase B.
- Add new concept and release plan pages only inside `ILS-doc`.
- Do not modify `ILS-dev` when updating docs.

## Common mistakes to avoid

- Editing `ILS-dev` source files when the task is docs-only.
- Running `mkdocs` from the wrong folder.
- Leaving navigation entries out of `mkdocs.yml`.
- Forgetting to build after changes.

## Helpful commands

```powershell
cd C:\Users\0102663\Projects\bim\ILS-doc
mkdocs build
mkdocs serve --dev-addr 127.0.0.1:8000
```


**Last updated:** 2026-07-08

# Translation & Localization — Documentation Guidelines

Purpose
- Provide a single reference for translating ILS documentation (no code changes). Use this when preparing, executing, or reviewing translations for other languages.

Scope
- Covers documentation only: Markdown content, captions, tooltips, image alt text, and UI copy shown in docs. Does NOT cover application code, resource files, or runtime translations.

Canonical source
- English is the canonical source. All translations are derived artifacts and must reference the English source when in doubt.

Options (pick one)
- Option A — Per-language folders (simple): create `docs/<lang>/...` with translated Markdown mirroring the English structure.
- Option B — i18n pipeline (preferred for scale): use a translation workflow with PO/JSON files, a translation memory, and CI-driven per-locale builds (e.g., `mkdocs-static-i18n`).

Preparation
- Create a glossary of product terms and approved translations before translating (see `glossary.md` below).
- Mark non-translatable blocks clearly: code, API payloads, SQL, and configuration.
- Extract strings for translators: headings, captions, link text, alt text, and tooltips.

Translation workflow
1. Export strings (PO/JSON) or copy files into `docs/<lang>/`.
2. Translate (machine-assisted or human). Use a translation memory (TM) to ensure consistency.
3. Reviewer: linguistic review + product/SME review.
4. Merge into repository under a language branch or PR.
5. CI builds site per-locale and runs link checks.

Quality checks
- Automated: `mkdocs build --strict` per-locale; linkcheck; spellcheck (optional).
- Manual: review links, anchors, screenshots, and data examples.

Deployment
- Deploy per-locale under `/nl/`, `/es/` or subdomains. Provide a language switcher in the site header linking to equivalent pages.

Best practices
- Keep screenshots minimal; prefer captions that can be translated instead of localized images.
- Never translate code blocks or API examples; include a translator note when necessary.
- Version translations: when templates or CSV headers change, bump template version and notify translators.

Files to add to repo
- `docs/internal/glossary.md` — product term list and approved translations (create before translating).
- `i18n/README.md` — chosen tooling and CI steps (optional).

Immediate next step (I can do now)
- Create `docs/internal/glossary.md` with starter terms and an empty `locales/` folder example, or scaffold `locales/nl/` with one translated sample page.

**Last updated:** 2026-07-08

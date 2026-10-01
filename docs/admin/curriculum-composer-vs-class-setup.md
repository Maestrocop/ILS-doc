# Curriculum Composer V2 vs Class Setup (Admin guidance)

This page explains the difference between the Curriculum Composer V2 (wizard) and the simpler Class Setup page, and documents recommended admin practice.

## Summary

- Curriculum Composer V2 (`/admin/curriculum-v2/:courseId`) is the canonical, structured wizard for initial curriculum setup. Flow: Course → Periods → Modules → Classes → Review.
- Class Setup (`/admin/classes/:classId`) is an operational view intended for quick fixes and one-off adjustments ("Quick Add"). It is not a replacement for the Composer.

## Why both exist

- Composer V2 enforces the full curriculum model and is recommended for first-time setup and bulk assignments.
- Class Setup exists to let admins add or remove a single module or change assigned teachers without re-running the full wizard.

## Recommended admin policy

1. Use Curriculum Composer V2 for initial curriculum configuration and when adding or reordering multiple modules.
2. Use Class Setup only for operational fixes (add/remove one module, reassign teacher) after the curriculum is already in place.
3. Add a short in-UI tip on the Class Setup page that points admins to the Composer for full configuration (proposal below).

## How to link the 10 HRD modules to Class 18

Option A — Canonical (recommended): Curriculum Composer V2

1. Open: `/admin/curriculum-v2/<courseId>` (select the relevant course)
2. Proceed to Step 3 — Modules: add modules 12 through 21 (Inleiding Bedrijfskunde → Ondernemen)
3. Proceed to Step 4 — Classes: assign the configured module set to Class 18
4. Review → Save

Option B — Quick Add (when you need a fast operational change)

1. Open: `/admin/classes/18`
2. Curriculum tab → Click **+ Add module manually…**
3. Add modules one-by-one: 12, 13, 14, …, 21
4. Save

## Suggested UI copy (proposal for developers/product)

Add the following note to the top of the Class Setup Curriculum tab:


Include a small link to `/admin/curriculum-v2/` and label the button: **Open Curriculum Composer**.

### Exact in-UI copy and snippet (developer-ready)

Copy (short):

"Tip: For full curriculum setup use the Curriculum Composer → This page is a quick-add for single-module adjustments after setup."

Button label: `Open Curriculum Composer`

Suggested HTML/Tailwind snippet (drop into the top of the Curriculum tab):

<div class="bg-blue-50 border-l-4 border-blue-400 p-3 rounded-md mb-4">
	<div class="flex items-start gap-3">
		<svg class="w-5 h-5 text-blue-500 mt-0.5" fill="currentColor" viewBox="0 0 20 20"><path d="M9 12l2-2 4 4-1 1-3-3-1 1-1-1z"/></svg>
		<div>
			<p class="text-sm text-slate-800">Tip: For full curriculum setup use the <strong>Curriculum Composer</strong>. This page is a quick-add for single-module changes.</p>
			<a href="/admin/curriculum-v2/" class="inline-block mt-2 text-sm text-blue-600 hover:underline">Open Curriculum Composer</a>
		</div>
	</div>
</div>

Developer notes:

- Place the snippet at the top of the Curriculum tab, above the module list.
- Optionally change the link to include the current course id: `/admin/curriculum-v2/${courseId}`.
- Keep the language short and non-judgmental; the snippet should guide, not block.


## Follow-ups for docs

- Add a short note on the Admin Guide index linking to this page.
- Consider adding a one-page quick script for bulk-adding modules (developer/admin utility) — only if the UI is too slow.


**Last updated:** 2026-07-08

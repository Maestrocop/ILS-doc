# In-repo TODOs for ILS-doc

This file tracks small, in-repo tasks related to documentation artifacts (screenshots, images, placeholders).

## Screenshot tasks

- [ ] composer-step2-periods.png — Capture Step 2 (Periods) as described in `docs/admin/curriculum-composer-guide.md` (see capture instructions there).
- [ ] composer-step2-periods@2x.png — High-resolution variant.
- [ ] composer-step3-modules.png — Capture Step 3 (Modules) showing library + "Adding to" indicator + `Assign to classes` pill.
- [ ] composer-step3-modules@2x.png — High-resolution variant.
- [ ] composer-step4-classes.png — Optional: capture Classes list with one class toggled ON.

## Notes

- Place images in `docs/images/` and name them exactly as above.
- After adding images, update `docs/admin/curriculum-composer-guide.md` to remove the placeholder text and insert the image with the relative path `images/<filename>`.
- Use PNG format, crop to ~1200–1366 px width, and provide @2x variants when possible.

## Minimal workflow to add screenshots

1. Capture images per instructions in `docs/admin/curriculum-composer-guide.md`.
2. Save files into `docs/images/`.
3. Edit `docs/admin/curriculum-composer-guide.md` to replace placeholders with image links.
4. Run `mkdocs build --strict` to validate.

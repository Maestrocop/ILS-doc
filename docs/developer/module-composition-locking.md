# Module Composition & Locking API

This page documents the Module composition endpoints that manage ordered module items (assignments, quizzes, projects) and per-item lock rules. All information is a read-only extraction from `ILS-dev/backend/routes/moduleItems.js`.

Base path

- Router mounted at: `GET|POST|PATCH|DELETE /api/modules/:id/items` (router uses `mergeParams` thus `:id` is the module id).

Endpoints

1. GET /api/modules/:id/items
- Purpose: return ordered items for the module (assignments + quizzes).
- Response: JSON array of rows ordered by `position` with these fields (selected columns):
  - `id`, `module_id`, `content_type` (`assignment`|`quiz`|`project`), `content_id`, `position`
  - `title`, `status`, `due_date` (text), `points_possible`, `rubric_total_points`, `quiz_type`, `item_count`
  - `locked_by_previous`, `unlock_on`

Notes:
- The SQL used by the endpoint joins only `assignments` and `quizzes`, and filters out module items whose referenced assignment/quiz row is missing; as a result, `project` content items (accepted by POST) are not returned by this query.

Example response (abridged):

```json
[
  {
    "id": 101,
    "module_id": 12,
    "content_type": "assignment",
    "content_id": 55,
    "position": 10,
    "title": "Research Essay",
    "due_date": "2026-06-01T23:59:00",
    "rubric_total_points": "20",
    "locked_by_previous": true,
    "unlock_on": "grade"
  }
]
```

2. POST /api/modules/:id/items
- Purpose: add a new content item to a module.
- Body: `{ content_type: 'assignment'|'quiz'|'project', content_id: number }` (JSON)
- Behavior:
  - Computes `position` as `COALESCE(MAX(position), -10) + 10` so new items are appended with spacing.
  - `ON CONFLICT (module_id, content_type, content_id) DO NOTHING` — duplicates are detected server-side.
  - Returns `201` with created item, or `409` if item already exists.

Example request:

```json
{ "content_type": "assignment", "content_id": 55 }
```

3. DELETE /api/modules/:id/items/:itemId
- Purpose: remove an item from a module.
- Returns `204` on success, `404` if not found.

4. PATCH /api/modules/:id/items/reorder
- Purpose: bulk update positions for multiple module items.
- Body: `{ items: [{ id: number, position: number }, ...] }` (JSON)
- Behavior: Updates each `module_items.position` inside a DB transaction; returns `{ ok: true }` on success.
- Note: this route is declared before `/:itemId` in the router to avoid the literal `reorder` path being interpreted as an `itemId`.

5. PATCH /api/modules/:id/items/:itemId
- Purpose: update lock settings for a single module item.
- Body: `{ locked_by_previous?: boolean, unlock_on?: 'submit'|'grade'|'pass' }` (JSON)
- Validation: `unlock_on` must be one of `submit`, `grade`, or `pass` if provided.
- Behavior: updates provided fields and `updated_at`, returns the updated item. Returns `400` for invalid inputs or when there are no fields to update, `404` if item not found.

Implementation notes & gotchas

- Position spacing: positions are incremented by 10 on insert to allow later inserts between items without a full reorder.
- `project` content type is accepted by the POST endpoint but the GET listing SQL only returns `assignment` and `quiz` rows — projects won't appear in the GET response until the SQL is extended.
- Reordering is performed inside a transaction, so partial failures roll back.
- Locking semantics:
  - `locked_by_previous` (boolean) — when true, the item is considered locked until the previous item meets the `unlock_on` condition.
  - `unlock_on` (enum) — one of `submit`, `grade`, or `pass` describing which event on the previous item unlocks this one.

Where this is used

- Teacher Module Composer UI (frontend) calls these endpoints to display, add, remove, reorder, and set locks for module items.

References (read-only)

- `ILS-dev/backend/routes/moduleItems.js`


**Last updated:** 2026-07-08

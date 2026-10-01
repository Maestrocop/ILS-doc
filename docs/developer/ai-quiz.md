# AI Quiz APIs

This page documents the AI-assisted quiz generation endpoint implemented in `ILS-dev/backend/routes/aiQuiz.js`.

Overview

- Endpoint: `POST /api/ai/quiz/generate`
- Purpose: generate multiple-choice quiz questions from selected learning outcomes or assignment context using an external AI service (Ollama/OpenAI-compatible endpoint).
- Authentication: the backend mounts `/api/ai` after `requireAuth` — an authenticated JWT session is required. The router itself does not enforce additional role restrictions.

Environment

- `AI_BASE_URL` — base URL for the AI service (default: `http://localhost:11434/v1`).
- `AI_MODEL` — model name used for generation (example default: `gemma2:9b-instruct-q4_K_M`).
- `AI_API_KEY` — used as Bearer token when calling the AI endpoint (`Authorization: Bearer <AI_API_KEY>`).

Request

- Content-Type: `application/json`
- Body schema (JSON):

```json
{
  "outcome_ids": [123, 456],      // optional
  "assignment_ids": [10, 11],     // optional
  "count": 3,                     // optional (default 3)
  "difficulty": "easy|medium|hard", // optional (default "medium")
  "instructions": "free-text instructions from teacher" // optional
}
```

Rules

- At least one of `outcome_ids` or `assignment_ids` must be provided — otherwise the server returns HTTP 400.
- The server validates the provided IDs exist; if none match, it returns HTTP 404.

Behavior

1. The server loads the referenced Outcomes and/or Assignments from the DB and builds a context block used in the AI prompt.
2. It constructs a deterministic prompt that instructs the model to return a JSON array of MCQ objects, each with exactly four options, a single correct answer, an explanation, `points`, and `type: "mcq"`.
3. It POSTs the prompt to the configured AI endpoint (`POST ${AI_BASE_URL}/chat/completions`) with model and temperature parameters.
4. The server parses the first JSON array found in the AI response. If parsing fails, the endpoint returns HTTP 502 with the raw model output.
5. Outcome mapping: for each returned question, the server maps `outcome_code` → `outcome_id` (if the outcome was included in the request) and returns an `outcome_id` (or `null`).

Response

- Success (200):

```json
{
  "questions": [
    {
      "question": "What is X?",
      "outcome_code": "OC.1",
      "outcome_id": 123,
      "options": [
        { "label": "Option A", "value": "0" },
        { "label": "Option B", "value": "1" },
        { "label": "Option C", "value": "2" },
        { "label": "Option D", "value": "3" }
      ],
      "correct_answer": "0",
      "explanation": "Reason why A is correct.",
      "points": 1,
      "type": "mcq"
    }
  ],
  "model": "gemma2:9b-instruct-q4_K_M"
}
```

Error cases

- 400 Bad Request — missing both `outcome_ids` and `assignment_ids`.
- 404 Not Found — none of the provided IDs match DB records.
- 502 Bad Gateway — AI service error or AI returned invalid/non-JSON output. The server includes the raw AI output in the error response when parsing fails.
- 500 Internal Server Error — unexpected server-side failure.

Implementation notes & cautions

- The endpoint relies on an external AI service; production usage should provision an appropriate `AI_BASE_URL` and `AI_API_KEY`, apply rate-limiting, and log/monitor AI errors.
- The server expects the model to respond with a JSON array only; it extracts the first `[...]` block found in the model output and attempts to `JSON.parse()` it. Malformed outputs produce a 502 error.
- Questions returned are not persisted by this endpoint — they are returned to the client as an unsaved `quiz_items`-compatible structure. The client (teacher UI) should validate and persist any items it decides to keep.
- The server maps `outcome_code` to `outcome_id` only if the outcome was included in the request; otherwise `outcome_id` will be `null`.

References (read-only source)

- `ILS-dev/backend/routes/aiQuiz.js`


**Last updated:** 2026-07-08

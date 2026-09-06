---
name: endpoint-review
description: Reviews a FastAPI endpoint in this repository against the team's five-point checklist covering response models, parameter validation, empty results, SQL parameterisation and test coverage. Use this whenever someone asks to review, check or sanity-check an endpoint before it is committed.
---

# Endpoint review

Review the endpoint you were asked about against every item below. Work through
them in order and report each one as pass or fail with the line that decided it.

1. **Typed response** — the endpoint declares `response_model=` and returns model
   instances from `app/models.py`, not bare dictionaries.
2. **Validated parameters** — every query parameter uses `Query(...)` with a
   default and, where it is numeric, bounds.
3. **Empty case** — the endpoint handles "no rows" explicitly rather than relying
   on the caller to cope with an empty list.
4. **Parameterised SQL** — values reach the query through the `params` tuple.
   Any f-string or `+` inside a SQL string is an automatic fail.
5. **Tests** — `tests/` contains at least one normal case and one empty case for
   this endpoint.

Finish with a one-line verdict: ready to commit, or the single most important fix.

For the wording of the checklist as the team publishes it, see
`docs/endpoint-checklist.md` in this repository.

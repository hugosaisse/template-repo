---
name: endpoint-review
description: Reviews a Kestrel Support API endpoint against the team's five-point quality checklist — consistent output, safe filters, an honest zero-results state, protected data, and a working safety net. Use this whenever someone asks to review, check or sanity-check an endpoint before it is committed.
---

# Endpoint review

Review the endpoint you were asked about against every item below. Work through
them in order and report each one as pass or fail with the line that decided it.

1. **Consistent output** — every ticket the endpoint returns has the same
   fields, in the same shape, every time (see `app/models.py`). No stray
   fields, none missing — like a form that never gains or drops a box, so
   whatever reads it downstream never has to guess what's there.
2. **Filters that can't break the page** — every filter the endpoint accepts
   (status, limit, …) falls back to a sensible default and a sane range, so a
   missing or odd value never produces an error page.
3. **Honest zero** — "no tickets match" comes back as an empty list, not a
   crash. Nothing hides the difference between "nothing found" and "something
   broke."
4. **Filters can't tamper with the data** — whatever a caller types into a
   filter is only ever treated as a search term, never as an instruction the
   database could run (values go through `params`, never pasted straight into
   the SQL text).
5. **A safety net that runs itself** — `tests/` has an automatic check that a
   normal request still returns real tickets, and an impossible one still
   returns none, every time the code changes.

Finish with a one-line verdict: ready to commit, or the single most important
fix.

For the checklist as the team publishes it, see `docs/endpoint-checklist.md`
in this repository.

# Kestrel Support API — working agreement

This is a small FastAPI service over a SQLite database of synthetic support tickets.

## Stack

Python 3.12, FastAPI, SQLite. No ORM — plain `sqlite3` through `app/db.py`.

## Commands

- Run the API: `uvicorn app.main:app --reload`
- Run the tests: `pytest -q`

## Where things go

- New endpoints go in `app/main.py`.
- Every response model goes in `app/models.py`. Endpoints return a model, never a bare dict.
- All database access goes through `query()` in `app/db.py`. Never open a connection elsewhere.

## Conventions

- Endpoint paths are lowercase and hyphenated: `/tickets/by-category`, not `/ticketsByCategory`.
- Function names are `snake_case` and say what they return: `count_by_category`.
- Pass values to SQL as parameters. Never build SQL with f-strings or concatenation — a filter value must never be able to change what the query does, only what it matches.

These three rules are exactly what `endpoint-review` checks for — see
`docs/endpoint-checklist.md` for the plain-language version of the same bar.

## Always

Add a test for every new endpoint — one normal case and one empty case — in `tests/`.

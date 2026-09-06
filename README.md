# Kestrel Support API — Session 4 template

A deliberately small FastAPI service over a SQLite database of **synthetic**
support tickets. Nothing here describes a real company, product or customer.

You will use this repository for all four demos in Session 4, and you may keep
using it for your project.

## Start here

Open this repository as a **Codespace** (green *Code* button → *Codespaces* →
*Create codespace on main*). Everything installs itself. Then:

```bash
uvicorn app.main:app --reload
```

Open the forwarded port and add `/docs` to the URL. You get a page listing the
endpoints, with a button to run each one. No REST client needed.

Run the tests with:

```bash
pytest -q
```

## What is in here

```
app/            the API — main.py, models.py, db.py
tests/          one normal case and one empty case per endpoint
data/           support.db — 60 synthetic tickets
docs/           the endpoint review checklist used in demo 2
demo/           the files you will copy into place during the demos
```

## The demo files

`demo/` holds the four steering files. They are **not** installed yet — putting
them in place is the demo. Each one goes somewhere specific:

| From | To | Used in |
|---|---|---|
| `demo/AGENTS.md` | repository root, `AGENTS.md` | demo 1 |
| `demo/endpoint-review/` | `.github/skills/endpoint-review/` | demo 2 |
| `demo/reviewer.agent.md` | `.github/agents/reviewer.agent.md` | demo 3 |
| `demo/mcp.json` | `.vscode/mcp.json` | demo 4 |

Two extras you can try afterwards: `demo/guardrails.json` and
`demo/block-secrets.sh` go to `.github/hooks/`, and show a rule that is enforced
rather than requested.

## When it goes wrong

- **Student verification still pending.** You cannot fix this by retrying. Start
  it early; it takes days.
- **A skill never fires.** The `description` is too vague. Rewrite it to say
  *what it does and when to use it* — that sentence is the entire trigger.
- **The MCP server does not appear.** Check the file is at `.vscode/mcp.json`
  and that the top-level key is `"servers"`. Accept the trust prompt, then
  reload the window before debugging anything else.
- **Custom agents missing.** You are in Ask mode. Switch the chat to Agent mode.
- **Out of AI credits.** Code completions still work. Batch your requests and
  start fresh chats instead of dragging a long history along.

## Licence and data

Synthetic material prepared for teaching. Reuse freely.

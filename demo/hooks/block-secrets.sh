#!/usr/bin/env bash
# Runs just before the agent uses ANY tool (read, edit, terminal, search).
# The agent's planned action arrives as text on standard input.

# 1. Read what the agent is about to do.
request=$(cat)

# 2. Does it mention a .env file (.env, .env.local, ...)?
if printf '%s' "$request" | grep -qE '\.env([^[:alnum:]_]|$)'; then
  # 3. Yes: refuse. Exit code 2 cancels the tool call, and this
  #    message is handed back to the agent as the reason.
  echo "Blocked: .env files are off limits to the agent." >&2
  exit 2
fi

# 4. No: exit 0 and the tool runs as normal.
exit 0

#!/usr/bin/env bash
# PreToolUse hook: refuse any tool call that touches a .env file.
# Exits non-zero to block. This runs outside the model — it is not a request.
payload=$(cat)
if echo "$payload" | grep -qE '\.env(\.|$|["'"'"'[:space:]])'; then
  echo "Blocked: .env files are off limits to the agent." >&2
  exit 2
fi
exit 0

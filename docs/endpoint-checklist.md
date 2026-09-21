# Endpoint review checklist

1. Does every response come back in the same, consistent shape — no fields added or missing?
2. Does every filter fall back to a sensible default when it's missing or odd?
3. Does "nothing matches" come back as an honest empty list, not a crash?
4. Are filter values kept safely separate from the SQL itself, so they can never be run as commands?
5. Is there an automatic check covering one normal case and one "nothing found" case?

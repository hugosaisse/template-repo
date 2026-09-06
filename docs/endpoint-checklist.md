# Endpoint review checklist

1. Does it return a typed response model, not a bare dict?
2. Is every query parameter validated, with a sensible default?
3. Does it handle the empty-result case explicitly?
4. Is the SQL parameterised — no f-strings, no concatenation?
5. Is there a test covering one normal case and one empty case?

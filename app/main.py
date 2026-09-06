"""Kestrel Software — support ticket API.

Deliberately small. Two endpoints, so that adding a third is a real task
with a real shape to copy.
"""
from fastapi import FastAPI, Query

from app.db import query
from app.models import CategoryCount, Ticket

app = FastAPI(
    title="Kestrel Support API",
    description="Synthetic support ticket data. Nothing here is real.",
    version="1.0.0",
)


@app.get("/tickets", response_model=list[Ticket])
def list_tickets(
    status: str | None = Query(default=None, description="Filter by status"),
    limit: int = Query(default=20, ge=1, le=100),
) -> list[Ticket]:
    """Return tickets, most recently opened first."""
    if status:
        rows = query(
            "SELECT * FROM tickets WHERE status = ? ORDER BY opened_on DESC LIMIT ?",
            (status, limit),
        )
    else:
        rows = query(
            "SELECT * FROM tickets ORDER BY opened_on DESC LIMIT ?",
            (limit,),
        )
    return [Ticket(**row) for row in rows]


@app.get("/tickets/by-urgency", response_model=list[CategoryCount])
def count_by_urgency() -> list[CategoryCount]:
    """Count tickets grouped by urgency.

    This is the shape to copy when you add a new aggregate endpoint.
    """
    rows = query(
        "SELECT urgency AS category, COUNT(*) AS ticket_count "
        "FROM tickets GROUP BY urgency ORDER BY ticket_count DESC"
    )
    if not rows:
        return []
    return [CategoryCount(**row) for row in rows]

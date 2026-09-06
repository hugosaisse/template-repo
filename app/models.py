"""Response models. Every endpoint returns one of these, never a bare dict."""
from pydantic import BaseModel


class Ticket(BaseModel):
    id: int
    subject: str
    category: str
    urgency: str
    status: str
    country: str
    opened_on: str


class CategoryCount(BaseModel):
    category: str
    ticket_count: int

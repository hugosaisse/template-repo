"""One normal case and one empty case per endpoint. Copy this shape."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_tickets_returns_rows():
    response = client.get("/tickets?limit=5")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_list_tickets_empty_when_status_unknown():
    response = client.get("/tickets?status=does-not-exist")
    assert response.status_code == 200
    assert response.json() == []


def test_count_by_urgency_covers_all_tickets():
    response = client.get("/tickets/by-urgency")
    assert response.status_code == 200
    assert sum(row["ticket_count"] for row in response.json()) == 60

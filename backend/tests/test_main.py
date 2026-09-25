from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "MovieVault API is running"


def test_search_returns_query():
    response = client.get("/api/search", params={"query": "Interstellar"})
    assert response.status_code == 200
    assert response.json()["query"] == "Interstellar"


def test_watchlist_add_and_remove():
    add = client.post("/api/watchlist/157336")
    assert 157336 in add.json()["watchlist"]

    remove = client.delete("/api/watchlist/157336")
    assert 157336 not in remove.json()["watchlist"]

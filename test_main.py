from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_homepage():
    res = client.get("/")
    assert res.status_code == 200
    assert "<title>Index - iPortfolio Bootstrap Template</title>" in res.text
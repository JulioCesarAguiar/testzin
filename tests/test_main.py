from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    payload = {"id": 1, "name": "Item Teste"}
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    assert response.json() == payload

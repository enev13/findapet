from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user_success():
    payload = {"email": "felix@kanitz.com", "password": "koti", "name": "Felix", "last_name": "Kanitz"}

    response = client.post("/register/", json=payload)
    assert response.status_code == 201
    assert response.json() == {"message": "Hello World"}


def test_read_user():
    payload = {
        "email": "felix@kanitz.com",
        "id": 1,
        "name": "Felix",
        "last_name": "Kanitz",
        "location": None,
        "role": "user",
        "animals": [],
    }

    response = client.get("/users/1/")
    assert response.status_code == 200
    assert response.json() == payload

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.db import crud

from app.main import app
from app.schemas.users import UserInCreate
from tests.utils.utils import random_email, random_lower_string

client = TestClient(app)


def generate_random_user_data() -> dict:
    email = random_email()
    password = random_lower_string()
    name = random_lower_string()
    last_name = random_lower_string()
    return {"email": email, "password": password, "name": name, "last_name": last_name}


def test_create_user_new_email(client: TestClient, db: Session) -> None:
    data = generate_random_user_data()
    rsp = client.post("/register/", json=data)

    assert 200 <= rsp.status_code < 300

    created_user = rsp.json()
    user = crud.get_user_by_email(db, email=data["email"])
    assert user
    assert user.email == created_user["email"]


def test_retrieve_users(client: TestClient, db: Session) -> None:
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    data2 = generate_random_user_data()
    user_in2 = UserInCreate(**data2)
    crud.create_user(db, user=user_in2)

    rsp = client.get("/users/")
    all_users = rsp.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "email" in item


def test_update_user(client: TestClient, db: Session) -> None:
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    user = crud.create_user(db, user=user_in)

    new_data = generate_random_user_data()
    del new_data["email"]
    data.update(new_data)

    rsp = client.patch("/users/", json=data)

    updated_user = rsp.json()
    user = crud.get_user_by_email(db, email=data["email"])
    print(user, updated_user)

    assert user
    assert user.email == updated_user["email"]

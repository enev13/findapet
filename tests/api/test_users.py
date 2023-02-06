from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.db import crud

from app.main import app
from app.schemas.users import UserInCreate
from tests.utils.utils import random_email, random_lower_string

client = TestClient(app)


def test_create_user_new_email(client: TestClient, db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    name = random_lower_string()
    last_name = random_lower_string()
    data = {"email": email, "password": password, "name": name, "last_name": last_name}
    rsp = client.post("/register/", json=data)

    assert 200 <= rsp.status_code < 300

    created_user = rsp.json()
    user = crud.get_user_by_email(db, email=email)
    assert user
    assert user.email == created_user["email"]


def test_retrieve_users(client: TestClient, db: Session) -> None:
    username = random_email()
    password = random_lower_string()
    name = random_lower_string()
    last_name = random_lower_string()
    user_in = UserInCreate(email=username, password=password, name=name, last_name=last_name)
    crud.create_user(db, user=user_in)

    username2 = random_email()
    password2 = random_lower_string()
    name2 = random_lower_string()
    last_name2 = random_lower_string()
    user_in2 = UserInCreate(email=username2, password=password2, name=name2, last_name=last_name2)
    crud.create_user(db, user=user_in2)

    r = client.get("/users/")
    all_users = r.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "email" in item

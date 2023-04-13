"""Tests for users API"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.db import crud

from app.main import app
from app.schemas.users import UserInCreate
from tests.utils.random import generate_random_user_data

client = TestClient(app)


def test_create_user_new_email(client: TestClient, db: Session) -> None:
    """Tests if user is created with new email"""
    data = generate_random_user_data()
    rsp = client.post("/register/", json=data)

    assert 200 <= rsp.status_code < 300

    created_user = rsp.json()
    user = crud.get_user_by_email(db, email=data["email"])
    assert user
    assert user.email == created_user["email"]


def test_retrieve_users(client: TestClient, db: Session) -> None:
    """Tests if users are retrieved"""
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
    """Tests if user is updated"""
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


def test_delete_user(client: TestClient, db: Session) -> None:
    """Tests if user is deleted"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    user = crud.create_user(db, user=user_in)

    rsp = client.delete(f"/users/{user.id}")
    assert rsp.status_code == 204

    user = crud.get_user(db, user_id=user.id)
    assert user is None


def test_login_user(client: TestClient, db: Session) -> None:
    """Tests if user can login with correct credentials"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 200
    assert "access_token" in rsp.json()


def test_login_user_wrong_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with wrong password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    data["password"] = "wrong_password"
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 401
    assert "detail" in rsp.json()


def test_login_user_wrong_email(client: TestClient, db: Session) -> None:
    """Tests if user can login with wrong email"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    data["email"] = "wrong_email"
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 401
    assert "detail" in rsp.json()


def test_login_user_wrong_email_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with wrong email and password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    data["email"] = "wrong_email"
    data["password"] = "wrong_password"
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 401
    assert "detail" in rsp.json()


def test_login_user_no_email(client: TestClient, db: Session) -> None:
    """Tests if user can login with no email"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    data["email"] = ""
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 422
    assert "detail" in rsp.json()


def test_login_user_no_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with no password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    data["password"] = ""
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 422
    assert "detail" in rsp.json()


def test_login_user_no_email_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with no email and password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    data["email"] = ""
    data["password"] = ""
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 422
    assert "detail" in rsp.json()


def test_login_user_no_data(client: TestClient, db: Session) -> None:
    """Tests if user can login with no data"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    crud.create_user(db, user=user_in)

    rsp = client.post("/login/", json={})
    assert rsp.status_code == 422
    assert "detail" in rsp.json()

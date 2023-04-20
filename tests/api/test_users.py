"""Tests for users API"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.db.crud.animals import create_animal

from app.db.crud.users import create_user, get_user_by_email
from app.main import app
from app.schemas.users import UserInCreate
from tests.utils.random import generate_random_animal_in
from tests.utils.random import generate_random_user_data

client = TestClient(app)


def test_create_user_new_email(client: TestClient, db: Session) -> None:
    """Tests if user is created with new email"""
    data = generate_random_user_data()
    rsp = client.post("/register/", json=data)

    assert 200 <= rsp.status_code < 300

    created_user = rsp.json()
    user = get_user_by_email(db, email=data["email"])
    assert user
    assert user.email == created_user["email"]


def test_create_user_existing_email(client: TestClient, db: Session) -> None:
    """Tests if user is not created with existing email"""
    data = generate_random_user_data()
    create_user(db, user=UserInCreate(**data))

    rsp = client.post("/register/", json=data)
    assert rsp.status_code == 400


def test_retrieve_user(client: TestClient, db: Session) -> None:
    """Tests if user is retrieved"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    user = create_user(db, user=user_in)

    rsp = client.get(f"/users/{user.id}")

    assert 200 <= rsp.status_code < 300

    retrieved_user = rsp.json()
    assert retrieved_user
    assert retrieved_user["email"] == user.email


def test_retrieve_users(client: TestClient, db: Session) -> None:
    """Tests if users are retrieved"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    data2 = generate_random_user_data()
    user_in2 = UserInCreate(**data2)
    create_user(db, user=user_in2)

    rsp = client.get("/users/")

    assert 200 <= rsp.status_code < 300

    all_users = rsp.json()

    assert all_users
    assert len(all_users) > 1


def test_update_user(client: TestClient, db: Session) -> None:
    """Tests if user is updated"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    user = create_user(db, user=user_in)

    new_data = generate_random_user_data()
    del new_data["email"]
    data.update(new_data)

    rsp = client.patch(f"/users/{user.id}", json=data)
    print(rsp)
    assert rsp.status_code == 200

    updated_user = rsp.json()
    print(updated_user)
    user = get_user_by_email(db, email=data["email"])

    assert user
    assert user.email == updated_user["email"]


def test_update_non_existing_user(client: TestClient, db: Session) -> None:
    """Tests if user is not updated"""
    data = generate_random_user_data()
    rsp = client.patch("/users/0", json=data)
    assert rsp.status_code == 404


def test_retrieve_animals_for_user(client: TestClient, db: Session) -> None:
    """Tests if animals are retrieved for user"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    create_animal(db, animal=animal_in)

    rsp = client.get(f"/users/{user.id}/animals/")
    assert rsp.status_code == 200

    all_animals = rsp.json()

    assert all_animals
    assert len(all_animals) > 0


def test_delete_user(client: TestClient, db: Session) -> None:
    """Tests if user is deleted"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    user = create_user(db, user=user_in)

    rsp = client.delete(f"/users/{user.id}")
    assert rsp.status_code == 204

    user = get_user_by_email(db, email=data["email"])
    assert user is None


def test_delete_non_existing_user(client: TestClient, db: Session) -> None:
    """Tests if user is not deleted"""
    rsp = client.delete("/users/0")
    assert rsp.status_code == 404


def test_user_not_found(client: TestClient, db: Session) -> None:
    """Tests if user is not found"""
    rsp = client.get("/users/0")
    assert rsp.status_code == 404


def test_login_user(client: TestClient, db: Session) -> None:
    """Tests if user can login with correct credentials"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)
    login_data = {"username": data["email"], "password": data["password"], "grant_type": "password"}
    rsp = client.post(
        "/login/", data=login_data, headers={"content-type": "application/x-www-form-urlencoded"}
    )
    assert rsp.status_code == 200
    assert "access_token" in rsp.json()


def test_login_user_wrong_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with wrong password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    data["password"] = "wrong_password"
    login_data = {"username": data["email"], "password": data["password"], "grant_type": "password"}
    rsp = client.post(
        "/login/", data=login_data, headers={"content-type": "application/x-www-form-urlencoded"}
    )
    assert rsp.status_code == 400
    assert "detail" in rsp.json()


def test_login_user_wrong_email(client: TestClient, db: Session) -> None:
    """Tests if user can login with wrong email"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    data["email"] = "wrong_email"
    login_data = {"username": data["email"], "password": data["password"], "grant_type": "password"}
    rsp = client.post(
        "/login/", data=login_data, headers={"content-type": "application/x-www-form-urlencoded"}
    )
    assert rsp.status_code == 400
    assert "detail" in rsp.json()


def test_login_user_wrong_email_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with wrong email and password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    data["email"] = "wrong_email"
    data["password"] = "wrong_password"
    login_data = {"username": data["email"], "password": data["password"], "grant_type": "password"}
    rsp = client.post(
        "/login/", data=login_data, headers={"content-type": "application/x-www-form-urlencoded"}
    )
    assert rsp.status_code == 400
    assert "detail" in rsp.json()


def test_login_user_no_email(client: TestClient, db: Session) -> None:
    """Tests if user can login with no email"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    data["email"] = ""
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 422
    assert "detail" in rsp.json()


def test_login_user_no_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with no password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    data["password"] = ""
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 422
    assert "detail" in rsp.json()


def test_login_user_no_email_password(client: TestClient, db: Session) -> None:
    """Tests if user can login with no email and password"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    data["email"] = ""
    data["password"] = ""
    rsp = client.post("/login/", json=data)
    assert rsp.status_code == 422
    assert "detail" in rsp.json()


def test_login_user_no_data(client: TestClient, db: Session) -> None:
    """Tests if user can login with no data"""
    data = generate_random_user_data()
    user_in = UserInCreate(**data)
    create_user(db, user=user_in)

    rsp = client.post("/login/", json={})
    assert rsp.status_code == 422
    assert "detail" in rsp.json()

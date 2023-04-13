"""Test for animals API"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.db import crud

from app.main import app
from app.schemas.animals import Animal
from tests.utils.random import generate_random_animal_data

client = TestClient(app)


def test_create_new_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is created"""
    data = generate_random_animal_data()
    rsp = client.post("/animals/", json=data)

    assert 200 <= rsp.status_code < 300

    created_animal = rsp.json()
    animal = crud.get_animal(db, animal_id=created_animal["id"])
    assert animal
    assert animal.name == created_animal["name"]


def test_get_animals(client: TestClient, db: Session) -> None:
    """Tests if animals are retrieved"""
    data = generate_random_animal_data()
    crud.create_animal(db, Animal(**data))
    rsp = client.get("/animals/")

    assert 200 <= rsp.status_code < 300

    created_animals = rsp.json()
    animals = crud.get_animals(db)
    assert animals == created_animals


def test_get_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is retrieved"""
    data = generate_random_animal_data()
    animal = crud.create_animal(db, Animal(**data))
    rsp = client.get(f"/animals/{animal.id}")
    assert 200 <= rsp.status_code < 300
    retrieved_animal = rsp.json()
    assert retrieved_animal
    assert retrieved_animal["id"] == animal.id
    assert retrieved_animal["name"] == animal.name


def test_update_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is updated"""
    data = generate_random_animal_data()
    animal = crud.create_animal(db, Animal(**data))
    new_data = generate_random_animal_data()
    rsp = client.put(f"/animals/{animal.id}", json=new_data)
    assert 200 <= rsp.status_code < 300
    updated_animal = rsp.json()
    assert updated_animal
    assert updated_animal["id"] == animal.id
    assert updated_animal["name"] == new_data["name"]


def test_delete_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is deleted"""
    data = generate_random_animal_data()
    animal = crud.create_animal(db, Animal(**data))
    rsp = client.delete(f"/animals/{animal.id}")
    assert 200 <= rsp.status_code < 300
    deleted_animal = rsp.json()
    assert deleted_animal
    assert deleted_animal["id"] == animal.id
    assert deleted_animal["name"] == animal.name


def test_get_animal_not_found(client: TestClient, db: Session) -> None:
    """Tests if animal is not found"""
    rsp = client.get("/animals/0")
    assert rsp.status_code == 404


def test_update_animal_not_found(client: TestClient, db: Session) -> None:
    """Tests if animal is not found"""
    data = generate_random_animal_data()
    rsp = client.put("/animals/0", json=data)
    assert rsp.status_code == 404


def test_delete_animal_not_found(client: TestClient, db: Session) -> None:
    """Tests if animal is not found"""
    rsp = client.delete("/animals/0")
    assert rsp.status_code == 404


def test_create_animal_invalid_data(client: TestClient, db: Session) -> None:
    """Tests if animal is not created"""
    data = generate_random_animal_data()
    data["name"] = 1
    rsp = client.post("/animals/", json=data)
    assert rsp.status_code == 422


def test_update_animal_invalid_data(client: TestClient, db: Session) -> None:
    """Tests if animal is not updated"""
    data = generate_random_animal_data()
    animal = crud.create_animal(db, Animal(**data))
    new_data = generate_random_animal_data()
    new_data["name"] = 1
    rsp = client.put(f"/animals/{animal.id}", json=new_data)
    assert rsp.status_code == 422


def test_get_animals_invalid_data(client: TestClient, db: Session) -> None:
    """Tests if animals are not retrieved"""
    rsp = client.get("/animals/?skip=abc&limit=abc")
    assert rsp.status_code == 422

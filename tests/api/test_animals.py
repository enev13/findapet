"""Test for animals API"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db.crud.animals import create_animal, get_animal
from app.db.crud.users import create_user
from app.main import app
from tests.crud.test_animals import generate_random_animal_in
from tests.crud.test_users import generate_random_user_in
from tests.utils.random import generate_random_animal_data

client = TestClient(app)


def test_create_new_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is created"""
    data = generate_random_animal_data()

    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    data.update({"owner_id": user.id})
    rsp = client.post("/animals/", json=data)

    assert 200 <= rsp.status_code < 300

    created_animal = rsp.json()
    animal = get_animal(db, animal_id=created_animal["id"])
    assert animal
    assert animal.name == created_animal["name"]


def test_get_animals(client: TestClient, db: Session) -> None:
    """Tests if animals are retrieved"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    create_animal(db, animal=animal_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    create_animal(db, animal=animal_in)

    rsp = client.get("/animals/")

    assert 200 <= rsp.status_code < 300

    all_animals = rsp.json()

    assert all_animals
    assert len(all_animals) > 1


def test_get_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is retrieved"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    rsp = client.get(f"/animals/{animal.id}")
    assert 200 <= rsp.status_code < 300
    retrieved_animal = rsp.json()
    assert retrieved_animal
    assert retrieved_animal["id"] == animal.id
    assert retrieved_animal["name"] == animal.name


def test_update_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is updated"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    new_data = generate_random_animal_data()
    new_data.update({"owner_id": user.id})
    print(new_data)
    rsp = client.patch(f"/animals/{animal.id}", json=new_data)
    assert 200 <= rsp.status_code < 300
    updated_animal = rsp.json()
    assert updated_animal
    assert updated_animal["id"] == animal.id
    assert updated_animal["name"] == new_data["name"]


def test_delete_animal(client: TestClient, db: Session) -> None:
    """Tests if animal is deleted"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    rsp = client.delete(f"/animals/{animal.id}")
    assert rsp.status_code == 204

    animal = get_animal(db, animal_id=animal.id)
    assert animal is None


def test_get_animal_not_found(client: TestClient, db: Session) -> None:
    """Tests if animal is not found"""
    rsp = client.get("/animals/0")
    assert rsp.status_code == 404


def test_create_animal_invalid_data(client: TestClient, db: Session) -> None:
    """Tests if animal is not created"""
    data = generate_random_animal_data()

    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    data.update({"owner_id": user.id, "age": 1})

    rsp = client.post("/animals/", json=data)
    assert rsp.status_code == 422


def test_update_animal_invalid_data(client: TestClient, db: Session) -> None:
    """Tests if animal is not updated"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    new_data = generate_random_animal_data()
    new_data.update({"owner_id": user.id, "age": 1})

    rsp = client.patch(f"/animals/{animal.id}", json=new_data)
    assert rsp.status_code == 422


def test_get_animals_invalid_data(client: TestClient, db: Session) -> None:
    """Tests if animals are not retrieved"""
    rsp = client.get("/animals/?skip=abc&limit=abc")
    assert rsp.status_code == 422

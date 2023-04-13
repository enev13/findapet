import random
from tests.utils.utils import random_email, random_lower_string


def generate_random_user_data() -> dict:
    """Generates random user data"""
    email = random_email()
    password = random_lower_string()
    name = random_lower_string()
    last_name = random_lower_string()
    return {"email": email, "password": password, "name": name, "last_name": last_name}


def generate_random_animal_data() -> dict:
    """Generates random animal data"""
    name = random_lower_string()
    description = random_lower_string()
    animal_type = "Cat"
    breed = random.choices(["Persian", "Siamese", "Sphynx", "Tabby"])
    size = random.choices(["small", "Medium", "Large"])
    gender = random.choices(["Male", "Female"])
    age = random.randint(1, 20)
    coat = random.choices(["Short", "Medium", "Long"])
    status = random.choices(["Adoptable", "Adopted"])
    good_with_children = random.choices([0, 1])
    good_with_dogs = random.choices([0, 1])
    good_with_cats = random.choices([0, 1])
    house_trained = random.choices([0, 1])
    declawed = random.choices([0, 1])
    special_needs = random.choices([0, 1])
    location = random_lower_string()
    return {
        "name": name,
        "description": description,
        "animal_type": animal_type,
        "breed": breed,
        "size": size,
        "gender": gender,
        "age": age,
        "coat": coat,
        "status": status,
        "good_with_children": good_with_children,
        "good_with_dogs": good_with_dogs,
        "good_with_cats": good_with_cats,
        "house_trained": house_trained,
        "declawed": declawed,
        "special_needs": special_needs,
        "location": location,
    }

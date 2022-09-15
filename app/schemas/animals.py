from typing import List, Optional

from models import enums

from base import AnimalBase


class Animal(AnimalBase):
    id: int
    type: enums.Type
    breed: str
    size: enums.Size
    gender: enums.Gender
    age: enums.Age
    coat: enums.Coat
    status: enums.Status
    user: str
    good_with_children: enums.BoolType
    good_with_dogs: enums.BoolType
    good_with_cats: enums.BoolType
    house_trained: enums.BoolType
    declawed: enums.BoolType
    special_needs: enums.BoolType
    location: str
    photos: Optional[List[str]]
    videos: Optional[List[str]]
    tags: Optional[List[str]]


class Dog(Animal):
    color: List[enums.ColorDog]


class Cat(Animal):
    color: List[enums.ColorCat]

    class Config:
        schema_extra = {
            "example": {
                "name": "Felix",
                "description": "A playful kitty with nice character",
                "type": "Cat",
                "breed": "European",
                "size": "Small",
                "color": ["tuxedo"],
                "gender": "Male",
                "age": "Young",
                "coat": "Short",
                "status": "Adopted",
                "organization": "None",
                "good_with_children": 1,
                "good_with_dogs": 0,
                "good_with_cats": 1,
                "house_trained": 1,
                "declawed": 0,
                "special_needs": 0,
                "location": "Varna, Bulgaria",
                "photos": [
                    "https://linktomyimage.com/photo1.png",
                    "https://linktomyimage.com/photo2.png",
                ],
                "videos": [
                    "https://linktomyvideo.com/video1.mpg",
                    "https://linktomyvideo.com/video2.mpg",
                ],
                "tags": ["Cute", "Playful"],
            }
        }


class Rabbit(Animal):
    color: List[enums.ColorRabbit]


class Bird(Animal):
    color: List[enums.ColorBird]

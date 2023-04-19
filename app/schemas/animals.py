"""Schemas for animals."""
from typing import List, Optional

from app.models import enums
from app.schemas.base import AnimalBase, Photo, Tag, Video


class Animal(AnimalBase):
    """Animal schema."""

    id: int
    animal_type: enums.Type
    breed: str
    size: enums.Size
    gender: enums.Gender
    age: enums.Age
    coat: enums.Coat
    status: enums.Status
    good_with_children: enums.BoolType
    good_with_dogs: enums.BoolType
    good_with_cats: enums.BoolType
    house_trained: enums.BoolType
    declawed: enums.BoolType
    special_needs: enums.BoolType
    location: str
    # photos: Optional[List[Photo]]
    # videos: Optional[List[Video]]
    # tags: Optional[List[Tag]]
    owner_id: int
    # owner: str

    class Config:
        """Pydantic config."""

        schema_extra = {
            "example": {
                "name": "Felix",
                "description": "A playful kitty with nice character",
                "animal_type": "Cat",
                "breed": "European",
                "size": "Small",
                "color": ["tuxedo"],
                "gender": "Male",
                "age": "Young",
                "coat": "Short",
                "status": "Adopted",
                "owner": "None",
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


class AnimalInCreateUpdate(AnimalBase):
    animal_type: enums.Type
    breed: str
    size: enums.Size
    gender: enums.Gender
    age: enums.Age
    coat: enums.Coat
    status: enums.Status
    good_with_children: enums.BoolType
    good_with_dogs: enums.BoolType
    good_with_cats: enums.BoolType
    house_trained: enums.BoolType
    declawed: enums.BoolType
    special_needs: enums.BoolType
    location: str
    photos: Optional[List[Photo]] = []
    videos: Optional[List[Video]] = []
    tags: Optional[List[Tag]] = []
    owner_id: Optional[int]


class Dog(Animal):
    """Dog schema."""

    color: List[enums.ColorDog]


class Cat(Animal):
    """Cat schema."""

    color: List[enums.ColorCat]


class Rabbit(Animal):
    """Rabbit schema."""

    color: List[enums.ColorRabbit]


class Bird(Animal):
    """Bird schema."""

    color: List[enums.ColorBird]

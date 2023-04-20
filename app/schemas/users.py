"""User schemas"""

from typing import List, Optional

from app.models import enums
from app.schemas.animals import Animal
from app.schemas.base import UserBase


class User(UserBase):
    """User schema"""

    id: int
    name: Optional[str]
    last_name: Optional[str]
    location: Optional[str]
    role: Optional[enums.RoleType] = enums.RoleType.user
    animals: Optional[List[Animal]]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"name": "Felix", "last_name": "Kanitz", "location": "Varna, Bulgaria", "role": "user"}
        }


class UserInCreate(UserBase):
    """User schema for creation"""

    name: Optional[str]
    last_name: Optional[str]
    location: Optional[str]
    password: str

    class Config:
        schema_extra = {"example": {"email": "felix@kanitz.com", "password": "koti"}}


class UserInUpdate(UserBase):
    """User schema for updating"""

    # id: int
    name: Optional[str]
    last_name: Optional[str]
    location: Optional[str]
    password: Optional[str] = None

    class Config:
        schema_extra = {"example": {"email": "felix@kanitz.com", "password": "koti"}}


class UserInLogin(UserBase):
    """User schema for login"""

    password: str

from models.enums import RoleType
from schemas.base import UserBase


class User(UserBase):
    last_name: str
    location: str
    role: RoleType

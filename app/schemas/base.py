"""Base schemas for the app."""
from pydantic import BaseModel, EmailStr


class AnimalBase(BaseModel):
    """Base schema for animals"""

    name: str
    description: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    """Base schema for users"""

    email: EmailStr

    class Config:
        orm_mode = True


class Token(BaseModel):
    """Base schema for tokens"""

    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class Photo(BaseModel):
    photo_address: str
    animal: int

    class Config:
        orm_mode = True


class Video(BaseModel):
    video_address: str
    animal: int

    class Config:
        orm_mode = True


class Tag(BaseModel):
    tag_name: str
    animal: int

    class Config:
        orm_mode = True

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models import enums


class Animal(Base):  # type: ignore
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    animal_type = Column(Enum(enums.Type), nullable=False, server_default=enums.Type.cat.name)
    breed = Column(String(120), nullable=False)
    size = Column(Enum(enums.Size), nullable=False, server_default=enums.Size.small.name)
    gender = Column(Enum(enums.Gender), nullable=False, server_default=enums.Gender.male.name)
    age = Column(Enum(enums.Age), nullable=False, server_default=enums.Age.young.name)
    coat = Column(Enum(enums.Coat), nullable=False, server_default=enums.Coat.short.name)
    status = Column(Enum(enums.Status), nullable=False, server_default=enums.Status.adoptable.name)
    good_with_children = Column(
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    )
    good_with_dogs = Column(
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    )
    good_with_cats = Column(
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    )
    house_trained = Column(
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    )
    declawed = Column(Enum(enums.BoolType), nullable=False, server_default=enums.BoolType.no.name)
    special_needs = Column(
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    )
    location = Column(String(200), nullable=False)
    photos = relationship("Photo", back_populates="animal")
    videos = relationship("Video", back_populates="animal")
    tags = relationship("Tag", back_populates="animal")
    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now())
    owner_id = Column(ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="animals")


class Photo(Base):  # type: ignore
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    photo_address = Column(String(255), nullable=False)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False)
    animal = relationship("Animal", back_populates="photos")


class Video(Base):  # type: ignore
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    video_address = Column(String(255), nullable=False)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False)
    animal = relationship("Animal", back_populates="videos")


class Tag(Base):  # type: ignore
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(255), nullable=False)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False)
    animal = relationship("Animal", back_populates="tags")

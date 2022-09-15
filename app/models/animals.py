from db.database import metadata
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Table, Text, func
from sqlalchemy.orm import relationship

import enums

animal = Table(
    "animals",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(120), nullable=False),
    Column("description", Text, nullable=False),
    Column("type", Enum(enums.Type), nullable=False, server_default=enums.Type.cat.name),
    Column("breed", String(120), nullable=False),
    Column("size", Enum(enums.Size), nullable=False, server_default=enums.Size.small.name),
    Column("gender", Enum(enums.Gender), nullable=False, server_default=enums.Gender.male.name),
    Column("age", Enum(enums.Age), nullable=False, server_default=enums.Age.young.name),
    Column("coat", Enum(enums.Coat), nullable=False, server_default=enums.Coat.short.name),
    Column("status", Enum(enums.Status), nullable=False, server_default=enums.Status.adoptable.name),
    Column(
        "good_with_children",
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    ),
    Column(
        "good_with_dogs",
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    ),
    Column(
        "good_with_cats",
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    ),
    Column(
        "house_trained",
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    ),
    Column("declawed", Enum(enums.BoolType), nullable=False, server_default=enums.BoolType.no.name),
    Column(
        "special_needs",
        Enum(enums.BoolType),
        nullable=False,
        server_default=enums.BoolType.no.name,
    ),
    Column("location", String(200), nullable=False),
    Column("created_at", DateTime, server_default=func.now()),
    Column("modified_at", DateTime, server_default=func.now()),
    Column("user", ForeignKey("users.id"), nullable=False),
)


photos = Table(
    "photos",
    metadata,
    id=Column("id", Integer, primary_key=True),
    photo_address=Column(String(200), nullable=False),
    animal_id=Column(Integer, ForeignKey("users.id")),
    animal=relationship("Animal", back_populates="photos"),
)

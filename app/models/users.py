from sqlalchemy import Column, DateTime, Enum, Integer, String, func
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models import enums


class User(Base):  # type: ignore
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(255))
    last_name = Column(String(200))
    location = Column(String(200))
    role = Column(Enum(enums.RoleType), nullable=False, server_default=enums.RoleType.user.name)
    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now())
    animals = relationship("Animal", back_populates="owner", cascade="all, delete-orphan")

from db.database import metadata
from sqlalchemy import Column, DateTime, Enum, Integer, String, Table, func
import enums

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(200), nullable=False),
    Column("email", String(200), nullable=False),
    Column("password", String(255)),
    Column("last_name", String(200)),
    Column("location", String(200)),
    Column("role", Enum(enums.RoleType), nullable=False, server_default=enums.RoleType.user.name),
    Column("created_at", DateTime, server_default=func.now()),
    Column("modified_at", DateTime, server_default=func.now()),
)

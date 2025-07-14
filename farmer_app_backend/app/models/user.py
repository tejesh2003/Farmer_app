from app.database import db
from app.enums.role_enum import Role
from sqlalchemy.dialects.postgresql import ENUM as PGEnum

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(
        PGEnum(Role,name="user_role"),
        nullable=False,
        default=Role.USER
    )

from app.models.roles import Role
from app.database import db

def seed_roles():
    default_roles = ["USER", "SUPER_USER", "ADMIN"]

    for role_name in default_roles:
        if not Role.query.filter_by(name=role_name).first():
            db.session.add(Role(name=role_name))

    db.session.commit()

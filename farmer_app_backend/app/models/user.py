from app.database import db
from app.models import user_roles

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    roles = db.relationship(
    "Role",
    secondary=user_roles,
    backref=db.backref("users", lazy="dynamic"),
    lazy="joined"
)


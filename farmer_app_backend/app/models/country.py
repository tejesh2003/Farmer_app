from app.database import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(100), unique=True, nullable=False)
    farmers = db.relationship('Farmer', backref='country', lazy=True)

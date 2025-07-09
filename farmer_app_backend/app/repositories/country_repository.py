from app.models.country import Country
from app.database import db

def get_by_name(country_name):
    return Country.query.filter_by(country_name=country_name).first()

def save(country):
    db.session.add(country)
    db.session.commit()
    return country

from app.models.farmer import Farmer
from app.database import db

def save_farmer(farmer):
    db.session.add(farmer)
    db.session.commit()
    return farmer

def farmer_exists_by_phone(phone):
    return Farmer.query.filter_by(phone=phone).first() is not None

def get_farmers_by_ids(farmer_ids):
    return Farmer.query.filter(Farmer.id.in_(farmer_ids)).all()


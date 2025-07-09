from app.database import db
from app.models.farm import Farm
from app.models.farmer import Farmer


def create_farmer(data):
    required_fields = ["name", "phone", "language", "country_id"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")
    if Farmer.query.filter_by(phone=data["phone"]).first():
        raise ValueError("Phone number already exists.")
    farmer = Farmer(
        name=data["name"],
        phone=data["phone"],
        language=data["language"],
        country_id=data["country_id"]
    )
    db.session.add(farmer)
    db.session.commit()
    return farmer


def get_farmers_by_crop(crop):
    if not crop:
        raise ValueError("Crop name is required.")
    farms = Farm.query.filter_by(crop=crop).all()
    if not farms:
        return []
    farmer_ids = {farm.farmer_id for farm in farms}
    farmers = Farmer.query.filter(Farmer.id.in_(farmer_ids)).all()
    return farmers

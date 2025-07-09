from app.models.farm import Farm
from app.database import db

def save_farm(farm):
    db.session.add(farm)
    db.session.commit()
    return farm


def get_farms_by_crop(crop):
    return Farm.query.filter_by(crop=crop).all()

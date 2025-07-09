from app.models.farmer import Farmer
from app.repositories import farmer_repository, farm_repository
from app.services.country_service import get_or_create_country

def create_farmer(data):
    required_fields = ["name", "phone", "language", "country_id"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")

    if farmer_repository.farmer_exists_by_phone(data["phone"]):
        raise ValueError("Phone number already exists.")
    
    country = get_or_create_country(data["country"])

    farmer = Farmer(
        name=data["name"],
        phone=data["phone"],
        language=data["language"],
        country_id=country.id
    )

    return farmer_repository.save_farmer(farmer)


def get_farmers_by_crop(crop):
    if not crop:
        raise ValueError("Crop name is required.")

    farms = farm_repository.get_farms_by_crop(crop)
    if not farms:
        return []

    farmer_ids = {farm.farmer_id for farm in farms}
    farmers = farmer_repository.get_farmers_by_ids(farmer_ids)
    return farmers


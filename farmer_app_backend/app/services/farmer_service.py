from app.repositories import farmer_repository, farm_repository
from app.mappers.farmer_mapper import map_to_farmer

def create_farmer(data):
    farmer = map_to_farmer(data)
    return farmer_repository.save_farmer(farmer)

def get_farmers_by_crop(crop):
    if not crop:
        raise ValueError("Crop name is required.")

    farms = farm_repository.get_farms_by_crop(crop)
    if not farms:
        return []

    farmer_ids = {farm.farmer_id for farm in farms}
    return farmer_repository.get_farmers_by_ids(farmer_ids)

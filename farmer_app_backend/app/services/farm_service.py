from app.repositories.farm_repository import save_farm
from app.mappers.farm_mapper import map_to_farm

def create_farm(data):
    farm = map_to_farm(data)
    return save_farm(farm)

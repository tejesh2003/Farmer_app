# app/services/farmer_service.py
from app.repositories import FarmerRepository, FarmRepository
from app.services import CountryService
from app.helpers import Farmer as FarmerHelper

class FarmerService:

    @staticmethod
    def create_farmer(name:str, language:str, phone:str, country:str):
        country = CountryService.get_or_create_country(country)#change here

        data = {
        "name": name,
        "phone": phone,
        "language": language,
        "country_id": country["id"]
    }

        farmer_helper=FarmerHelper.from_dict(data)

        new_farmer_helper=FarmerRepository.save_farmer(farmer_helper)
        farmer_dict=FarmerHelper.to_dict(new_farmer_helper)
        farmer_dict.pop("country_id")
        farmer_dict["country"]=country["country_name"]
        return farmer_dict

    @staticmethod
    def get_farmers_by_crop(crop):
        if not crop:
            raise ValueError("Crop name is required.")

        farms = FarmRepository.get_farms_by_crop(crop)
        if not farms:
            return []

        farmer_ids = {farm.farmer_id for farm in farms}

        farmer_helpers = FarmerRepository.get_farmers_by_ids(farmer_ids)

        return [FarmerHelper.to_dict(helper) for helper in farmer_helpers]
        

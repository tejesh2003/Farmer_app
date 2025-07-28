# app/services/farmer_service.py
from app.repositories import FarmerRepository, FarmRepository
from app.services import CountryService
from app.helpers import Farmer as FarmerHelper

class FarmerService:

    @staticmethod
    def create_farmer(name:str, language:str, phone:str, country:str):
        country = CountryService.get_country(country)

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

        farmers = []
        for helper in farmer_helpers:
            farmer_dict = FarmerHelper.to_dict(helper)

        # Get country name from ID
            country = CountryService.get_country_by_id(farmer_dict["country_id"])
            farmer_dict.pop("country_id", None)
            farmer_dict["country"] = country["country_name"] if country else None

            farmers.append(farmer_dict)

        return farmers

        
    @staticmethod
    def get_farmers_with_crop():
        farmer_helpers = FarmerRepository.get_all_farmers()
        if not farmer_helpers:
            return []
    
        filtered = []
        for helper in farmer_helpers:
            farmer_dict = FarmerHelper.to_dict(helper)

        # Check if farmer has any farms
            farms = farmer_dict.get("farms", [])
            if isinstance(farms, list) and len(farms) > 0:
            # Replace country_id with country name
                country = CountryService.get_country_by_id(farmer_dict["country_id"])
                farmer_dict.pop("country_id", None)
                farmer_dict["country"] = country["country_name"] if country else None

                filtered.append(farmer_dict)

        return filtered

    
    @staticmethod
    def get_all_farmers():
        farmer_helpers = FarmerRepository.get_all_farmers()
        if not farmer_helpers:
            return []
    
        filtered = []
        for helper in farmer_helpers:
            farmer_dict = FarmerHelper.to_dict(helper)

        # Replace country_id with country name
            country = CountryService.get_country_by_id(farmer_dict["country_id"])
            farmer_dict.pop("country_id", None)
            farmer_dict["country"] = country["country_name"] if country else None

            filtered.append(farmer_dict)

        return filtered



       

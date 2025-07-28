# app/services/farm_service.py
from datetime import datetime
from app.repositories import FarmRepository
from app.helpers import Farm as FarmHelper

class FarmService:

    @staticmethod
    def create_farm(area: float, village: str, crop: str, sowing_date: str, farmer_id: int):
        sowing_date = datetime.strptime(sowing_date, "%Y-%m-%d").date()

        data = {
        "area": area,
        "village": village,
        "crop": crop,
        "sowing_date": sowing_date,
        "farmer_id": farmer_id
    }

        farm_helper=FarmHelper.from_dict(data)

        new_farm_helper= FarmRepository.save_farm(farm_helper)

        farm_dict=FarmHelper.to_dict(new_farm_helper)

        return farm_dict
    
    @staticmethod
    def get_farm_by_schedule_id(schedule_id: int):
        farm_helper = FarmRepository.get_farm_by_schedule_id(schedule_id)
        if not farm_helper:
            raise ValueError(f"No farm found for schedule ID {schedule_id}")

        return FarmHelper.to_dict(farm_helper)
    
    @staticmethod
    def get__all_farms():
        farm_helpers = FarmRepository.get_all_farms()
        if not farm_helpers:
            return []
        
        filtered = []
        for helper in farm_helpers:
            farmer_dict = FarmHelper.to_dict(helper)
            filtered.append(farmer_dict)

        return filtered

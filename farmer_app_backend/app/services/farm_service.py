# app/services/farm_service.py
from datetime import datetime
from app.models.farm import Farm
from app.repositories.farm_repository import FarmRepository
from app.helpers.farm_helper import Farm as FarmHelper

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

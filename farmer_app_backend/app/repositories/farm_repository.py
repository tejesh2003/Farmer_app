from app.models import Farm, Schedule
from app.database import db
from app.mappers import Farm_Mapper

class FarmRepository:

    @staticmethod
    def save_farm(farm):
        farm_model=Farm_Mapper.helper_to_model(farm)
        db.session.add(farm_model)
        db.session.commit()
        farm_helper=Farm_Mapper.model_to_helper(farm_model)
        return farm_helper
    
    @staticmethod
    def get_farms_by_crop(crop: str):
        if not crop:
            return []

        farm_models = Farm.query.filter_by(crop=crop).all()
        return [Farm_Mapper.model_to_helper(farm) for farm in farm_models]
    
    @staticmethod
    def get_farm_by_schedule_id(schedule_id: int):
        schedule = Schedule.query.get(schedule_id)
        if not schedule:
            return None

        farm = Farm.query.get(schedule.farm_id)
        if not farm:
            return None

        return Farm_Mapper.model_to_helper(farm)
    
    @staticmethod
    def get_all_farms():
        farms = Farm.query.all()
        return [Farm_Mapper.model_to_helper(farm) for farm in farms]

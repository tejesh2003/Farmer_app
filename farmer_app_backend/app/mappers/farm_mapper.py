from app.models import Farm as FarmModel
from app.helpers import Farm as FarmHelper

class Farm_Mapper:

    @staticmethod
    def model_to_helper(model:FarmModel)->FarmHelper:
        return FarmHelper(
            id=model.id,
            area=model.area,
            village=model.village,
            crop=model.crop,
            sowing_date=model.sowing_date,
            farmer_id=model.farmer_id,
            schedules=model.schedules
        )
    @staticmethod
    def helper_to_model(helper: FarmHelper) -> FarmModel:
        return FarmModel(
            id=helper.id,
            area=helper.area,
            village=helper.village,
            crop=helper.crop,
            sowing_date=helper.sowing_date,
            farmer_id=helper.farmer_id,
            schedules=helper.schedules
        )
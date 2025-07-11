from app.models.schedule import Schedule as ScheduleModel
from app.helpers.schedule_helper import Schedule as ScheduleHelper

class Schedule_Mapper:

    @staticmethod
    def model_to_helper(model: ScheduleModel) -> ScheduleHelper:
        return ScheduleHelper(
            id=model.id,
            days_after_sowing=model.days_after_sowing,
            fertiliser=model.fertiliser,
            quantity=model.quantity,
            unit=model.unit,
            farm_id=model.farm_id
        )

    @staticmethod
    def helper_to_model(helper: ScheduleHelper) -> ScheduleModel:
        return ScheduleModel(
            days_after_sowing=helper.days_after_sowing,
            fertiliser=helper.fertiliser,
            quantity=helper.quantity,
            unit=helper.unit,
            farm_id=helper.farm_id
        )

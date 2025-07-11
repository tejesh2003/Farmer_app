from app.models.schedule import Schedule
from app.database import db
from app.mappers.schedule_mapper import Schedule_Mapper
from app.models.farm import Farm

class ScheduleRepository:

    @staticmethod
    def save_schedule(schedule):
        schedule_model=Schedule_Mapper.helper_to_model(schedule)
        db.session.add(schedule_model)
        db.session.commit()
        schedule_helper=Schedule_Mapper.model_to_helper(schedule_model)
        return schedule_helper

    @staticmethod
    def get_all_schedules():
        schedules = Schedule.query.all()
        return [Schedule_Mapper.model_to_helper(s) for s in schedules]

    @staticmethod
    def get_schedules_by_farmer_id(farmer_id: int):
        schedules = (
            db.session.query(Schedule)
            .join(Farm)
            .filter(Farm.farmer_id == farmer_id)
            .all()
        )

        return [Schedule_Mapper.model_to_helper(s) for s in schedules]
    
    


from app.repositories.schedule_repository import save_schedule, get_all_schedules
from app.mappers.schedule_mapper import map_to_schedule
from datetime import date, timedelta

class ScheduleService:

    @staticmethod
    def create_schedule(data):
        schedule = map_to_schedule(data)
        return save_schedule(schedule)

    @staticmethod
    def get_due_schedules():
        today = date.today()
        tomorrow = today + timedelta(days=1)
        result = []

        for s in get_all_schedules():
            due_date = s.farm.sowing_date + timedelta(days=s.days_after_sowing)
            if due_date in [today, tomorrow]:
                result.append({
                    "farm_id": s.farm_id,
                    "fertiliser": s.fertiliser,
                    "due_date": due_date.isoformat()
                })

        return result

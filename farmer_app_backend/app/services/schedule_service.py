from datetime import date, timedelta
from app.models.schedule import Schedule
from app.repositories.schedule_repository import save_schedule, get_all_schedules

def create_schedule(data):
    required_fields = ["days_after_sowing", "fertiliser", "quantity", "unit", "farm_id"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")

    schedule = Schedule(
        days_after_sowing=data["days_after_sowing"],
        fertiliser=data["fertiliser"],
        quantity=data["quantity"],
        unit=data["unit"],
        farm_id=data["farm_id"]
    )

    return save_schedule(schedule)

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

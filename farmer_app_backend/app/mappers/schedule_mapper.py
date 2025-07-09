from app.models.schedule import Schedule
from app.repositories import farm_repository


def validate_required_fields(data, required):
    missing = [f for f in required if f not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")

def map_to_schedule(data):
    validate_required_fields(data, ["days_after_sowing", "fertiliser", "quantity", "unit", "farm_id"])

    if not farm_repository.exists_by_id(data["farm_id"]):
        raise ValueError("Invalid farm_id: Farm does not exist.")

    return Schedule(
        days_after_sowing=data["days_after_sowing"],
        fertiliser=data["fertiliser"],
        quantity=data["quantity"],
        unit=data["unit"],
        farm_id=data["farm_id"]
    )

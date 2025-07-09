from datetime import datetime
from app.models.farm import Farm
from app.repositories import farmer_repository


def validate_required_fields(data, required):
    missing = [f for f in required if f not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")

def map_to_farm(data):
    validate_required_fields(data, ["area", "village", "crop", "sowing_date", "farmer_id"])

    if not farmer_repository.exists_by_id(data["farmer_id"]):
        raise ValueError("Invalid farmer_id: Farmer does not exist.")

    try:
        sowing_date = datetime.strptime(data["sowing_date"], "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid sowing_date format. Use YYYY-MM-DD.")

    return Farm(
        area=data["area"],
        village=data["village"],
        crop=data["crop"],
        sowing_date=sowing_date,
        farmer_id=data["farmer_id"]
    )

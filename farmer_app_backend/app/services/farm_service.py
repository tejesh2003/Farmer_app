from datetime import datetime
from app.models.farm import Farm
from app.repositories import farm_repository

def create_farm(data):
    required_fields = ["area", "village", "crop", "sowing_date", "farmer_id"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")

    try:
        sowing_date = datetime.strptime(data["sowing_date"], "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD for 'sowing_date'.")

    farm = Farm(
        area=data["area"],
        village=data["village"],
        crop=data["crop"],
        sowing_date=sowing_date,
        farmer_id=data["farmer_id"]
    )

    return farm_repository.save_farm(farm)

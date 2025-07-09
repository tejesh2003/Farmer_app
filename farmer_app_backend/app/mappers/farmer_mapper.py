import re
from app.models.farmer import Farmer
from app.services.country_service import get_or_create_country
from app.repositories import farmer_repository


def validate_required_fields(data, required):
    missing = [f for f in required if f not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")

def validate_phone(phone):
    if not re.fullmatch(r"^\d{10}$", phone):
        raise ValueError("Phone number must be a 10-digit numeric string.")
    if farmer_repository.farmer_exists_by_phone(phone):
        raise ValueError("Phone number already exists.")

def map_to_farmer(data):
    validate_required_fields(data, ["name", "phone", "language", "country"])
    validate_phone(data["phone"])
    country = get_or_create_country(data["country"])

    return Farmer(
        name=data["name"],
        phone=data["phone"],
        language=data["language"],
        country_id=country.id
    )

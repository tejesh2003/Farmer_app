import re
from app.repositories.farmer_repository import FarmerRepository
from app.repositories.user_repository import UserRepository

class ValidationUtils:

    @staticmethod
    def validate_required_fields(data, required_fields):
        missing = [field for field in required_fields if field not in data]
        if missing:
            raise ValueError(f"Missing fields: {', '.join(missing)}")

    @staticmethod
    def validate_phone_number(phone):
        if not re.fullmatch(r"^\d{10}$", phone):
            raise ValueError("Phone number must be a 10-digit numeric string.")
        if FarmerRepository.farmer_exists_by_phone(phone):
            raise ValueError("Phone number already exists.")
        
    @staticmethod
    def user_exists_by_user_name(user_name):
        if UserRepository.user_exists_by_user_name(user_name):
            raise ValueError("User Name already exists.")

from app.models.farmer import Farmer
from app.database import db
from app.mappers.farmer_mapper import Farmer_Mapper

class FarmerRepository:

    @staticmethod
    def save_farmer(farmer_helper):
        farmer_model=Farmer_Mapper.helper_to_model(farmer_helper)
        db.session.add(farmer_model)
        db.session.commit()
        new_farmer_helper=Farmer_Mapper.model_to_helper(farmer_model)
        return new_farmer_helper

    @staticmethod
    def farmer_exists_by_phone(phone):
        return Farmer.query.filter_by(phone=phone).first() is not None

    @staticmethod
    def get_farmers_by_ids(farmer_ids: list[int]):
        farmers = Farmer.query.filter(Farmer.id.in_(farmer_ids)).all()
        return [Farmer_Mapper.model_to_helper(farmer) for farmer in farmers]

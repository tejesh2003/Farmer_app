# app/repositories/country_repository.py

from app.models.country import Country
from app.database import db
from app.mappers.country_mapper import Country_Mapper

class CountryRepository:

    @staticmethod
    def get_by_name(country_name: str):
        country_model = Country.query.filter_by(country_name=country_name).first()
        return Country_Mapper.model_to_helper(country_model) if country_model else None

    @staticmethod
    def save(country_helper):
        country_model = Country_Mapper.helper_to_model(country_helper)
        db.session.add(country_model)
        db.session.commit()
        return Country_Mapper.model_to_helper(country_model)

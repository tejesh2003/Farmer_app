# app/repositories/country_repository.py

from app.models import Country
from app.database import db
from app.mappers import Country_Mapper

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

    @staticmethod
    def get_by_id(country_id: int):
        country_model = Country.query.get(country_id)
        return Country_Mapper.model_to_helper(country_model) if country_model else None

    @staticmethod
    def get_all_countries():
        countries = Country.query.all()
        return [Country_Mapper.model_to_helper(country) for country in countries]

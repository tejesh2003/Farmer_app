from app.repositories import CountryRepository
from app.helpers import Country as CountryHelper


class CountryService:

    @staticmethod
    def get_country(country_name):
        
        country_helper = CountryRepository.get_by_name(country_name)
        return CountryHelper.to_dict(country_helper)
    

    @staticmethod
    def create_country(country_name):
        data={
            "country_name":country_name
        }
        new_country_helper=CountryHelper.from_dict(data)
        final_country_helper = CountryRepository.save(new_country_helper)
        return CountryHelper.to_dict(final_country_helper)
    
    @staticmethod
    def get_country_by_id(country_id):
        country_helper = CountryRepository.get_by_id(country_id)
        return CountryHelper.to_dict(country_helper)
    
    @staticmethod
    def get_all_countries():
        country_helpers = CountryRepository.get_all_countries()
        if not country_helpers:
            return []
    
        return [{"id": country.id, "country_name": country.country_name} for country in country_helpers]


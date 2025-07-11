from app.models.country import Country
from app.repositories.country_repository import CountryRepository
from app.helpers.country_helper import Country as CountryHelper


class CountryService:

    @staticmethod
    def get_or_create_country(country_name):
        
        country_helper = CountryRepository.get_by_name(country_name)

        if country_helper:
            return CountryHelper.to_dict(country_helper)
        data={
            "country_name":country_name
        }
        new_country_helper=CountryHelper.from_dict(data)
        final_country_helper = CountryRepository.save(new_country_helper)
        return CountryHelper.to_dict(final_country_helper)

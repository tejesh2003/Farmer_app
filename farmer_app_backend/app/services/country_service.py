from app.models.country import Country
from app.repositories import country_repository as repo

def get_or_create_country(country_name):
    country = repo.get_by_name(country_name)
    if country:
        return country
    
    country = Country(country_name=country_name)
    return repo.save(country)

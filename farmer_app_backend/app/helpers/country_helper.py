from typing import Optional, List
from app.helpers import Farmer

class Country:
    def __init__(
        self,
        country_name : str,
        farmers : Optional[List[Farmer]]=None,
        id : Optional[int]= None,
    ):
        self.id=id
        self.country_name=country_name
        self.farmers=farmers if farmers is not None else []
        
    def to_dict(self)->dict:
        return{
            "id":self.id,
            "country_name":self.country_name,
            "farmers": [Farmer.to_dict(farmer) for farmer in self.farmers]
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Country":
        farmers_data = data.get("farmers", [])
        farmers = [Farmer.from_dict(farmer_dict) for farmer_dict in farmers_data]

        return cls(
            country_name=data["country_name"],
            id=data.get("id"),
            farmers=farmers,
        )
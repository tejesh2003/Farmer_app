from typing import List, Optional
from app.helpers import Farm

class Farmer:
    def __init__(
        self,
        name : str ,
        phone : str,
        language : str,
        country_id : int,
        farms : Optional[List[Farm]]= None,
        id : Optional[int]= None,
    ):
        self.id=id
        self.name=name
        self.phone = phone
        self.language=language
        self.country_id=country_id
        self.farms=farms if farms is not None else []

    def to_dict(self) ->dict:
        return{
            "id":self.id,
            "name":self.name,
            "phone":self.phone,
            "language":self.language,
            "country_id":self.country_id,
            "farms": [Farm.to_dict(farm) for farm in self.farms]
        }
    @classmethod
    def from_dict(cls, data:dict)->"Farmer":
        farms_data= data.get("farms",[])
        farms= [Farm.from_dict(farm_dict) for farm_dict in farms_data]
        return cls(
            id=data.get("id"),
            name=data["name"],
            language=data["language"],
            phone=data["phone"],
            country_id=data["country_id"],
            farms=farms
        )

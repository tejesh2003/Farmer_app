from typing import List, Optional

class Farmer:
    def __init__(
        self,
        id : Optional[int]= None,
        name : str = "",
        phone : str= "",
        language : str = "",
        country_id : int =0,
        farms : Optional[List[int]]= None,
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
            "language":self.language,
            "country_id":self.country_id,
        }
    @staticmethod
    def from_dict(data:dict):
        return Farmer(
            name=data["name"],
            language=data["language"],
            phone=data["phone"],
            country_id=data["country_id"],
        )

from typing import Optional, List

class Country:
    def __init__(
        self,
        id : Optional[int]= None,
        country_name : str = "",
        farmers : Optional[List[int]]=None
    ):
        self.id=id
        self.country_name=country_name
        self.farmers=farmers if farmers is not None else []
        
    def to_dict(self)->dict:
        return{
            "id":self.id,
            "country_name":self.country_name
        }
    
    @staticmethod
    def from_dict(data:dict):
        return Country(
            country_name=data["country_name"]
        )
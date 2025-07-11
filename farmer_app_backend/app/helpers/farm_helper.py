from typing import List, Optional
from datetime import date

class Farm:
    def __init__(
        self,
        id: Optional[int]=None,
        area: float = 0.0,
        village: str="",
        crop: str = "",
        sowing_date: date = None,
        farmer_id: int = 0,
        schedules : Optional[List[int]]= None,
    ):
        self.id=id
        self.area=area
        self.village = village
        self.crop = crop
        self.sowing_date = sowing_date
        self.farmer_id = farmer_id
        self.schedules=schedules if schedules is not None else []
    
    def to_dict(self)->dict:
        return {
            "id": self.id,
            "area": self.area,
            "village": self.village,
            "crop": self.crop,
            "sowing_date": self.sowing_date.isoformat() if self.sowing_date else None,
            "farmer_id": self.farmer_id
        }
    
    @staticmethod
    def from_dict(data:dict):
        return Farm(
            area=data["area"],
            village=data["village"],
            crop=data["crop"],
            sowing_date=data["sowing_date"],
            farmer_id=data["farmer_id"]
        )
        
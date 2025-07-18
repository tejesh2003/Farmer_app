from typing import List, Optional
from datetime import date
from app.helpers import Schedule

class Farm:
    def __init__(
        self,
        area: float,
        village: str,
        crop: str,
        sowing_date: date,
        farmer_id: int,
        schedules : Optional[List[Schedule]]= None,
        id: Optional[int]=None,
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
            "farmer_id": self.farmer_id,
            "schedules": [Schedule.to_dict(schedule) for schedule in self.schedules]
        }
    
    @classmethod
    def from_dict(cls, data:dict)->"Farm":
        schedules_data=data.get("schedules",[])
        schedules=[Schedule.from_dict(schedule_dict) for schedule_dict in schedules_data]
        return cls(
            id=data.get("id"),
            area=data["area"],
            village=data["village"],
            crop=data["crop"],
            sowing_date=data["sowing_date"],
            farmer_id=data["farmer_id"],
            schedules=schedules
        )
        
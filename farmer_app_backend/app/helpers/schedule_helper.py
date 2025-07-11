from typing import Optional

class Schedule:
    def __init__(
        self,
        id: Optional[int] = None,
        days_after_sowing: int = 0,
        fertiliser: str = "",
        quantity: float = 0.0,
        unit: str = "",
        farm_id: int = 0
    ):
        self.id = id
        self.days_after_sowing = days_after_sowing
        self.fertiliser = fertiliser
        self.quantity = quantity
        self.unit = unit
        self.farm_id = farm_id

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "days_after_sowing": self.days_after_sowing,
            "fertiliser": self.fertiliser,
            "quantity": self.quantity,
            "unit": self.unit,
            "farm_id": self.farm_id
        }

    @staticmethod
    def from_dict(data: dict):
        return Schedule(
            days_after_sowing=data["days_after_sowing"],
            fertiliser=data["fertiliser"],
            quantity=data["quantity"],
            unit=data["unit"],
            farm_id=data["farm_id"]
        )

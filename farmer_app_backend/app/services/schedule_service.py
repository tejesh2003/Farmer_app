from datetime import date, timedelta, datetime
from app.repositories.schedule_repository import ScheduleRepository
from app.helpers.schedule_helper  import Schedule as ScheduleHelper
from app.services.farm_service import FarmService

class ScheduleService:

    @staticmethod
    def create_schedule(days_after_sowing: int, fertiliser: str, quantity: float, unit: str, farm_id: int):
        
        data = {
        "days_after_sowing": days_after_sowing,
        "fertiliser": fertiliser,
        "quantity": quantity,
        "unit": unit,
        "farm_id": farm_id

        }

        schedule_helper= ScheduleHelper.from_dict(data)

        new_schedule_helper= ScheduleRepository.save_schedule(schedule_helper)

        schedule_dict=ScheduleHelper.to_dict(new_schedule_helper)

        return schedule_dict

    @staticmethod
    def get_due_schedules():
        today = date.today()
        tomorrow = today + timedelta(days=1)
        result = []

        for schedule in ScheduleRepository.get_all_schedules():
            try:
                farm = FarmService.get_farm_by_schedule_id(schedule.id)
            except ValueError:
                continue

            sowing_date = datetime.strptime(farm["sowing_date"], "%Y-%m-%d").date()
            due_date = sowing_date + timedelta(days=schedule.days_after_sowing)

            if due_date in [today, tomorrow]:
                schedule_dict = ScheduleHelper.to_dict(schedule)
                schedule_dict["due_date"] = due_date.isoformat()
                result.append(schedule_dict)

        return result
    
    @staticmethod
    def get_schedules_by_farmer(farmer_id: int):
        return [
            ScheduleHelper.to_dict(helper)
            for helper in ScheduleRepository.get_schedules_by_farmer_id(farmer_id)
        ]

    @staticmethod
    def calculate_bill_for_farmer(farmer_id: int, fertilizer_prices: dict):
        schedules = ScheduleRepository.get_schedules_by_farmer_id(farmer_id)

        if not schedules:
            raise ValueError("No schedules found for this farmer")

        bill = {}
        total_cost = 0.0

        for schedule in schedules:
            fertiliser = schedule.fertiliser
            quantity = float(schedule.quantity)
            unit = schedule.unit

            if unit == "g":
                quantity /= 1000
                standard_unit = "kg"
            elif unit == "ton":
                quantity *= 1000
                standard_unit = "kg"
            elif unit == "mL":
                quantity /= 1000
                standard_unit = "L"
            else:
                standard_unit = unit

            fertilizer_key = f"{fertiliser}_{standard_unit}"
            price_per_unit = fertilizer_prices.get(fertilizer_key, 0.0)

            if fertiliser not in bill:
                bill[fertiliser] = {
                    "total_quantity": 0.0,
                    "unit": standard_unit,
                    "price_per_unit": price_per_unit,
                    "total_cost": 0.0,
                    "farms": []
                }

            bill[fertiliser]["total_quantity"] += quantity
            cost = quantity * price_per_unit
            bill[fertiliser]["total_cost"] += cost
            
            try:
               farm_dict = FarmService.get_farm_by_schedule_id(schedule.id)
            except ValueError:
               continue 

            sowing_date = datetime.strptime(farm_dict["sowing_date"], "%Y-%m-%d").date()
            due_date = sowing_date + timedelta(days=schedule.days_after_sowing)

            bill[fertiliser]["farms"].append({
                "farm_id": schedule.farm_id,
                "crop": farm_dict["crop"],
                "quantity": quantity,
                "due_date": due_date.isoformat()
            })

            total_cost += cost

        return {
            "farmer_id": farmer_id,
            "total_cost": total_cost,
            "fertilizers": bill
        }

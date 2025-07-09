class BillService:

    @staticmethod
    def calculate_bill_for_farmer(farmer, prices_dict):
        total_cost = 0
        for farm in farmer.farms:
            for sched in farm.schedules:
                unit_price = prices_dict.get(sched.fertiliser, 0)
                total_cost += unit_price * sched.quantity
        return total_cost

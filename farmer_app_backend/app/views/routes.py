from flask import Blueprint, request
from app.models.farmer import Farmer
from app.services.farmer_service import FarmerService
from app.services.farm_service import FarmService
from app.services.schedule_service import ScheduleService
from app.services.bill_service import BillService
from app.utils.response_helper import ResponseHelper

main_bp = Blueprint("main", __name__)

# add farmer
@main_bp.route("/farmer", methods=["POST"])
def create_farmer_route():
    try:
        data = request.json
        farmer = FarmerService.create_farmer(data)
        return ResponseHelper.success_response({
            "id": farmer.id,
            "name": farmer.name,
        }, code=201)
    except ValueError as ve:
        return ResponseHelper.error_response(str(ve), code=400)
    except Exception:
        return ResponseHelper.error_response("Something went wrong", code=500)

# add farm (we need to send farmer_id)
@main_bp.route("/farm", methods=["POST"])
def create_farm_route():
    try:
        data = request.json
        farm = FarmService.create_farm(data)
        return ResponseHelper.success_response({
            "id": farm.id,
            "village": farm.village
        }, code=201)
    except ValueError as ve:
        return ResponseHelper.error_response(str(ve), code=400)
    except Exception:
        return ResponseHelper.error_response("Internal server error", code=500)

# add schedule (we need to send the farm_id)
@main_bp.route("/schedule", methods=["POST"])
def create_schedule_route():
    try:
        data = request.json
        schedule = ScheduleService.create_schedule(data)
        return ResponseHelper.success_response({
            "id": schedule.id,
            "fertiliser": schedule.fertiliser
        }, code=201)
    except ValueError as ve:
        return ResponseHelper.error_response(str(ve), code=400)
    except Exception:
        return ResponseHelper.error_response("Internal server error", code=500)

# get all schedules due for tomorrow (ntg need to be sent)
@main_bp.route("/schedules/due", methods=["GET"])
def due_schedules():
    return ResponseHelper.success_response(ScheduleService.get_due_schedules())

# find all farmers who are growing the crop (crop should be sent)
@main_bp.route("/farmers/by-crop", methods=["GET"])
def by_crop():
    crop = request.args.get("crop")
    if not crop:
        return ResponseHelper.error_response("Missing 'crop'", code=400)
    farmers = FarmerService.get_farmers_by_crop(crop)
    return ResponseHelper.success_response([{"name": f.name, "phone": f.phone} for f in farmers])

# given prices calc the bill (prices and farmer_id should be sent)
@main_bp.route("/bill/<int:farmer_id>", methods=["POST"])
def bill(farmer_id):
    try:
        farmer = Farmer.query.get_or_404(farmer_id)
        prices = request.json  # {"Urea": 10.0, "DAP": 25.0}
        total = BillService.calculate_bill_for_farmer(farmer, prices)
        return ResponseHelper.success_response({"farmer": farmer.name, "total_cost": total})
    except Exception:
        return ResponseHelper.error_response("Unable to calculate bill", code=500)

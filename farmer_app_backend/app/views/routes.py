from flask import Blueprint, request, jsonify
from app.database import db
from app.models.farmer import Farmer
from app.models.schedule import Schedule
from app.models.farm import Farm
from datetime import datetime
from app.services.farmer_service import get_farmers_by_crop, create_farmer
from app.services.farm_service import create_farm
from app.services.schedule_service import get_due_schedules, create_schedule
from app.services.bill_service import calculate_bill_for_farmer
from app.utils.response_helper import success_response, error_response

main_bp = Blueprint("main", __name__)

# add farmer

@main_bp.route("/farmer", methods=["POST"])
def create_farmer_route():
    try:
        data = request.json
        farmer = create_farmer(data)
        return jsonify(success_response({
            "id": farmer.id,
            "name": farmer.name,
        })), 201
    except ValueError as ve:
        return jsonify(error_response(str(ve))), 400
    except Exception:
        return jsonify(error_response("Something went wrong")), 500

# add farm (we need to send farmer_id)

@main_bp.route("/farm", methods=["POST"])
def create_farm_route():
    try:
        data = request.json
        farm = create_farm(data)
        return jsonify(success_response({
            "id": farm.id,
            "village": farm.village
        })), 201
    except ValueError as ve:
        return jsonify(error_response(str(ve))), 400
    except Exception:
        return jsonify(error_response("Internal server error")), 500

# add schedule (we need to send the farm_id)


@main_bp.route("/schedule", methods=["POST"])
def create_schedule_route():
    data = request.json
    try:
        schedule = create_schedule(data)
        return jsonify(success_response({
            "id": schedule.id,
            "fertiliser": schedule.fertiliser
        })), 201
    except ValueError as ve:
        return jsonify(error_response(str(ve))), 400
    except Exception:
        return jsonify(error_response("Internal server error")), 500

    
# get all schedules due for tomorrow (ntg need to be sent)

@main_bp.route("/schedules/due", methods=["GET"])
def due_schedules():
    return jsonify(success_response(get_due_schedules()))

# find all farmers who are growing the crop (crop should be sent)

@main_bp.route("/farmers/by-crop", methods=["GET"])
def by_crop():
    crop = request.args.get("crop")
    if not crop:
        return jsonify(error_response("Missing 'crop'")), 400
    farmers = get_farmers_by_crop(crop)
    return jsonify(success_response([{"name": f.name, "phone": f.phone} for f in farmers]))

# given prices calc the bill (prices and farmer_id should be sent)

@main_bp.route("/bill/<int:farmer_id>", methods=["POST"])
def bill(farmer_id):
    farmer = Farmer.query.get_or_404(farmer_id)
    prices = request.json  # {"Urea": 10.0, "DAP": 25.0}
    total = calculate_bill_for_farmer(farmer, prices)
    return jsonify(success_response({"farmer": farmer.name, "total_cost": total}))






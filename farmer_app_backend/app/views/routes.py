from flask import Blueprint, request, jsonify
from app.models.farmer import Farmer
from app.services.farmer_service import FarmerService
from app.services.farm_service import FarmService
from app.services.schedule_service import ScheduleService
from app.utils.response_helper import ResponseHelper
from app.utils.validation_utils import ValidationUtils

main_bp = Blueprint("main", __name__)

# add farmer
@main_bp.route("/farmer", methods=["POST"])
def create_farmer_route():
    try:
        data = request.json

        ValidationUtils.validate_required_fields(data, ["name", "phone", "language", "country"])
        ValidationUtils.validate_phone_number(data["phone"])

        farmer= FarmerService.create_farmer(name=data["name"], language=data["language"],phone=data["phone"],country=data["country"])
        return jsonify(farmer), 201

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 500


# add farm (we need to send farmer_id

@main_bp.route("/farm", methods=["POST"])
def create_farm_route():
    try:
        data = request.json

        ValidationUtils.validate_required_fields(data, [
            "area", "village", "crop", "sowing_date", "farmer_id"
        ])

        farm = FarmService.create_farm(area=data["area"], village=data["village"], crop=data["crop"], sowing_date=data["sowing_date"], farmer_id=data["farmer_id"])

        return jsonify(farm), 201

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        return jsonify({"error": "Something went wrong"}), 500


# add schedule (we need to send the farm_id)
@main_bp.route("/schedule", methods=["POST"])
def create_schedule_route():
    try:
        data = request.json
        ValidationUtils.validate_required_fields(data, [
            "days_after_sowing", "fertiliser", "quantity", "unit", "farm_id"
        ])
        schedule = ScheduleService.create_schedule(**{key: data[key] for key in ["days_after_sowing", "fertiliser", "quantity", "unit", "farm_id"]})

        return jsonify(schedule), 201
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        return jsonify({"error": "Something went wrong"}), 500


# get all schedules due for tomorrow (ntg need to be sent)
@main_bp.route("/schedules/due", methods=["GET"])
def due_schedules():
    try:
        result = ScheduleService.get_due_schedules()
        return jsonify(result), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except Exception:
        return jsonify({"error": "Unable to fetch due schedules"}), 500

# find all farmers who are growing the crop (crop should be sent)
@main_bp.route("/farmers/by-crop", methods=["GET"])
def by_crop():
    crop = request.args.get("crop")
    if not crop:
        return {"error": "Missing 'crop'"}, 400

    farmers = FarmerService.get_farmers_by_crop(crop)

    return farmers, 200


# given prices calc the bill (prices and farmer_id should be sent)
@main_bp.route("/bill/<int:farmer_id>", methods=["POST"])
def bill(farmer_id):
    try:
        prices = request.json
        total = ScheduleService.calculate_bill_for_farmer(farmer_id, prices)
        return jsonify(total), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Unable to calculate bill: {str(e)}"}), 500

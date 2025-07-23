from flask import Blueprint, request, jsonify
from app.services import FarmerService, FarmService, ScheduleService, User_Service
from app.utils.validation_utils import ValidationUtils
from app.models import Role
from flask_jwt_extended import create_access_token , set_access_cookies, unset_jwt_cookies
from app.middlewares.auth import with_jwt_data
import bcrypt


main_bp = Blueprint("main", __name__)

#register
@main_bp.route("/register",methods=["POST"])
def register_user():
    try:
        data=request.json

        if " " in data["user_name"]:
          return {"message": "Username should not contain spaces."}, 400

        ValidationUtils.user_exists_by_user_name(data["user_name"])
        password_hash = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user = User_Service.register_user(user_name=data["user_name"], password_hash=password_hash)
        return jsonify(user), 201

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 500

#login
@main_bp.route("/login", methods=["POST"])
def login():
    try:
        data=request.json
        user=User_Service.get_by_user_name(data["user_name"])

        if not user or not bcrypt.checkpw(data["password"].encode('utf-8'),user["password_hash"].encode('utf-8')):
            raise ValueError("Invalid credentials")
        roles = user.get("roles", ["USER"])
                                   
        access_token = create_access_token(
        identity=str(user["id"]),
        additional_claims={
            "roles": roles,
            "user_name": user["user_name"]
            }
        )

        # response = jsonify({"message": "Login successful"})
        # set_access_cookies(response, access_token) 
        response = jsonify({
          "message": "Login successful",
          "access_token": access_token
        })
        
        return response

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 500

#logout
@main_bp.route("/logout", methods=["POST"])
def logout():
    try:
        return jsonify({"message": "Logout successful"}), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except Exception:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 500



#change roles
@main_bp.route("/add-role", methods=["POST"])
@with_jwt_data(allowed_roles=["ADMIN", "SUPER_USER"])
def add_user_role(jwt_data):
    try:
        data=request.json
        target_user_name=data["user_name"]
        target_role=data["role"]
        
        logged_user_roles = jwt_data.get("roles", [])

        if "ADMIN" in logged_user_roles and target_role == "SUPER_USER":
            return jsonify({"error": "Admins cannot assign super_user role"}), 403
        
        role_obj = Role.query.filter_by(name=target_role).first()
        if not role_obj:
            return jsonify({"error": f"Role '{target_role}' does not exist"}), 400

        
        user=User_Service.get_by_user_name(data["user_name"])

        if not user:
            raise ValueError("User with this UserName does not exist")
        
        updated_user = User_Service.add_user(user_name=target_user_name, role=role_obj)
        return jsonify(updated_user), 201
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 500
    
@main_bp.route("/get-user", methods=["GET"])
@with_jwt_data(allowed_roles=["USER","ADMIN", "SUPER_USER"])
def get_user(jwt_data):
    try:
        user_name=jwt_data.get("user_name",[])
        roles = jwt_data.get("roles", [])
        id=jwt_data.get("sub",[])

        return jsonify({"user_name":user_name, "roles":roles, "id":id}), 201
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 500
    

@main_bp.route("/remove-role", methods=["POST"])
@with_jwt_data(allowed_roles=["ADMIN", "SUPER_USER"])
def remove_user_role(jwt_data):
    try:
        data=request.json
        target_user_name=data["user_name"]
        target_role=data["role"]
        
        logged_user_roles = jwt_data.get("roles", [])

        if "ADMIN" in logged_user_roles and target_role == "SUPER_USER":
            return jsonify({"error": "Admins cannot remove super_user role"}), 403
        
        role_obj = Role.query.filter_by(name=target_role).first()
        if not role_obj:
            return jsonify({"error": f"Role '{target_role}' does not exist"}), 400

        
        user=User_Service.get_by_user_name(data["user_name"])

        if not user:
            raise ValueError("User with this UserName does not exist")
        
        updated_user = User_Service.remove_user(user_name=target_user_name, role=role_obj)
        return jsonify(updated_user), 201
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Something went wrong"}), 500

# add farmer
@main_bp.route("/farmer", methods=["POST"])
@with_jwt_data(allowed_roles=["ADMIN", "SUPER_USER"])
def create_farmer_route(jwt_data):
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
@with_jwt_data(allowed_roles=["ADMIN", "SUPER_USER"])
def create_farm_route(jwt_data):
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
@with_jwt_data(allowed_roles=["ADMIN", "SUPER_USER"])
def create_schedule_route(jwt_data):
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
@with_jwt_data(allowed_roles=["USER", "ADMIN", "SUPER_USER"])
def due_schedules(jwt_data):
    try:
        result = ScheduleService.get_due_schedules()
        return jsonify(result), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except Exception:
        return jsonify({"error": "Unable to fetch due schedules"}), 500

# find all farmers who are growing the crop (crop should be sent)
@main_bp.route("/farmers/by-crop", methods=["GET"])
@with_jwt_data(allowed_roles=["USER", "ADMIN", "SUPER_USER"])
def by_crop(jwt_data):
    crop = request.args.get("crop")
    if not crop:
        return {"error": "Missing 'crop'"}, 400

    farmers = FarmerService.get_farmers_by_crop(crop)

    return farmers, 200


# given prices calc the bill (prices and farmer_id should be sent)
@main_bp.route("/bill/<int:farmer_id>", methods=["POST"])
@with_jwt_data(allowed_roles=["USER", "ADMIN", "SUPER_USER"])
def bill(farmer_id,jwt_data):
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

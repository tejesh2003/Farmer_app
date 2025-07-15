from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from app.utils.route_permissions import ROUTE_ROLE_PERMISSIONS
from flask import jsonify, request

def with_jwt_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        jwt_data = get_jwt()
        user_roles = jwt_data.get("roles", ["USER"]) 
        route_path=request.path
        if "bill" in route_path:
            allowed_route_paths = ROUTE_ROLE_PERMISSIONS.get("/bill", [])
        else:
            allowed_route_paths = ROUTE_ROLE_PERMISSIONS.get(route_path,[])

        if not any(role in allowed_route_paths for role in user_roles):
            return jsonify({"error": "Access forbidden for your roles"}), 403

        return func(jwt_data=jwt_data, *args, **kwargs)
    return wrapper

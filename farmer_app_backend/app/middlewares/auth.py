from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from app.utils.route_permissions import ROUTE_ROLE_PERMISSIONS
from flask import jsonify, request

def with_jwt_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        jwt_data = get_jwt()
        user_role = jwt_data["role"]
        route_path=request.path
        if "bill" in route_path:
            allowed_route_paths = ROUTE_ROLE_PERMISSIONS.get("/bill", [])
        else:
            allowed_route_paths = ROUTE_ROLE_PERMISSIONS.get(route_path,[])

        if user_role not in allowed_route_paths:
            return jsonify({"error": "Access forbidden for the role"}),403

        return func(jwt_data=jwt_data, *args, **kwargs)
    return wrapper

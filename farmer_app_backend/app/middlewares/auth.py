from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify, request

def with_jwt_data(allowed_roles=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            jwt_data=get_jwt()
            user_roles=jwt_data.get("roles",["USER"])

            if allowed_roles and not any (role in allowed_roles for role in user_roles):
                return jsonify({"error": "Access forbidden for your roles"}), 403
            
            return func(jwt_data=jwt_data, *args, **kwargs)
        
        return wrapper
    return decorator
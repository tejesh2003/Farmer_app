from flask import jsonify

class ResponseHelper:

    @staticmethod
    def success(data=None, message="Success", code=200):
        return jsonify({
            "status": "success",
            "message": message,
            "data": data
        }), code

    @staticmethod
    def error(message="An error occurred", code=400, errors=None):
        response = {
            "status": "error",
            "message": message,
            "code": code
        }
        if errors:
            response["errors"] = errors
        return jsonify(response), code

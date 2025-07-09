# app/utils/response_helper.py

def success_response(data, message="Success"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(message, code=400):
    return {
        "status": "error",
        "message": message,
        "code": code
    }

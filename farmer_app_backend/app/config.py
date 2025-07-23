import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/farmer_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    JWT_SECRET_KEY = "BATMAN"

    JWT_TOKEN_LOCATION = ["headers"] 

    # JWT_TOKEN_LOCATION = ["cookies"]
    # JWT_ACCESS_COOKIE_NAME = "access_token_cookie"
    # JWT_COOKIE_CSRF_PROTECT = True
    # JWT_CSRF_IN_COOKIES = True
    # JWT_CSRF_HEADER_NAME = "X-CSRF-TOKEN"
    # JWT_COOKIE_SECURE = False
    # JWT_COOKIE_SAMESITE = "Lax" 
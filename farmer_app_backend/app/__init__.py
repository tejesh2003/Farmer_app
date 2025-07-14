from flask import Flask
from .config import Config
from .database import db
from flask_jwt_extended import JWTManager
from .views.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app) 

    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

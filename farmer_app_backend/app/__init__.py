from flask import Flask
from .config import Config
from .database import db
from flask_jwt_extended import JWTManager
from .views.routes import main_bp
from app.utils.seed_utils import seed_roles
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins=["http://localhost:4200"])

    db.init_app(app)
    JWTManager(app) 

    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()
        seed_roles()

    return app

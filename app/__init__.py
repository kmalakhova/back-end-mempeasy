from flask import Flask
from dotenv import load_dotenv
import os 

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["APP_KEY"] = os.environ.get("APP_KEY")
    app.config["APP_ID"] = os.environ.get("APP_ID")

    from app.routes import app_bp
    app.register_blueprint(app_bp)

    return app

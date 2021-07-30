from flask import Flask
from dotenv import load_dotenv
import os 

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["APP_KEY"] = os.environ.get("APP_KEY")
    app.config["APP_ID"] = os.environ.get("APP_ID")
    return app

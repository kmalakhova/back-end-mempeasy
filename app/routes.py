from flask import Blueprint
from app.password import get_response
from flask import json

app_bp = Blueprint("app", __name__, url_prefix="/")

@app_bp.route("", methods=["GET"], strict_slashes=False)
def start():
    password, hint = (get_response())
    return json.dumps({"password":password, "hint":hint}, indent = 4)

from app.routes import *
import json

def test_start():
    data = start()
    json_data = json.loads(data)
    assert len(json_data) == 2
    assert json_data["password"] != ""
    assert json_data["hint"] != ""
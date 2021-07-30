from flask import app
from password import get_response
from flask import jsonify
from flask import request

@app.route("/")
def home():
    # print("hello")
    return "hello"

@app.route('/get-password', methods=['GET'])
def start_process():
    return jsonify(get_response())

@app.route('/start_process', methods=['GET'])
def start_process():
    return jsonify(get_response())

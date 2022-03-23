import json
from flask import Flask, jsonify, request

app = Flask(__name__)

icecreams = {
    "MrSmith": {"flavour": "Vanilla", "price": 3.50},
    "MrsSmith": {"flavour": "Chocolate", "price": 3.50},
    "Matcha": {"flavour": "Green Tea", "price": 5.50},
}

users = [
    {"name": "Vivian", "email": "vivian.d@gmail.com"},
    {"name": "Erica", "email": "erica.d@gmail.com"},
]


@app.route("/", methods=["GET"])
def index() -> json:
    return jsonify({"message": "Hello, world!"})


@app.route("/flavours", methods=["GET"])
def show_all_flavours() -> json:
    # returns all the values in the icecream_flavours list
    return jsonify({"icecream_flavours": icecreams})


@app.route("/flavours/<string:name>", methods=["GET"])
def show_one_flavour(name: str) -> json:
    """_summary_

    Args:
        name (str): name of the flavour

    Returns:
        _type_: json dict with the specified flavour
    """
    flavours = icecreams[name]
    return jsonify({"icecream": flavours})


@app.route("/signup", methods=["POST"])
def signup() -> json:
    new_user = {"name": request.json["name"], "email": request.json["email"]}
    users.append(new_user)
    return jsonify({"users": users})

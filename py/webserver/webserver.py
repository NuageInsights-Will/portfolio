from flask import Flask, jsonify, url_for, request
from markupsafe import escape

app = Flask(__name__)

icecreams = [{
    "name" : "MrSmith",
    "flavour" : "Vanilla",
    "price" : 3.50
    }, 
    {
    "name" : "MrsSmith",
    "flavour" : "Chocolate",
    "price" : 3.50
    }, 
    {
    "name" : "Matcha",
    "flavour" : "Green Tea",
    "price" : 5.50
    }]

users = [{
    "name" : "Vivian", 
    "email" : "vivian.d@gmail.com"
    }, {
    "name" : "Erica", 
    "email" : "erica.d@gmail.com"
    }]

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message" : "Hello, world!"})

@app.route("/flavours", methods=["GET"])
def show_all_flavours():
    #returns all the values in the icecream_flavours list
    return jsonify({"icecream_flavours" : icecreams})

@app.route("/flavours/<string:name>", methods=["GET"])
def show_one_flavour(name):
    #returns the flavour with the matching name
    flavours = [flavours for flavours in icecreams if flavours["name"] == name]
    return jsonify({"icecream" : flavours[0]})

@app.route("/signup", methods=["POST"])
def signup():
    new_user = {"name" : request.json["name"], "email" : request.json["email"]}
    users.append(new_user)
    return jsonify({"users" : users})
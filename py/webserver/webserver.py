import json
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify#, request, render_template
#from datetime import datetime
import psycopg2

#give our file access to environment variables
load_dotenv(find_dotenv())

app = Flask(__name__)

#function that establishes a connection to our database
def get_db_connection() -> None:
    conn = psycopg2.connect(
            host='pg-db-host',
            port=5432,
            database='postgres',
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'))
    return conn

icecreams = {
    "MrSmith": {"flavour": "Vanilla", "price": 3.50},
    "MrsSmith": {"flavour": "Chocolate", "price": 3.50},
    "Matcha": {"flavour": "Green Tea", "price": 5.50},
}

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


@app.route("/users", methods=["GET"])
def users() -> json:
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM users;")
            users = cur.fetchall()
    return json.dumps(users)


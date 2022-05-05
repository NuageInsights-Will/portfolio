import os
import json
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text as T

#give our file access to environment variables
load_dotenv(find_dotenv())

app = Flask(__name__)

engine = create_engine(os.getenv("CONNECTION_URI"))

@app.route("/", methods=["GET"])
def index():
        return render_template("index.html")

@app.route("/films/<string:id>", methods=["GET"])
def get_film(id):
        with engine.connect() as conn:
                q = T("""
                SELECT title, description, release_date, image FROM ghiblmi.films
                WHERE id = :id
                """)
                results = conn.execute(q, id=id).fetchall()
        return render_template("films.html", title=results[0]["title"], description=results[0]["description"], release_date=results[0]["release_date"], url=results[0]["image"])


@app.route("/search", methods=["GET", "POST"])
def search_page():
        error = ""
        if request.method == 'POST':
                with open("input_log.json", "w") as file:
                        json.dump(request.form, file, indent=4)

                search_input = request.form["search_text"]
                
                if len(search_input) == 0:
                        error = "Not a valid search."
                
                else:
                        with engine.connect() as conn:
                                search_input = '%' + search_input + '%'
                                q = T("""
                                SELECT COUNT (id) FROM ghiblmi.films
                                WHERE LOWER(title) LIKE LOWER(:search_input)
                                """)
                                results = conn.execute(q, search_input=search_input).fetchall()
                                if results[0]["count"] == 0:
                                        error = "No results found."
                                else:
                                        with engine.connect() as conn:
                                                search_input = '%' + search_input + '%'
                                                q = T("""
                                                SELECT id FROM ghiblmi.films
                                                WHERE LOWER(title) LIKE LOWER(:search_input)
                                                LIMIT 1;
                                                """)
                                                results = conn.execute(q, search_input=search_input).fetchall()
                                                id = results[0]["id"]
                                        return get_film(id)
        return render_template("search.html", message=error) #get_film(id)


@app.route("/about", methods=["GET"])
def about_page():
        p1 = """
        This website was built by "William T." as an educational tool 
        to provide users with an image, description, and release year
        for Studio Ghibli films via a simple search function.
        """
        p2 = """
        Ghiblmi's database is populated with data from the open source 
        herokuapp "Studio Ghibli API". Please note that the information 
        on this site may be inaccurate.
        """
        p3 = """
        Disclaimer: This site is not in any way affiliated with
        Studio Ghibli Inc. All intellectual property rights belong to their
        respective owner(s).
        """
        return render_template("about.html", p1=p1, p2=p2, p3=p3)
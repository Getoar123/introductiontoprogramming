# Implements a registration form, storing registrants in a SQLite database, with support for deregistration

from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return render_template("error.html", message="Missing name")

    if not sport:
        return render_template("error.html", message="Missing sport")

    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    db.execute(
        "INSERT INTO registrants (name, sport) VALUES(?, ?)",
        name,
        sport
    )

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=rows)


@app.route("/deregister", methods=["POST"])
def deregister():

    registrant_id = request.form.get("id")

    if registrant_id:
        db.execute("DELETE FROM registrants WHERE id = ?", registrant_id)

    return redirect("/registrants")

from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

SPORTS = ["Soccer", "Basketball", "Tennis", "Volleyball"]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return render_template("error.html", message="Name is required")

    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport selected")

    # INSERT INTO DATABASE (NEW PART)
    db.execute(
        "INSERT INTO registrants (name, sport) VALUES (?, ?)",
        name,
        sport
    )

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=rows)

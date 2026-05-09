from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = ["Soccer", "Basketball", "Tennis", "Volleyball"]

# in-memory storage (this is NEW)
registrants = []


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name or sport not in SPORTS:
        return "Invalid registration", 400

    # store in memory
    registrants.append({"name": name, "sport": sport})

    return redirect("/registrants")


@app.route("/registrants")
def show_registrants():
    return render_template("registrants.html", registrants=registrants)

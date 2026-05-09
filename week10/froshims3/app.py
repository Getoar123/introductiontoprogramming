from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Soccer", "Basketball", "Tennis", "Volleyball"]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    # validation
    if not name:
        return render_template("error.html", message="Name is required")

    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport selected")

    return render_template("success.html", name=name, sport=sport)

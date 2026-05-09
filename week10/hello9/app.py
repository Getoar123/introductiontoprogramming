from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # default value
    name = "world"

    # if form submitted (POST)
    if request.method == "POST":
        name = request.form.get("name", "world")

    # if query string used (GET)
    elif request.method == "GET" and request.args.get("name"):
        name = request.args.get("name")

    return render_template("index.html", name=name)


@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "world")
    return render_template("greet.html", name=name)

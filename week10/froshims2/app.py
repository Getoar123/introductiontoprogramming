from flask import Flask, request

app = Flask(__name__)

SPORTS = ["Soccer", "Basketball", "Tennis", "Volleyball"]


@app.route("/", methods=["GET"])
def index():
    # simple HTML with radio buttons
    html = """
    <h1>Register for a Sport</h1>

    <form action="/register" method="post">

        <input name="name" type="text" placeholder="Name">

        <h3>Select a sport:</h3>
    """

    for sport in SPORTS:
        html += f'''
        <label>
            <input type="radio" name="sport" value="{sport}">
            {sport}
        </label><br>
        '''

    html += """
        <button type="submit">Register</button>
    </form>
    """

    return html


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return "Registration failed: Name is required"

    if sport not in SPORTS:
        return "Registration failed: Invalid sport selected"

    return f"Success! {name} registered for {sport}"

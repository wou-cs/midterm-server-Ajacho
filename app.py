from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<int:number>", methods=["GET"])
def get_calcs(number):
    # First calc: decrement the number
    dec = number - 1
    hex_value = hex(number)

    # Second calc: convert to hex
    response = {
        "dec": dec,
        "hex": hex_value
    }
    return response, 200

@app.errorhandler(404)
def handle_bad_request(e):
    return {"error": "Bad Request"}, 400
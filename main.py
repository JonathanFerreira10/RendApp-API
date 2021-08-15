from flask                 import Flask, request
from flask_cors            import CORS
from calculatevalueinvoice import calculateValueInvoice

app = Flask("RendApp")
CORS(app)
cors = CORS(app, resources = {
    r"/*":{
        "origins": "*"
    }
})

#Route for test
@app.route("/totalvalue", methods=["GET"])
def totalValueInvoice():
    value = 2
    return {"value": value}

@app.route("/receivevalue", methods = ["POST"])
def receiveValueInvoice():
    body = request.get_json()
    newinv = calculateValueInvoice(body["valueInvoice"], body["income"])
    return newinv

app.run()
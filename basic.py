from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/name", methods = ["GET"])
def name():
    name = {
        "name": "Martin"
    }
    return jsonify(name)

@app.route("/hello/<name>", methods = ["GET"])
def hello(name):
    helloMessage = {
        "message": "hello there, {0}".format(name)
    }
    return jsonify(helloMessage)

@app.route("/distance", methods = ["POST"])
def distance():
    import math
    r = request.get_json()
    x1 = r["a"][0]
    x2 = r["b"][0]
    y1 = r["a"][1]
    y2 = r["b"][1]
    c = math.sqrt(math.pow((x1-x2),2) + math.pow(y1-y2,2))

    dist = {
        "distance" : c ,
        "a" : [x1,y1] ,
        "b" : [x2,y2]
    }
    return jsonify(dist)

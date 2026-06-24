from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return {
        "a": a,
        "b": b,
        "operation": "addition",
        "result": a + b
    }


@app.route("/subtract")
def subtract():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return {
        "a": a,
        "b": b,
        "operation": "subtraction",
        "result": a - b
    }


@app.route("/multiply")
def multiply():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return {
        "a": a,
        "b": b,
        "operation": "multiplication",
        "result": a * b
    }


app.run(port=5000)
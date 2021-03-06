
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def auth():
    print("The raw Authorization header", request.environ["HTTP_AUTHORIZATION"])
    print("Flask's Authorization header", request.authorization)
    return ""


if __name__ == "__main__":
    app.run()
    

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/person/<person_id>")
def my_microservice(person_id):
    return jsonify({"Hello": person_id})


if __name__ == "__main__":
    app.run()
    
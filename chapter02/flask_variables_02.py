
import typing as t
from flask import Flask, jsonify
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {"1": "Tarek", "2": "Freya"}
_IDS = {val: id for id, val in _USERS.items()}

class RegisteredUser(BaseConverter):
    
    def to_python(self, value: str) -> t.Any:
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()
    
    def to_url(self, value: t.Any) -> str:
        return _IDS[value]

app = Flask(__name__)
app.url_map.converters["registered"] = RegisteredUser

@app.route("/api/person/<registered:name>")
def person(name):
    return jsonify({"Hello hey": name})


if __name__ == "__main__":
    app.run()
    
import time
from flask import Flask, jsonify, request, Response, abort


app = Flask(__name__)


def _time2etag(stamp=None):
    if stamp is None:
        stamp = time.time()  # Return the current time in seconds since the Epoch.
    return str(int(stamp * 1000))


_USERS = {"1": {"name": "Tarek", "modified": _time2etag()}}


@app.route("/api/user/<user_id>", methods=["POST"])
def change_user(user_id):
    print(request)
    
    user = request.json
    user["modified"] = _time2etag()
    _USERS[user_id] = user
    resp = jsonify(user)
    resp.set_etag(user["modified"])
    return resp


@app.route("/api/user/<user_id>")
def get_user(user_id):
    if user_id not in _USERS:
        return abort(404)
    user = _USERS[user_id]
    
    if user["modified"] in request.if_none_match:
        return Response(status=304)
    
    resp = jsonify(user)
    resp.set_etag(user["modified"])
    return resp


if __name__ == "__main__":
    app.run()

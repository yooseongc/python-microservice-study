import logging
import graypy
import json
from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException, _aborter


app = Flask(__name__)


def error_handling(error):
    if isinstance(error, HTTPException):
        result = {"code": error.code, "description": error.description}
    else:
        description = _aborter.mapping[500].description
        result = {"code": 500, "description": description}
        
    app.logger.exception(f"예외 발생! {error}", extra=result)
    result["message"] = str(error)
    resp = jsonify(result)
    resp.status_code = result["code"]
    return resp


for code in _aborter.mapping:
    app.register_error_handler(code, error_handling)
    
    
@app.route("/api", methods=["GET", "POST"])
def my_microservice():
    app.logger.info("Graylog에 info 로그 기록")
    resp = jsonify({"result": "OK", "Hello": "World!"})
    
    raise Exception("BAHM")
    return resp


if __name__ == "__main__":
    handler = graypy.GELFUDPHandler("localhost", 12201)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()

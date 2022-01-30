import functools
import logging
import graypy
import json
import time
import random
from collections import defaultdict, deque
from flask import Flask, jsonify, g


app = Flask(__name__)


class Encoder(json.JSONEncoder):
    
    def default(self, obj):
        base = super(Encoder, self).default
        
        if isinstance(obj, deque):
            calls = list(obj)
            return {"num_calls": len(calls), 
                    "min": min(calls), 
                    "max": max(calls),
                    "values": calls}
        
        return base(obj)


def timeit(func):
    
    @functools.wraps(func)
    def _timeit(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            if "timers" not in g:
                g.timers = defaultdict(functools.partial(deque, maxlen=5))
            g.timers[func.__name__].append(time.time() - start)
    
    return _timeit


@timeit
def fast_stuff():
    time.sleep(.001)
    

@timeit
def some_slow_stuff():
    time.sleep(random.randint(1, 100) / 100.)


def set_view_metrics(view_func):
    
    @functools.wraps(view_func)
    def _set_view_metrics(*args, **kwargs):
        try:
            return view_func(*args, **kwargs)
        finally:
            app.logger.info(json.dumps(dict(g.timers), cls=Encoder))
            
    return _set_view_metrics


def set_app_metrics(app: Flask):
    for endpoint, func in app.view_functions.items():
        app.view_functions[endpoint] = set_view_metrics(func)
        
        
@app.route("/api", methods=["GET", "POST"])
def my_microservice():
    some_slow_stuff()
    for _ in range(12):
        fast_stuff()
        resp = jsonify({"result": "OK", "Hello": "World!"})
        fast_stuff()
    return resp


if __name__ == "__main__":
    handler = graypy.GELFUDPHandler("localhost", 12201)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    set_app_metrics(app)
    app.run()

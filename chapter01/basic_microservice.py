
import json
import time
from wsgiref.simple_server import make_server


def application(environ, start_response):
    headers = [('Content-Type', 'application/json')]
    start_response('200 OK', headers)
    return [bytes(json.dumps({'time': time.time()}), 'utf8')]


if __name__ == '__main__':
    
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
    
    

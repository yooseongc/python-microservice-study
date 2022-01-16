
import json
import time
from wsgiref.simple_server import make_server
from gevent import monkey; monkey.patch_all()


def application(environ, start_response):
    headers = [('Content-type', 'application/json')]
    start_response('200 OK', headers)
    # 소켓으로 필요한 작업을 한다.
    return [bytes(json.dumps({'time': time.time()}), 'utf8')]

if __name__ == '__main__':
    
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()

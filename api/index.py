from app import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Request, Response

# Convert Flask app to WSGI application
wsgi_app = DispatcherMiddleware(app)

def handler(request, response):
    req = Request(request.environ)
    res = Response.from_app(wsgi_app, req.environ)
    response.status_code = res.status_code
    for k, v in res.headers:
        response.headers[k] = v
    response.set_body(res.get_data())

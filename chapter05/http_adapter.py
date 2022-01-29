from requests.adapters import HTTPAdapter
from requests import Session, PreparedRequest, Response


class HTTPTimeoutAdapter(HTTPAdapter):
    
    def __init__(self, *args, **kwargs) -> None:
        self.timeout = kwargs.pop("timeout", 30.)
        super().__init__(*args, **kwargs)
        
    def send(self, request: PreparedRequest, **kwargs) -> Response:
        """
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        """
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def setup_connector(app, name="default", **options):
    
    if not hasattr(app, "extensions"):
        app.extensions = {}
        
    if "connectors" not in app.extensions:
        app.extensions["connectors"] = {}
    
    session = Session()
    
    if "auth" in options:
        session.auth = options["auth"]
    
    headers = options.get("headers", {})
    
    if "Content-Type" not in headers:
        headers["Content-Type"] = "application/json"
        
    session.headers.update(headers)
    
    retries = options.get("retries", 3)
    timeout = options.get("timeout", (5.0, 3.0))
    
    adapter = HTTPTimeoutAdapter(max_retries=retries, timeout=timeout)
    # Registers a connection adapter to a prefix.
    # Adapters are sorted in descending order by prefix length.
    session.mount("http://", adapter=adapter)
    app.extensions["connectors"][name] = session
    
    return session


def get_connector(app, name="default"):
    
    return app.extensions["connectors"][name]

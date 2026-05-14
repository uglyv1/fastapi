class HttpRequest:
    def __init__(
            self, 
            body: dict = None, 
            headers: dict = None, 
            path_params: dict = None
        ):
        self.body = body
        self.headers = self.headers

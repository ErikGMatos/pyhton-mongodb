class HttpRequest:
    def __init__(
            self,
            body: dict = None,
            headers: dict = None,
            params: dict = None

    ):
        self.body = body
        self.headers = headers
        self.params = params

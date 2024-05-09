class ClientNotImplemented(Exception):
    def __init__(self, method):
        self.method = method

    def __repr__(self):
        return f"{self.method} not implemented"


class InvalidUrl(Exception):
    pass

class RequestError(Exception):
    def __init__(self, status_code : int = 0, message : str = "connection error"):
        self.status_code = status_code
        self.message = str

    def __repr__(self) -> str:
        return f"status_code: {self.status_code}, message: {self.message}"

    def __str__(self) -> str:
        return self.__repr__()

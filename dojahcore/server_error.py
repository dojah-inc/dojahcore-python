class ServerError(Exception):
    def __init__(self, message) -> None:
        self.message = message
from typing import TypeVar, TypedDict



T = TypeVar('T')

class Request:
    def __init__(self, body : T, ):
        self.body = body




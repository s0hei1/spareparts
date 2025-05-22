from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

class HttpBadRequest(HTTPException):
    def __init__(self, message: str = "Bad Request"):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=message)

from pydantic import BaseModel


class SuccessResponse(BaseModel):
    message : str | None = 'The Process was Successful'

class DeleteResponse(BaseModel):
    id : int
    message : str = "The Delete Process was Successful"
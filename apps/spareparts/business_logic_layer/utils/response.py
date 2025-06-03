from pydantic import BaseModel


class SuccessResponse(BaseModel):
    message : str | None = 'The Process was Successful'

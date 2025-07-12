from pydantic import BaseModel

class LoginSchema(BaseModel):
    user_name: str
    password: str


class Token(BaseModel):
    token: str
    token_type: str = "bearer"


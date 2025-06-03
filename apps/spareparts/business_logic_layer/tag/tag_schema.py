from pydantic import BaseModel


class TagCreate(BaseModel):
    title: str


class TagUpdate(BaseModel):
    id: int
    title: str | None = None


class TagRead(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class TagDeleteRead(BaseModel):
    id: int
    message: str = "Tag deleted successfully"

    class Config:
        orm_mode = True

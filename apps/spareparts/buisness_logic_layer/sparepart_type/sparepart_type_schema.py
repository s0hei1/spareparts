from pydantic import BaseModel


class SparePartTypeCreate(BaseModel):
    name: str


class SparePartTypeUpdate(BaseModel):
    id: int
    name: str | None = None


class SparePartTypeRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SparePartTypeDeleteRead(BaseModel):
    id: int
    message: str = "Spare part type deleted successfully"

    class Config:
        orm_mode = True

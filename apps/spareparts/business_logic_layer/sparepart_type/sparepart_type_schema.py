from pydantic import BaseModel

from apps.spareparts.business_logic_layer.property.property_schema import PropertyCreate, PropertyRead
from apps.spareparts.data_layer.models.sparepart import SparePartType


class SparePartTypeCreate(BaseModel):
    name: str
    properties_id : list[int]


    def to_sparepart_type(self):
        return SparePartType(
            name = self.name,
        )



class SparePartTypeUpdate(BaseModel):
    id: int
    name: str | None = None

class SparePartTypeCreationRead(BaseModel):
    id: int
    name: str
    properties: list[PropertyRead]

    class Config:
        orm_mode = True


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

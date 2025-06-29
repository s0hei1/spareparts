from pydantic import BaseModel

from apps.spareparts.business_logic_layer.property.property_schema import PropertyCreate, PropertyRead
from apps.spareparts.data_layer.models.sparepart import SparePartType


class SparePartTypeCreate(BaseModel):
    name: str
    properties_id : list[int] = []
    symbol : str


    def to_sparepart_type(self):
        return SparePartType(
            name = self.name,
            symbol = self.symbol,
        )



class SparePartTypeUpdate(BaseModel):
    id: int
    name: str | None = None



class SparePartTypeRead(BaseModel):
    id: int
    name: str
    symbol : str
    properties: list['SparePartTypePropertiesRead']



    class Config:
        from_attributes = True



class SparePartTypeDeleteRead(BaseModel):
    id: int
    message: str = "Spare part type deleted successfully"

    class Config:
        from_attributes = True

class SparePartTypePropertiesRead(BaseModel):
    property_id: int

    class Config:
        from_attributes = True

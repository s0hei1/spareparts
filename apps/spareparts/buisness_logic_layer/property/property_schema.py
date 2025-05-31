from pydantic import BaseModel

from apps.spareparts.data.enums.property_value_type import PropertyValueType
from apps.spareparts.data.models.sparepart import Property


class PropertyCreate(BaseModel):
    name: str
    value_type: PropertyValueType
    unit_of_measure_id: int

    def to_property(self):
        return Property(
            name = self.name,
            value_type = self.value_type,
            unit_of_measure_id = self.unit_of_measure_id,
        )


class PropertyUpdate(BaseModel):
    id: int
    name: str | None = None
    value_type: PropertyValueType | None = None
    unit_of_measure_id: int | None = None


class PropertyRead(BaseModel):
    id: int
    name: str
    value_type: PropertyValueType
    unit_of_measure_id: int

    class Config:
        orm_mode = True


class PropertyDeleteRead(BaseModel):
    id: int
    message: str = "Property deleted successfully"

    class Config:
        orm_mode = True

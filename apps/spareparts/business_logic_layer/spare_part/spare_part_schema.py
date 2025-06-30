from pydantic import BaseModel
from typing import ForwardRef, Any

from apps.spareparts.data_layer.models.sparepart import SparePart, SparePartPropertyValue

SparePartCreatePartNumbers = ForwardRef('SparePartCreatePartNumbers')
SparePartCreateLocation = ForwardRef('SparePartCreateLocation')
SparePartCreateProperty = ForwardRef('SparePartCreateProperty')


class SparePartCreate(BaseModel):
    name: str
    alias_name: str | None = None
    spare_part_type_id: int
    part_numbers: list[SparePartCreatePartNumbers] | None = None
    machines_using_parts: list[int] | None = None
    location: SparePartCreateLocation | None = None
    properties: list[SparePartCreateProperty] | None = None

    def to_sparepart(self, code: str):
        return SparePart(
            name=self.name,
            alias_name=self.alias_name,
            spare_part_type_id=self.spare_part_type_id,
            code=code
        )


class SparePartCreatePartNumbers(BaseModel):
    part_number: str
    company_id: str


class SparePartCreateLocation(BaseModel):
    x: str
    y: str
    floor: str


class SparePartCreateProperty(BaseModel):
    property_id: int
    property_value: Any


class SparePartUpdate(BaseModel):
    id: int
    name: str | None = None
    alias_name: str | None = None
    code: str | None = None


class SparePartRead(BaseModel):
    id: int
    name: str
    alias_name: str | None
    spare_part_type_id: int
    code: str

    class Config:
        from_attributes = True


class SparePartDeleteRead(BaseModel):
    id: int
    message: str = "Delete spare part was successful"

    class Config:
        from_attributes = True


class SparePartPropertyValueCreate(BaseModel):
    spare_part_type_property_id: int
    spare_part_id: int
    value: Any

    def to_spare_part_property_value(self) -> SparePartPropertyValue:
        return SparePartPropertyValue(
            spare_part_type_property_id=self.spare_part_type_property_id,
            spare_part_id=self.spare_part_id,
            value=self.value,
        )


class SparePartPropertyValueRead(BaseModel):
    id: int
    sparepart_id: str
    property_name: str
    property_id: str
    value: Any
    property_uom: str

    class Config:
        from_attributes = True

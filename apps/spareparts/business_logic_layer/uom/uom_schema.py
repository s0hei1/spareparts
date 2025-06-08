from pydantic import BaseModel, computed_field
from typing import Optional, Sequence

from apps.spareparts.data_layer.models.sparepart import UnitOfMeasure, UnitOfMeasureGroup


class UnitOfMeasureCreate(BaseModel):
    name : str
    unit_in_group : float | None = None
    group_id : int


    def to_unit_of_measure(self) -> UnitOfMeasure:
        return UnitOfMeasure(
            name=self.name,
            unit_in_group=self.unit_in_group,
            group_id=self.group_id,
        )

class UnitOfMeasureGroupCreate(BaseModel):
    name : str

    def to_unit_of_measure_group(self) -> UnitOfMeasureGroup:
        return UnitOfMeasureGroup(
            name =self.name
        )


class UnitOfMeasureRead(BaseModel):
    id : int
    name : str
    unit_in_group : float | None
    group_name : str


    class Config:
        from_attributes = True

    @classmethod
    def from_unit_of_measure(cls, unit_of_measure: UnitOfMeasure) -> 'UnitOfMeasureRead':
        return UnitOfMeasureRead(
            id = unit_of_measure.id,
            name = unit_of_measure.name,
            unit_in_group= unit_of_measure.unit_in_group,
            group_name = unit_of_measure.group.name,
        )

    @classmethod
    def from_unit_of_measures(cls,unit_of_measures : Sequence[UnitOfMeasure] ) -> Sequence['UnitOfMeasureRead']:
        result = [cls.from_unit_of_measure(uom) for uom in unit_of_measures]
        return result


class UnitOfMeasureUpdate(BaseModel):
    id : int
    name : str
    unit_in_group : float | None = None
    group_id : int | None = None


class UnitOfMeasureGroupRead(BaseModel):
    id : int
    name : str

class UnitOfMeasureGroupDelete(BaseModel):

    id: int
    message: str = "UOM Group is deleted successfully"

    class Config:
            from_attributes = True

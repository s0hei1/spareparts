from pydantic import BaseModel, computed_field
from typing import Optional

from apps.spareparts.data_layer.models.sparepart import UnitOfMeasure, UnitOfMeasureGroup


class UnitOfMeasureCreate(BaseModel):
    name : str
    unit_in_group : float | None = None
    group_id : Optional[int] = None

    model_config = {
        "from_attributes": True,
    }

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
    name : str
    unit_in_group : float | None
    # group_name : str
    #
    # @computed_field
    # @property
    # def group_name(self) -> str:
    #     return self.__pydantic_self__.group.name

    class Config:
        from_attributes = True



class UnitOfMeasureUpdate(BaseModel):
    id : int
    name : str
    unit_in_group : float | None = None
    group_id : int | None = None


class UnitOfMeasureGroupRead(BaseModel):
    name : str
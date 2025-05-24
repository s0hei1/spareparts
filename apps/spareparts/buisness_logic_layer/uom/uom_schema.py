from pydantic import BaseModel, computed_field
from typing import Optional

from apps.spareparts.data.models.sparepart import UnitOfMeasure


class UnitOfMeasureCreate(BaseModel):
    name : str
    unit_in_group : float | None = None
    newGroupName : str | None = None
    groupId : Optional[int] = None

    model_config = {
        "from_attributes": True,
    }

    def to_unit_of_measure(self) -> UnitOfMeasure:
        return UnitOfMeasure(
            name=self.name,
            unit_in_group=self.unit_in_group,
            group_id=self.groupId,
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


    model_config = {
        "from_attributes": True,
    }

from pydantic import BaseModel, computed_field


class UnitOfMeasureCreate(BaseModel):
    name : str
    unit_in_group : float | None
    newGroupName : str | None
    groupId : int | None

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

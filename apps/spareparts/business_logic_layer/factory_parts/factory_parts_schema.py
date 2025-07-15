from pydantic import BaseModel,Field
from typing import Annotated, TypeVar
from apps.spareparts.data_layer.models.sparepart import FactoryPart


NameField = Annotated[str, Field(min_length=1, max_length=256)]
ParentIdField = Annotated[int, Field(gt=0)]
DescriptionField = Annotated[str, Field(min_length=1, max_length=1024)]

class FactoryPartCreate(BaseModel):
    name : NameField
    parent_id : ParentIdField | None = None
    description : DescriptionField | None = None


    def to_factory_part(self) -> FactoryPart:
        return FactoryPart(
            name=self.name,
            parentId=self.parent_id,
            description=self.description,
        )

class FactoryPartRead(BaseModel):
    id : int
    name : str
    description : str | None = None


    class Config:
        from_attributes = True

class FactoryPartUpdate(BaseModel):
    id : int
    name : NameField | None = None
    parent_id : ParentIdField | None = None
    description : DescriptionField | None = None

class FactoryPartDelete(BaseModel):
    id : int
    message : str = "Delete factory part was successful"
    class Config:
        from_attributes = True



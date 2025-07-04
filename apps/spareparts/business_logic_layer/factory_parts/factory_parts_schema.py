from pydantic import BaseModel

from apps.spareparts.data_layer.models.sparepart import FactoryPart


class FactoryPartCreate(BaseModel):
    name : str
    parentId : int | None = None
    description : str | None = None


    def to_factory_part(self) -> FactoryPart:
        return FactoryPart(
            name=self.name,
            parentId=self.parentId,
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
    name : str | None = None
    parentId : int | None = None
    description : str | None = None

class FactoryPartDelete(BaseModel):
    id : int
    message : str = "Delete factory part was successful"
    class Config:
        from_attributes = True



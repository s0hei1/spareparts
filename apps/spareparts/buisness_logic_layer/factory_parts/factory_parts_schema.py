from pydantic import BaseModel

from apps.spareparts.data.models.sparepart import FactoryParts


class FactoryPartCreate(BaseModel):
    name : str
    parentId : int | None = None
    description : str | None = None


    def to_factory_part(self) -> FactoryParts:
        return FactoryParts(
            name=self.name,
            parentId=self.parentId,
            description=self.description,
        )

class FactoryPartRead(BaseModel):
    id : int
    name : str
    description : str | None = None


    class Config:
        orm_mode = True

class FactoryPartUpdate(BaseModel):
    id : int
    name : str | None = None
    parentId : int | None = None
    description : str | None = None

class FactoryPartDelete(BaseModel):
    id : int
    message : str = "Delete factory part was successful"
    class Config:
        orm_mode = True



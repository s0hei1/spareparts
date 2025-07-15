from typing import Annotated

from pydantic import BaseModel, Field
from apps.spareparts.data_layer.models.sparepart import MachineCatalog

MachineNameField = Annotated[str, Field(min_length=1, max_length=256)]
LocationInFactoryField = Annotated[str, Field(min_length=1, max_length=256)]
FactoryPartId = Annotated[int, Field(gt=0)]
DescriptionField = Annotated[str, Field(max_length=512)]
ModelNameField = Annotated[str, Field(min_length=1, max_length=128)]
IsToolField = Annotated[bool, Field()]


class MachineCatalogCreate(BaseModel):
    machine_name: MachineNameField
    location_in_factory: LocationInFactoryField | None = None
    factory_part_id: FactoryPartId | None = None
    description: DescriptionField | None = None
    model_name: ModelNameField
    is_tool: IsToolField

    def to_machine_catalog(self) -> MachineCatalog:
        return MachineCatalog(
            machine_name=self.machine_name,
            location_in_factory=self.location_in_factory,
            factory_part_id=self.factory_part_id,
            description=self.description,
            model_name=self.model_name,
            is_tool=self.is_tool,
        )


class MachineCatalogRead(BaseModel):
    id: int
    machine_name: str
    location_in_factory: str | None
    description: str | None
    model_name: str
    is_tool: bool

    class Config:
        from_attributes = True


class MachineCatalogUpdate(BaseModel):
    id: int
    machine_name: MachineNameField | None = None
    location_in_factory: LocationInFactoryField | None = None
    factory_part_id: FactoryPartId | None = None
    description: DescriptionField | None = None
    model_name: ModelNameField | None = None
    is_tool: IsToolField | None = None


class MachineCatalogDeleteRead(BaseModel):
    id: int
    message: str = "Delete machine catalog was successful"

    class Config:
        from_attributes = True

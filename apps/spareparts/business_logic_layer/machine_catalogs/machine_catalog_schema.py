from pydantic import BaseModel

from apps.spareparts.data_layer.models.sparepart import MachineCatalog


class MachineCatalogCreate(BaseModel):
    machine_name : str
    location_in_factory : str | None = None
    factory_part_id : int | None = None
    description : str | None = None
    model_name : str
    is_tool : bool

    def to_machine_catalog(self) -> MachineCatalog:
        return MachineCatalog(
            machine_name = self.machine_name,
            location_in_factory = self.location_in_factory,
            factory_parts_id = self.factory_part_id,
            description = self.description,
            model_name = self.model_name,
            is_tool = self.is_tool,
        )


class MachineCatalogRead(BaseModel):
    id : int
    machine_name : str
    location_in_factory : str | None
    description : str | None
    model_name : str
    is_tool : bool

class MachineCatalogUpdate(BaseModel):
    id : int
    machine_name : str | None = None
    location_in_factory : str | None = None
    factory_part_id : str | None = None
    description : str | None = None
    model_name : str | None = None
    is_tool : bool | None = None

class MachineCatalogDeleteRead(BaseModel):
    id : int
    message : str = "Delete machine catalog was successful"
    class Config:
        orm_mode = True


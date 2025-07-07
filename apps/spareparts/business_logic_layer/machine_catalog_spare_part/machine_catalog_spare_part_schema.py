from psycopg2._psycopg import Float
from pydantic import BaseModel

from apps.spareparts.data_layer.models.sparepart import MachineCatalogSparePart


class MachineCatalogSparePartCreate(BaseModel):

    spare_part_id : int
    machine_catalog_id : int
    usage_ration : float

    def to_machine_catalog_spare_part(self):
        return MachineCatalogSparePart(
            spare_part_id=self.spare_part_id,
            machine_catalog_id=self.machine_catalog_id,
            usage_ration=self.usage_ration,
        )

class MachineCatalogSparePartRead(BaseModel):
    id : int
    spare_part_id : int
    machine_catalog_id : int
    usage_ration : float | None
    class Config:
        from_attributes = True

class MachineCatalogSparePartUpdate(BaseModel):
    id : int
    spare_part_id : int | None = None
    machine_catalog_id : int | None = None
    usage_ration : float | None = None

class MachineCatalogSparePartDelete(BaseModel):
    id : int
    message : str = "MachineCatalogSparePart deleted successfully"
    class Config:
        from_attributes = True
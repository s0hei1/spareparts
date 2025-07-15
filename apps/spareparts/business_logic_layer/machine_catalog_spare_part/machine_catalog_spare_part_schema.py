from typing import Annotated

from psycopg2._psycopg import Float
from pydantic import BaseModel, Field

from apps.spareparts.data_layer.models.sparepart import MachineCatalogSparePart

SparePartIDField = Annotated[int, Field(gt=0)]
MachineCatalogIDField = Annotated[int, Field(gt=0)]
UsageRationField = Annotated[float, Field(gt=0)]


class MachineCatalogSparePartCreate(BaseModel):
    spare_part_id: SparePartIDField
    machine_catalog_id: MachineCatalogIDField
    usage_ration: UsageRationField

    def to_machine_catalog_spare_part(self):
        return MachineCatalogSparePart(
            spare_part_id=self.spare_part_id,
            machine_catalog_id=self.machine_catalog_id,
            usage_ration=self.usage_ration,
        )


class MachineCatalogSparePartRead(BaseModel):
    id: int
    spare_part_id: int
    machine_catalog_id: int
    usage_ration: float | None

    class Config:
        from_attributes = True


class MachineCatalogSparePartUpdate(BaseModel):
    id: int
    spare_part_id: SparePartIDField | None = None
    machine_catalog_id: MachineCatalogIDField | None = None
    usage_ration: UsageRationField | None = None


class MachineCatalogSparePartDelete(BaseModel):
    id: int
    message: str = "MachineCatalogSparePart deleted successfully"

    class Config:
        from_attributes = True

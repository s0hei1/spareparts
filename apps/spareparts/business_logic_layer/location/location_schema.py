from pydantic import BaseModel, Field

from apps.spareparts.data_layer.models.sparepart import Location
from typing import Annotated, TypeVar

ShelfField = Annotated[str, Field(min_length=1, max_length=8)]
ColumnField = Annotated[int, Field(gt=1, lt=100)]
RowField = Annotated[int, Field(gt=1, lt=10)]
FloorField = Annotated[int | None, Field(gt=1, lt=10)]

class LocationCreate(BaseModel):
    shelf: ShelfField
    column: ColumnField
    row: RowField
    floor: FloorField | None= None

    def to_location(self) -> Location:
        return Location(
            shelf=self.shelf,
            column=self.column,
            row=self.row,
            floor=self.floor,
        )

class LocationUpdate(BaseModel):
    id: int
    shelf: ShelfField | None = None
    column: ColumnField | None = None
    row: RowField | None = None
    floor: FloorField | None = None

class LocationRead(BaseModel):
    shelf: str
    column: int
    row: int
    floor: int | None

    class Config:
        from_attributes = True

# --- DELETE RESPONSE MODEL ---
class LocationDeleteRead(BaseModel):
    id: int
    message: str = "Delete location was successful"

    class Config:
        from_attributes = True
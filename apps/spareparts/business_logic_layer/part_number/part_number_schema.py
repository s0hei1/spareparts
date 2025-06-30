from pydantic import BaseModel

from apps.spareparts.data_layer.models.sparepart import PartNumber


class PartNumberCreate(BaseModel):
    part_number: str
    spare_part_id: int
    company_id: int

    def to_part_number(self) -> PartNumber:
        return PartNumber(
            part_number=self.part_number,
            spare_part_id=self.spare_part_id,
            company_id=self.company_id,
        )

class PartNumberRead(BaseModel):
    id : int
    part_number: str
    spare_part_id: int
    company_id: int

    class Config:
        from_attributes = True

class PartNumberUpdate(BaseModel):
    id : int
    part_number: str | None = None
    spare_part_id: int | None = None
    company_id: int | None = None

class PartNumberDelete(BaseModel):
    id : int
    message : str = "Delete part number was successful"

    class Config:
        from_attributes = True
from pydantic import BaseModel

class PartNumber(BaseModel):
    partNumber : str
    companyId : int

class Location(BaseModel):
    x : str
    y : str
    z : str
    floor : str | None = None

class SparePartsCreate(BaseModel):
    wareHouseId : int
    persianName : str
    englishName : str | None = None
    machineIds : list[int]
    sparePartGroupId : int
    partNumbers : list[PartNumber] | None = None
    location : Location | None
    uomId : int

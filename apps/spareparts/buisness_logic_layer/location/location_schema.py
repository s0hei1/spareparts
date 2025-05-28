from pydantic import BaseModel

from apps.spareparts.data.models.sparepart import Location


class LocationCreate(BaseModel):
    x: str
    y: str
    z: str
    floor: int | None = None

    def to_location(self) -> Location:
        return Location(
            x=self.x,
            y=self.y,
            z=self.z,
            floor=self.floor,
        )


class LocationUpdate(BaseModel):
    id: int
    x: str | None = None
    y: str | None = None
    z: str | None = None
    floor: int | None = None


class LocationRead(BaseModel):
    x: str
    y: str
    z: str
    floor: int | None

    class Config:
        orm_mode = True


class LocationDeleteRead(BaseModel):
    id: int
    message: str = "Delete location was successful"

    class Config:
        orm_mode = True

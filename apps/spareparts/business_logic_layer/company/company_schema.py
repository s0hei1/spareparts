from pydantic import BaseModel,EmailStr, HttpUrl
from apps.spareparts.data_layer.models.sparepart import Company


class CompanyCreate(BaseModel):
    name: str
    location: str
    description: str
    website: HttpUrl | None = None
    contactEmail: EmailStr | None = None

    def to_company(self):
        return Company(
            name=self.name,
            location=self.location,
            description=self.description,
            website=str(self.website),
            contactEmail=str(self.contactEmail),
        )


class CompanyRead(BaseModel):
    id : int
    name: str
    location: str
    description: str
    website: str | None = None
    contactEmail: str | None = None

    class Config:
        from_attributes = True


class CompanyUpdate(BaseModel):
    id: int
    name: str | None = None
    location: str | None = None
    description: str | None = None
    website: HttpUrl | None = None
    contactEmail: EmailStr | None = None

class CompanyDelete(BaseModel):
    id: int
    message : str = "Company deleted successfully"

    class Config:
        from_attributes = True

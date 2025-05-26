from pydantic import BaseModel

from apps.spareparts.data.models.sparepart import Company


class CompanyCreate(BaseModel):
    name: str
    location: str
    description: str
    website: str | None = None
    contactEmail: str | None = None

    def to_company(self):
        return Company(
            name=self.name,
            location=self.location,
            description=self.description,
            website=self.website,
            contactEmail=self.contactEmail,
        )


class CompanyRead(BaseModel):
    name: str
    location: str
    description: str
    website: str | None = None
    contactEmail: str | None = None

    class Config:
        orm_mode = True


class CompanyUpdate(BaseModel):
    id: int
    name: str | None = None
    location: str | None = None
    description: str | None = None
    website: str | None = None
    contactEmail: str | None = None

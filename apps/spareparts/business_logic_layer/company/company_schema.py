from pydantic import BaseModel,EmailStr, HttpUrl,Field
from sqlalchemy.sql.coercions import AnonymizedFromClauseImpl

from apps.spareparts.data_layer.models.sparepart import Company
from typing import Annotated

IdField= Annotated[int, Field(gt=0)]
NameField = Annotated[str, Field(min_length=1, max_length=156)]
LocationField = Annotated[str, Field(min_length=1, max_length=156)]
DescriptionField = Annotated[str, Field(min_length=1, max_length=1024)]

class CompanyCreate(BaseModel):
    name: NameField
    location: LocationField
    description: DescriptionField
    website: HttpUrl | None = None
    contact_email: EmailStr | None = None

    def to_company(self):
        return Company(
            name=self.name,
            location=self.location,
            description=self.description,
            website=str(self.website),
            contact_email=str(self.contact_email),
        )


class CompanyRead(BaseModel):
    id : int
    name: str
    location: str
    description: str
    website: str | None = None
    contact_email: str | None = None

    class Config:
        from_attributes = True


class CompanyUpdate(BaseModel):
    id : IdField
    name: NameField | None = None
    location: LocationField | None = None
    description: DescriptionField | None = None
    website: HttpUrl | None = None
    contact_email: EmailStr | None = None

class CompanyDelete(BaseModel):
    id: int
    message : str = "Company deleted successfully"

    class Config:
        from_attributes = True

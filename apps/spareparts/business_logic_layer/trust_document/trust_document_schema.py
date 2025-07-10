from pydantic import BaseModel
from datetime import date
from apps.spareparts.data_layer.models.sparepart import TrustDocument

class TrustDocumentCreate(BaseModel):
    delivery_date: date
    return_date: date
    description: str
    personal_name: str

    def to_trust_document(self):
        return TrustDocument(
            delivery_date=self.delivery_date,
            return_date=self.return_date,
            description=self.description,
            personal_name=self.personal_name,
        )

class TrustDocumentUpdate(BaseModel):
    id : int
    delivery_date: date | None = None
    return_date: date | None = None
    description: str | None = None
    personal_name: str | None = None

class TrustDocumentRead(BaseModel):
    id : int
    delivery_date: date
    return_date: date
    description: str
    personal_name: str

    class Config:
        from_attributes = True
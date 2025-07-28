from pydantic import BaseModel
from apps.spareparts.business_logic_layer.utils import IdField


class SuccessResponse(BaseModel):
    message : str | None = 'The Process was Successful'

class DeleteResponse(BaseModel):
    id : IdField
    message : str = "The Delete Process was Successful"
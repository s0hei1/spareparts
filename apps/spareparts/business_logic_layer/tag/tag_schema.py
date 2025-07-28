from pydantic import BaseModel,Field
from typing import Annotated

from apps.spareparts.business_logic_layer.utils import ShortTextField,IdField
from apps.spareparts.data_layer.models.sparepart import Tag


class TagCreate(BaseModel):
    title: ShortTextField
    title_alias: ShortTextField | None = None

    def to_tag(self):
        return Tag(
            title = self.title,
        title_alias = self.title_alias,
        )


class TagUpdate(BaseModel):
    id: IdField
    title_alias: ShortTextField | None = None
    title: ShortTextField | None = None


class TagRead(BaseModel):
    id: IdField
    title: ShortTextField | None = None
    title_alias: ShortTextField | None = None

    class Config:
        from_attributes = True



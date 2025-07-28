from sqlalchemy import select

from apps.spareparts.business_logic_layer.tag.tag_schema import TagRead, TagCreate
from apps.spareparts.data_layer.core.read_only_async_session import ReadOnlyAsyncSession
from apps.spareparts.data_layer.models.sparepart import Tag


class TagBLL:


    def __init__(self, db: ReadOnlyAsyncSession):
        self.db = db








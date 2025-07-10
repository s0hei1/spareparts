from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from apps.spareparts.data_layer.models.sparepart import TrustDocument


class TrustDocumentRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, trust_document: TrustDocument) -> TrustDocument:
        self.db.add(trust_document)
        await self.db.commit()
        await self.db.refresh(trust_document)

        return trust_document

    async def read_one(self, id: int) -> TrustDocument:
        q = select(TrustDocument).where(TrustDocument.id == id)
        query_result = await self.db.execute(q)
        obj = query_result.scalar_one_or_none()

        if obj is None:
            raise NoResultFound(f"Document with id {id} does not exist")

        return obj

    async def read_many(self) -> Sequence[TrustDocument]:
        q = select(TrustDocument)
        query_result = await self.db.execute(q)
        objs = query_result.scalars().all()

        return objs

    async def update(self,
                     id: int,
                     delivery_date: datetime | None,
                     return_date: datetime | None,
                     description: str | None,
                     personal_name: str | None,
                     ) -> TrustDocument:
        obj = await self.read_one(id)

        if delivery_date is not None :
            obj.delivery_date = delivery_date
        if return_date is not None :
            obj.return_date = return_date
        if description is not None :
            obj.description = description
        if personal_name is not None :
            obj.personal_name = personal_name

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> TrustDocument:
        obj = await self.read_one(id)
        await self.db.delete(obj)
        await self.db.commit()
        return obj
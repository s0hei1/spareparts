from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from apps.spareparts.data_layer.models.sparepart import SparePart


class SparePartRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> SparePart:
        q = await self.db.execute(
            select(SparePart).where(SparePart.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePart with id {id} not found")
        return obj

    async def read_many(self) -> Sequence[SparePart]:
        q = await self.db.execute(select(SparePart))
        return q.scalars().all()

    async def create(self, spare_part: SparePart) -> SparePart:
        self.db.add(spare_part)
        await self.db.commit()
        await self.db.refresh(spare_part)
        return spare_part

    async def update(
        self,
        id: int,
        name: str | None = None,
        alias_name: str | None = None,
        sparePartType: int | None = None,
        code: str | None = None,
    ) -> SparePart:
        q = await self.db.execute(
            select(SparePart).where(SparePart.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePart with id {id} not found")

        if name is not None:
            obj.name = name
        if alias_name is not None:
            obj.alias_name = alias_name
        if sparePartType is not None:
            obj.sparePartType = sparePartType
        if code is not None:
            obj.code = code

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> SparePart:
        q = await self.db.execute(
            select(SparePart).where(SparePart.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePart with id {id} not found")

        await self.db.delete(obj)
        await self.db.commit()
        return obj

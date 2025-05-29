from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from apps.spareparts.data.models.sparepart import SparePartType


class SparePartTypeRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> SparePartType:
        q = await self.db.execute(select(SparePartType).where(SparePartType.id == id))
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePartType with id {id} does not exist")
        return obj

    async def read_many(self) -> Sequence[SparePartType]:
        q = await self.db.execute(select(SparePartType))
        return q.scalars().all()

    async def create(self, spare_part_type: SparePartType) -> SparePartType:
        self.db.add(spare_part_type)
        await self.db.commit()
        await self.db.refresh(spare_part_type)
        return spare_part_type

    async def update(self, id: int, name: str | None = None) -> SparePartType:
        q = await self.db.execute(select(SparePartType).where(SparePartType.id == id))
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePartType with id {id} does not exist")

        if name is not None:
            obj.name = name

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> SparePartType:
        q = await self.db.execute(select(SparePartType).where(SparePartType.id == id))
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePartType with id {id} does not exist")

        await self.db.delete(obj)
        await self.db.commit()
        return obj

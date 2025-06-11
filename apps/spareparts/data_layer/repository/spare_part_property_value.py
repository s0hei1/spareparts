from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from apps.spareparts.data_layer.models.sparepart import SparePartPropertyValue


class SparePartPropertyValueRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> SparePartPropertyValue:
        q = await self.db.execute(
            select(SparePartPropertyValue).where(SparePartPropertyValue.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePartPropertyValue with id {id} not found")
        return obj

    async def read_many(self) -> Sequence[SparePartPropertyValue]:
        q = await self.db.execute(select(SparePartPropertyValue))
        return q.scalars().all()

    async def create(self, obj: SparePartPropertyValue) -> SparePartPropertyValue:
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def update(
        self,
        id: int,
        spare_part_type_property_id: int | None = None,
        spare_part_id: int | None = None,
        value: str | None = None,
    ) -> SparePartPropertyValue:
        q = await self.db.execute(
            select(SparePartPropertyValue).where(SparePartPropertyValue.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePartPropertyValue with id {id} not found")

        if spare_part_type_property_id is not None:
            obj.spare_part_type_property_id = spare_part_type_property_id
        if spare_part_id is not None:
            obj.spare_part_id = spare_part_id
        if value is not None:
            obj.value = value

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> SparePartPropertyValue:
        q = await self.db.execute(
            select(SparePartPropertyValue).where(SparePartPropertyValue.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePartPropertyValue with id {id} not found")

        await self.db.delete(obj)
        await self.db.commit()
        return obj

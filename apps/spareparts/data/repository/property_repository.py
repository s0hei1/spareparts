
from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from apps.spareparts.data.models.sparepart import Property


class PropertyRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> Property:
        q = await self.db.execute(
            select(Property).where(Property.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"Property with id {id} does not exist")
        return obj

    async def read_many(self) -> Sequence[Property]:
        q = await self.db.execute(select(Property))
        return q.scalars().all()

    async def create(self, property_obj: Property) -> Property:
        self.db.add(property_obj)
        await self.db.commit()
        await self.db.refresh(property_obj)
        return property_obj

    async def update(
        self,
        id: int,
        name: str | None = None,
        value_type: str | None = None,
        unit_of_measure_id: int | None = None,
    ) -> Property:
        q = await self.db.execute(
            select(Property).where(Property.id == id)
        )
        obj: Property | None = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"Property with id {id} does not exist")

        if name is not None:
            obj.name = name
        if value_type is not None:
            obj.value_type = value_type
        if unit_of_measure_id is not None:
            obj.unit_of_measure_id = unit_of_measure_id

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> Property:
        q = await self.db.execute(
            select(Property).where(Property.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"Property with id {id} does not exist")

        await self.db.delete(obj)
        await self.db.commit()
        return obj

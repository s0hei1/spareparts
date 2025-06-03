from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data_layer.models.sparepart import Location


class LocationRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> Location:
        q = await self.db.execute(
            select(Location).where(Location.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"Location with id: {id} does not exist")
        return obj

    async def read_many(self) -> Sequence[Location]:
        q = await self.db.execute(select(Location))
        return q.scalars().all()

    async def create(self, location: Location) -> Location:
        self.db.add(location)
        await self.db.commit()
        await self.db.refresh(location)
        return location

    async def update(
        self,
        id: int,
        x: str | None = None,
        y: str | None = None,
        z: str | None = None,
        floor: int | None = None
    ) -> Location:
        q = await self.db.execute(
            select(Location).where(Location.id == id)
        )
        obj: Location | None = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Location with id: {id} does not exist")

        if x is not None:
            obj.x = x
        if y is not None:
            obj.y = y
        if z is not None:
            obj.z = z
        if floor is not None:
            obj.floor = floor

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> Location:
        q = await self.db.execute(
            select(Location).where(Location.id == id)
        )
        obj = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Location with id: {id} does not exist")

        await self.db.delete(obj)
        await self.db.commit()
        return obj
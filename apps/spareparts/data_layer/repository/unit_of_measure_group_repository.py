from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data_layer.models.sparepart import UnitOfMeasureGroup


class UnitOfMeasureGroupRepository:

    def __init__(self, db : AsyncSession):
        self.db = db

    async def read_many(self) -> Sequence[UnitOfMeasureGroup] | None:
        q = select(UnitOfMeasureGroup)
        result = await self.db.execute(q)
        return result.scalars().all()

    async def read_one(self, id: int) -> UnitOfMeasureGroup:
        q = select(UnitOfMeasureGroup).where(UnitOfMeasureGroup.id == id)
        result = await self.db.execute(q)
        instance =  result.scalar_one_or_none()

        if not instance:
            raise NoResultFound(f"Unit Of Measure Group with id: {id} does not exist")

        return instance

    async def create(self, uom_group: UnitOfMeasureGroup) -> UnitOfMeasureGroup:
        print("Hii")
        self.db.add(uom_group)
        await self.db.commit()
        await self.db.refresh(uom_group)
        return uom_group

    async def update(
        self,
        id: int,
        name: str | None = None,
    ) -> UnitOfMeasureGroup:
        q = select(UnitOfMeasureGroup).where(UnitOfMeasureGroup.id == id)
        result = await self.db.execute(q)
        obj = result.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Unit of measure group with id: {id} does not exist")

        if name is not None:
            obj.name = name

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    # async def delete(self, id: int) -> UnitOfMeasureGroup:
    #     pass


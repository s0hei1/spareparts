from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound
from apps.spareparts.data.models.sparepart import UnitOfMeasure, UnitOfMeasureGroup


class UnitOfMeasureRepository():

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_by_id(self, id : int) -> UnitOfMeasure:
        q = select(UnitOfMeasure).where(UnitOfMeasure.id == id)
        instance = (await self.db.execute(q)).scalar_one_or_none()
        if not instance:
            raise NoResultFound(f"Unit of measure with id: {id} does not exist")

        return instance


    async def read_all(self) -> Sequence[UnitOfMeasure] | None:
        q = select(UnitOfMeasure, UnitOfMeasureGroup)
        result = await self.db.execute(q)
        instances = result.scalars().all()
        return instances


    async def create(self, uom: UnitOfMeasure) -> UnitOfMeasure:
        self.db.add(uom)
        await self.db.commit()
        await self.db.refresh(uom)
        return uom

    async def update(
        self,
        id: int,
        name: str | None = None,
        group_id: int | None = None,
        unit_in_group: float | None = None,
    ) -> UnitOfMeasure:
        q = select(UnitOfMeasure).where(UnitOfMeasure.id == id)
        result = await self.db.execute(q)
        obj = result.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Unit of measure with id: {id} does not exist")

        if name is not None:
            obj.name = name
        if group_id is not None:
            obj.group_id = group_id
        if unit_in_group is not None:
            obj.unit_in_group = unit_in_group

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> int:
        q = select(UnitOfMeasure).where(UnitOfMeasure.id == id)
        result = await self.db.execute(q)
        instance = result.scalar_one_or_none()

        if not instance:
            raise NoResultFound(f"Unit of measure with id: {id} does not exist")

        await self.db.delete(instance)
        await self.db.commit()
        return id

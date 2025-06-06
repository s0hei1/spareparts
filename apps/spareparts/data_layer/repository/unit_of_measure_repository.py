from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.orm.exc import NoResultFound
from apps.spareparts.data_layer.models.sparepart import UnitOfMeasure, UnitOfMeasureGroup


class UnitOfMeasureRepository():

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id : int) -> UnitOfMeasure:
        q = select(UnitOfMeasure).options(selectinload(UnitOfMeasure.group)).where(UnitOfMeasure.id == id)

        obj = (await self.db.execute(q)).scalar_one_or_none()
        if obj is None:
            raise NoResultFound(f"Unit of measure with id: {id} does not exist")

        return obj


    async def read_many(self) -> Sequence[UnitOfMeasure] | None:
        q = select(UnitOfMeasure).options(selectinload(UnitOfMeasure.group))
        query_result = await self.db.execute(q)
        objs = query_result.scalars().all()
        return objs


    async def create(self, uom: UnitOfMeasure) -> UnitOfMeasure:
        self.db.add(uom)
        await self.db.commit()
        return await self.read_one(uom.id)


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
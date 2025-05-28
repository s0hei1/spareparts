from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from apps.spareparts.data.models.sparepart import MachineCatalog


class MachineCatalogRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> MachineCatalog:
        q = await self.db.execute(
            select(MachineCatalog).where(MachineCatalog.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"Machine catalog with id: {id} does not exist")
        return obj

    async def read_many(self) -> Sequence[MachineCatalog]:
        q = await self.db.execute(
            select(MachineCatalog)
        )
        objs = q.scalars().all()
        return objs

    async def create(self, machine: MachineCatalog) -> MachineCatalog:
        self.db.add(machine)
        await self.db.commit()
        await self.db.refresh(machine)
        return machine

    async def update(
        self,
        id: int,
        machine_name : str | None = None,
        location_in_factory : str | None = None,
        factory_part_id : str | None = None,
        description : str | None = None,
        model_name : str | None = None,
        is_tool : bool | None = None,

    ) -> MachineCatalog:
        q = await self.db.execute(
            select(MachineCatalog).where(MachineCatalog.id == id)
        )
        obj : MachineCatalog | None = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Machine catalog with id: {id} does not exist")

        if machine_name:
            obj.machine_name = machine_name
        if location_in_factory:
            obj.location_in_factory = location_in_factory
        if factory_part_id:
            obj.factory_part_id = factory_part_id
        if description:
            obj.description = description
        if model_name:
            obj.model_name = model_name
        if is_tool:
            obj.is_tool = is_tool

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> MachineCatalog:

        q = await self.db.execute(
            select(MachineCatalog).where(MachineCatalog.id == id)
        )
        obj = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Machine catalog with id: {id} does not exist")

        await self.db.delete(obj)
        await self.db.commit()
        return obj


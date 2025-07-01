from typing import List, Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data_layer.models.sparepart import MachineCatalogSparePart


class MachineCatalogSparePartRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> MachineCatalogSparePart:
        q = await self.db.execute(
            select(MachineCatalogSparePart).where(MachineCatalogSparePart.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"Machine catalog with id: {id} does not exist")
        return obj

    async def read_all(self) -> Sequence[MachineCatalogSparePart]:
        q = select(MachineCatalogSparePart)
        query_result = await self.db.execute(q)
        objs = query_result.scalars().all()

        return objs

    async def create(self, machine_catalog_spare_part: MachineCatalogSparePart):
        self.db.add(machine_catalog_spare_part)
        await self.db.commit()
        await self.db.refresh(machine_catalog_spare_part)

        return machine_catalog_spare_part

    async def update(self,
                     id: int,
                     spare_part_id: int | None = None,
                     machine_catalog_id: int | None = None,
                     usage_ration: int | None = None,
                     ) -> MachineCatalogSparePart:

        obj = await self.read_one(id)

        if spare_part_id is not None:
            obj.spare_part_id = spare_part_id
        if machine_catalog_id is not None:
            obj.machine_catalog_id = machine_catalog_id
        if usage_ration is not None:
            obj.usage_ration = usage_ration

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> MachineCatalogSparePart:
        obj = await self.read_one(id)
        await self.db.delete(obj)
        await self.db.commit()
        await self.db.refresh(obj)

        return obj


from typing import List

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data_layer.models.sparepart import PartNumber


class PartNumberRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> PartNumber:
        q = select(PartNumber).where(PartNumber.id == id)
        query_result = await self.db.execute(q)

        obj = query_result.scalar_one_or_none()

        if obj is None:
            raise NoResultFound(f"Part Number with id: {id} does not exist")

        return obj


    async def read_many(self) -> List[PartNumber]:
        q = select(PartNumber)
        query_result = await self.db.execute(q)
        objs = query_result.scalars().all()
        return objs

    async def create(self, part_number: PartNumber) -> PartNumber:
        self.db.add(part_number)

        await self.db.commit()
        await self.db.refresh(part_number)

        return part_number


    async def update(self,
                     id: int,
                     part_number: str | None = None,
                     spare_part_id: int | None = None,
                     company_id: int | None = None,
                     ) -> PartNumber:
        obj : PartNumber = await self.read_one(id)

        obj.part_number = obj.part_number if part_number is None else part_number
        obj.spare_part_id = obj.spare_part_id if spare_part_id is None else spare_part_id
        obj.company_id = obj.company_id if company_id is None else company_id

        await self.db.commit()
        await self.db.refresh(obj)
        return obj




    async def delete(self, id: int) -> PartNumber:
        obj = await self.read_one(id)

        await self.db.delete(obj)
        await self.db.commit()
        return obj

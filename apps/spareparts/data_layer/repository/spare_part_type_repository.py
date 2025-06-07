from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.orm.exc import NoResultFound

from apps.spareparts.data_layer.models.sparepart import SparePartType, SparePartTypeProperties, Property


class SparePartTypeRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> SparePartType:
        q = (select(SparePartType).
             options(selectinload(SparePartType.properties)).
             where(SparePartType.id == id))
        query_result = await self.db.execute(q)

        obj = query_result.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"SparePartType with id {id} does not exist")
        return obj

    async def read_many(self) -> Sequence[SparePartType]:
        q = select(SparePartType).options(selectinload(SparePartType.properties))
        query_result = await self.db.execute(q)
        return query_result.scalars().all()

    async def create(self, spare_part_type: SparePartType) -> SparePartType:
        self.db.add(spare_part_type)
        await self.db.commit()
        await self.db.refresh(spare_part_type)

        result = await self.read_one(spare_part_type.id)
        return result

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

    async def create_sparepart_type_property(self, sparepart_type_id, property_id) -> SparePartTypeProperties:
        obj = SparePartTypeProperties(
            spare_part_type_id = sparepart_type_id,
            property_id = property_id
        )

        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def read_many_sparepart_type_properties(self, sparepart_type_id : int) -> Sequence[SparePartTypeProperties]:
        q = select(SparePartTypeProperties).where(SparePartTypeProperties.spare_part_type_id == sparepart_type_id)
        query_result = await self.db.execute(q)

        return query_result.scalars().all()


    async def read_many_sparepart_types_properties(self) -> Sequence[SparePartTypeProperties]:
        q = select(SparePartTypeProperties)
        query_result = await self.db.execute(q)

        return query_result.scalars().all()

from typing import Sequence

from sqlalchemy import select, exists
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from apps.spareparts.data_layer.models.sparepart import FactoryPart

class FactoryPartsRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id : int) -> FactoryPart:
        result = await self.db.execute(
            select(FactoryPart).where(FactoryPart.id == id)
        )
        obj = result.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"factory part with id: {id} does not exist")

        return obj

    async def read_many(self) -> Sequence[FactoryPart] | None:
        result = await self.db.execute(
            select(FactoryPart)
        )
        objs = result.scalars().all()

        return objs


    async def create(self, factoryPart: FactoryPart) -> FactoryPart:
        self.db.add(factoryPart)
        await self.db.commit()
        await self.db.refresh(factoryPart)

        return factoryPart

    async def update(self, id: int, name: str | None, parentId: int | None, description: str | None, )\
            -> FactoryPart:
        q = await self.db.execute(
            select(FactoryPart).where(FactoryPart.id == id)
        )

        obj = q.scalar_one_or_none()

        if obj is None:
            raise NoResultFound(f"factory part with id: {id} does not exist")

        if name:
            obj.name = name
        if parentId:
            isExistsFacoryPart = (await self.db.execute(
                select(exists().where(FactoryPart.id == parentId))
            )).scalar()
            if not isExistsFacoryPart:
                raise NoResultFound(f"factory part with id: {id} does not exist to be used as a parent")
            obj.parentId = parentId
        if description:
            obj.description = description

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> FactoryPart:
        result = await self.db.execute(select(FactoryPart).where(FactoryPart.id == id))
        obj = result.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"factory part with id: {id} does not exist")

        await self.db.delete(obj)
        await self.db.commit()

        return obj
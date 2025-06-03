from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from apps.spareparts.data_layer.models.sparepart import Tag  # Adjust import path if needed


class TagRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_one(self, id: int) -> Tag:
        q = await self.db.execute(
            select(Tag).where(Tag.id == id)
        )
        obj = q.scalar_one_or_none()
        if not obj:
            raise NoResultFound(f"Tag with id {id} does not exist")
        return obj

    async def read_many(self) -> Sequence[Tag]:
        q = await self.db.execute(select(Tag))
        return q.scalars().all()

    async def create(self, tag: Tag) -> Tag:
        self.db.add(tag)
        await self.db.commit()
        await self.db.refresh(tag)
        return tag

    async def update(self, id: int, title: str | None = None) -> Tag:
        q = await self.db.execute(select(Tag).where(Tag.id == id))
        obj: Tag | None = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Tag with id {id} does not exist")

        if title is not None:
            obj.title = title

        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int) -> Tag:
        q = await self.db.execute(select(Tag).where(Tag.id == id))
        obj = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Tag with id {id} does not exist")

        await self.db.delete(obj)
        await self.db.commit()
        return obj

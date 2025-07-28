from typing import Sequence, Any
from sqlalchemy import select, Result, Selectable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import Select
from sqlalchemy.util import await_only

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


    async def create_or_read(self, tag: Tag) -> Tag:

        q = select(Tag).where(Tag.title == tag.title)
        query_result = await self.db.execute(q)
        obj : Tag | None = query_result.scalar_one_or_none()

        if obj is None:
            return await self.create(tag)
        return obj

    async def create_or_read_many(self, tags : list[Tag]) -> Sequence[Tag]:
        return [await self.create_or_read(tag) for tag in tags]


from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data.models.sparepart import Company


class CompanyRepository:

    def __init__(self, db: AsyncSession):
        self.db = db


    async def read_one(self, id: int)-> Company:
        q = await self.db.execute(
            select(Company).where(Company.id == id)
        )
        obj = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Company with id: {id} does not exist")

        return obj

    async def read_many(self) -> Sequence[Company] | None:
        q = await self.db.execute(
            select(Company)
        )
        objs = q.scalars().all()

        return objs

    async def create(self, company: Company) -> Company:
        self.db.add(company)

        await self.db.commit()
        await self.db.refresh(company)

        return company

    async def update(self,
                     id : int,
                     name: str | None = None,
                     location: str | None = None,
                     description: str | None = None,
                     website: str | None = None,
                     contactEmail: str | None = None,
                     ):
        q = await self.db.execute(
            select(Company).where(Company.id == id)
        )

        obj = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"Company with id: {id} does not exist")

        if name :
            obj.name = name
        if location :
            obj.location = location
        if description :
            obj.description = description
        if website :
            obj.website = website
        if contactEmail :
            obj.contactEmail = contactEmail

        await self.db.commit()
        await self.db.refresh(obj)
        return obj


    async def delete(self, id: int) -> Company:
        q = await self.db.execute(select(Company).where(Company.id == id))
        obj = q.scalar_one_or_none()

        if not obj:
            raise NoResultFound(f"factory part with id: {id} does not exist")

        await self.db.delete(obj)
        await self.db.commit()

        return obj


from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data.core.spare_parts_db import get_db
from apps.spareparts.data.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data.repository.unit_of_measure_repository import UnitOfMeasureRepository


class RepositoryDI():

    @classmethod
    def unit_of_measure_repository(self, db: AsyncSession = Depends(get_db),) -> UnitOfMeasureRepository:
        return UnitOfMeasureRepository(db = db)

    @classmethod
    def unit_of_measure_group_repository(self, db: AsyncSession = Depends(get_db), ) \
            -> UnitOfMeasureGroupRepository:
        return UnitOfMeasureGroupRepository(db=db)

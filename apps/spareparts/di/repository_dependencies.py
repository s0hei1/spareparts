from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data.core.spare_parts_db import get_db
from apps.spareparts.data.repository.factory_parts_repository import FactoryPartsRepository
from apps.spareparts.data.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data.repository.unit_of_measure_repository import UnitOfMeasureRepository

class RepositoryDI():

    @classmethod
    def unit_of_measure_repository(cls, db: AsyncSession = Depends(get_db),) -> UnitOfMeasureRepository:
        return UnitOfMeasureRepository(db = db)

    @classmethod
    def unit_of_measure_group_repository(cls, db: AsyncSession = Depends(get_db), ) \
            -> UnitOfMeasureGroupRepository:
        return UnitOfMeasureGroupRepository(db=db)

    @classmethod
    def factory_part_repository(cls , db : AsyncSession = Depends(get_db)) -> FactoryPartsRepository:
        return FactoryPartsRepository(db=db)


from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data.core.spare_parts_db import get_db
from apps.spareparts.data.repository.company_repository import CompanyRepository
from apps.spareparts.data.repository.factory_parts_repository import FactoryPartsRepository
from apps.spareparts.data.repository.location_repository import LocationRepository
from apps.spareparts.data.repository.machine_catalog_repository import MachineCatalogRepository
from apps.spareparts.data.repository.property_repository import PropertyRepository
from apps.spareparts.data.repository.spare_part_repository import SparePartRepository
from apps.spareparts.data.repository.spare_part_type_repository import SparePartTypeRepository
from apps.spareparts.data.repository.tag_repository import TagRepository
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

    @classmethod
    def company_repository(cls, db: AsyncSession = Depends(get_db)) -> CompanyRepository:
        return CompanyRepository(db=db)

    @classmethod
    def machine_catalog_repository(cls, db: AsyncSession = Depends(get_db)) -> MachineCatalogRepository:
        return MachineCatalogRepository(db=db)

    @classmethod
    def location_repository(cls, db: AsyncSession = Depends(get_db)) -> LocationRepository:
        return LocationRepository(db=db)

    @classmethod
    def tag_repository(cls, db: AsyncSession = Depends(get_db)) -> TagRepository:
        return TagRepository(db=db)

    @classmethod
    def sparepart_type(cls, db: AsyncSession = Depends(get_db)) -> SparePartTypeRepository:
        return SparePartTypeRepository(db=db)

    @classmethod
    def property_repository(cls, db: AsyncSession = Depends(get_db)) -> PropertyRepository:
        return PropertyRepository(db=db)

    @classmethod
    def spare_part_repository(cls, db: AsyncSession = Depends(get_db)) -> SparePartRepository:
        return SparePartRepository(db=db)




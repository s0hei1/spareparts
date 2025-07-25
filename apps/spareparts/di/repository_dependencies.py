from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.data_layer.core.spare_parts_db import get_db
from apps.spareparts.data_layer.models.sparepart import SparePartPropertyValue
from apps.spareparts.data_layer.repository.company_repository import CompanyRepository
from apps.spareparts.data_layer.repository.factory_parts_repository import FactoryPartsRepository
from apps.spareparts.data_layer.repository.location_repository import LocationRepository
from apps.spareparts.data_layer.repository.machine_catalog_repository import MachineCatalogRepository
from apps.spareparts.data_layer.repository.machine_catalog_spare_part import MachineCatalogSparePartRepository
from apps.spareparts.data_layer.repository.part_number_repository import PartNumberRepository
from apps.spareparts.data_layer.repository.property_repository import PropertyRepository
from apps.spareparts.data_layer.repository.spare_part_property_value import SparePartPropertyValueRepository
from apps.spareparts.data_layer.repository.spare_part_repository import SparePartRepository
from apps.spareparts.data_layer.repository.spare_part_type_repository import SparePartTypeRepository
from apps.spareparts.data_layer.repository.tag_repository import TagRepository
from apps.spareparts.data_layer.repository.trust_document_repository import TrustDocumentRepository
from apps.spareparts.data_layer.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data_layer.repository.unit_of_measure_repository import UnitOfMeasureRepository
from apps.spareparts.data_layer.repository.user_repository import UserRepository


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

    @classmethod
    def spare_part_property_value_repository(cls, db: AsyncSession = Depends(get_db)) -> SparePartPropertyValueRepository:
        return SparePartPropertyValueRepository(db=db)

    @classmethod
    def part_number_repository(cls, db: AsyncSession = Depends(get_db)) -> PartNumberRepository:
        return PartNumberRepository(db=db)

    @classmethod
    def machine_catalog_spare_part_repository(cls, db: AsyncSession = Depends(get_db)) -> MachineCatalogSparePartRepository:
        return MachineCatalogSparePartRepository(db=db)

    @classmethod
    def user_repository(cls, db: AsyncSession = Depends(get_db)) -> UserRepository:
        return UserRepository(db=db)

    @classmethod
    def trust_document_repository(cls, db: AsyncSession = Depends(get_db)) -> TrustDocumentRepository:
        return TrustDocumentRepository(db=db)


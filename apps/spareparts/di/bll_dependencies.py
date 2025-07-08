from fastapi.params import Depends

from apps.spareparts.business_logic_layer.auth.auth_bll import AuthBLL
from apps.spareparts.business_logic_layer.company.company_bll import CompanyBLL
from apps.spareparts.business_logic_layer.spare_part.spare_part_bll import SparePartBLL
from apps.spareparts.business_logic_layer.uom.unit_of_measure_bll import UnitOfMeasureBLL
from apps.spareparts.data_layer.core.read_only_async_session import ReadOnlyAsyncSession
from apps.spareparts.data_layer.core.spare_parts_db import get_read_only_db
from apps.spareparts.data_layer.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data_layer.repository.unit_of_measure_repository import UnitOfMeasureRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI


class BLL_DI():

    @classmethod
    def unit_of_measure_bll(cls) -> UnitOfMeasureBLL:
        return UnitOfMeasureBLL()

    @classmethod
    def spare_part_bll(cls,db: ReadOnlyAsyncSession = Depends(get_read_only_db)) -> SparePartBLL:
        return SparePartBLL(db = db)

    @classmethod
    def company_bll(cls):
        return CompanyBLL()

    @classmethod
    def auth_bll(cls,db: ReadOnlyAsyncSession = Depends(get_read_only_db)):
        return AuthBLL(db = db)


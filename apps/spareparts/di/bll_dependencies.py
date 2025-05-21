from fastapi.params import Depends

from apps.spareparts.buisness_logic_layer.uom.unit_of_measure_bll import UnitOfMeasureBLL
from apps.spareparts.data.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data.repository.unit_of_measure_repository import UnitOfMeasureRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI


class BLL_DI():

    @classmethod
    def unit_of_measure_bll(self,
                        uomRepo : UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository),
                        uomGroupRepo : UnitOfMeasureGroupRepository = Depends(RepositoryDI.unit_of_measure_group_repository),
                    ) -> UnitOfMeasureBLL:
        return UnitOfMeasureBLL(uomRepository= uomRepo, uomGroupRepository=uomGroupRepo)

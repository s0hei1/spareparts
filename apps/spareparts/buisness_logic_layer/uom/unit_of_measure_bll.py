from typing import Sequence

from apps.spareparts.buisness_logic_layer.uom.uom_schema import UnitOfMeasureCreate, UnitOfMeasureRead
from apps.spareparts.data.models.sparepart import UnitOfMeasureGroup, UnitOfMeasure
from apps.spareparts.data.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data.repository.unit_of_measure_repository import UnitOfMeasureRepository


class UnitOfMeasureBLL:

    def __init__(
            self,
            uomRepository : UnitOfMeasureRepository,
            uomGroupRepository : UnitOfMeasureGroupRepository,
                 ):
        self.uomRepository = uomRepository
        self.uomGroupRepository = uomGroupRepository

    async def add_uom(self, uomGroup : UnitOfMeasureCreate) -> UnitOfMeasureGroup:
        pass

    async def read_uoms(self) -> Sequence[UnitOfMeasureRead]:
        instances = await self.uomRepository.read_all()

        result = [UnitOfMeasureRead.model_validate(i) for i in instances]

        return result


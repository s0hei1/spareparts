from typing import Sequence

from fastapi import HTTPException

from apps.spareparts.business_logic_layer.exceptions.http_exceptions import HttpBadRequest
from apps.spareparts.business_logic_layer.uom.uom_schema import UnitOfMeasureCreate, UnitOfMeasureRead
from apps.spareparts.data_layer.models.sparepart import UnitOfMeasureGroup, UnitOfMeasure
from apps.spareparts.data_layer.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data_layer.repository.unit_of_measure_repository import UnitOfMeasureRepository


class UnitOfMeasureBLL:

    def __init__(
            self,
            uomRepository : UnitOfMeasureRepository,
            uomGroupRepository : UnitOfMeasureGroupRepository,
                 ):
        self.uomRepository = uomRepository
        self.uomGroupRepository = uomGroupRepository

    async def add_uom(self, uomCreate : UnitOfMeasureCreate) -> UnitOfMeasureRead:
        if uomCreate.newGroupName:
            newGroup = await self.uomGroupRepository.create(
                UnitOfMeasureGroup(name=uomCreate.newGroupName)
            )
            uomCreate.group_id = newGroup.id

        if not uomCreate.group_id:
            raise HttpBadRequest("You must add a new group name or specify a valid group ID")

        new_uom = await self.uomRepository.create(uomCreate.to_unit_of_measure())
        return UnitOfMeasureRead.model_validate(new_uom)


    async def read_uoms(self) -> Sequence[UnitOfMeasureRead]:
        instances = await self.uomRepository.read_many()

        result = [UnitOfMeasureRead.model_validate(i) for i in instances]

        return result


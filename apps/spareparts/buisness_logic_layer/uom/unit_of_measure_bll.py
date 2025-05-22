from typing import Sequence

from fastapi import HTTPException

from apps.spareparts.buisness_logic_layer.exceptions.http_exceptions import HttpBadRequest
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

    async def add_uom(self, uomCreate : UnitOfMeasureCreate) -> UnitOfMeasureRead:
        if uomCreate.newGroupName:
            newGroup = await self.uomGroupRepository.create(
                UnitOfMeasureGroup(name=uomCreate.newGroupName)
            )
            uomCreate.groupId = newGroup.id

        if not uomCreate.groupId:
            raise HttpBadRequest("You must add a new group name or specify a valid group ID")

        uom_data = uomCreate.model_dump(exclude={"newGroupName"})
        new_uom = await self.uomRepository.create(**uom_data)
        return UnitOfMeasureRead.model_validate(new_uom)


    async def read_uoms(self) -> Sequence[UnitOfMeasureRead]:
        instances = await self.uomRepository.read_all()

        result = [UnitOfMeasureRead.model_validate(i) for i in instances]

        return result


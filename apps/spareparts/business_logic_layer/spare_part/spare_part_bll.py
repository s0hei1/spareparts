from typing import Sequence, Any
from sqlalchemy import select,func
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.business_logic_layer.spare_part.spare_part_schema import SparePartCreate, SparePartCreateProperty
from apps.spareparts.data_layer.core.read_only_async_session import ReadOnlyAsyncSession
from apps.spareparts.data_layer.enums.property_value_type import PropertyValueType
from apps.spareparts.data_layer.models.sparepart import SparePartType, SparePart, SparePartTypeProperties, Property
from more_itertools import first

class SparePartBLL:

    def __init__(self, db: ReadOnlyAsyncSession):
        self.db = db

    async def sparepart_create_validation_process(self, sparepart_create : SparePartCreate) -> SparePartCreate:

        code = self.validate_properties(sparepart_create.sparepart_type_id, )

        return sparepart_create

    async def generate_code(self, spare_part_type_id : int) -> str:
        qSymbol = await self.db.execute(
            select(SparePartType.symbol).where(SparePartType.id == spare_part_type_id)
        )
        symbol : str | None = qSymbol.scalar_one_or_none()

        if symbol is None:
            symbol = "GN"

        qMaxCode = await self.db.execute(
            select(func.max(SparePart.code)).where(SparePart.spare_part_type_id == spare_part_type_id)
        )
        max_code : str | None = qMaxCode.scalar_one_or_none()

        if max_code is None:
             return f'SP-{symbol}-0001'

        lastCode = int(max_code.split('-')[-1]) + 1

        return f'SP-{symbol}-{lastCode:04d}'

    async def validate_properties(self,spare_part_type_id : int ,properties : Sequence[SparePartCreateProperty]):

        spare_part_type_properties = (await self.db.execute(
            select(SparePartTypeProperties.property_id,Property.value_type)
            .join(Property, Property.id == SparePartTypeProperties.property_id)
            .where(SparePartTypeProperties.spare_part_type_id == spare_part_type_id)
        )).all()

        for property in properties:
            spare_part_type_property : tuple[int, PropertyValueType] | None = first(
                [i for i in spare_part_type_properties if i[0] == property.property_id],
                default=None
            )
            if spare_part_type_property is None:
                raise ValueError()

            if not isinstance(property.value_type, spare_part_type_property[1].get_type()):
                raise ValueError()

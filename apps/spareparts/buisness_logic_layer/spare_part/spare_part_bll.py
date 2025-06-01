from sqlalchemy import select,func
from sqlalchemy.ext.asyncio import AsyncSession

from apps.spareparts.buisness_logic_layer.spare_part.spare_part_schema import SparePartCreate
from apps.spareparts.data.core.read_only_async_session import ReadOnlyAsyncSession
from apps.spareparts.data.models.sparepart import SparePartType, SparePart


class SparePartBLL:

    def __init__(self, db: ReadOnlyAsyncSession):
        self.db = db

    async def sparepart_creation_process(self, spare_part_create : SparePartCreate):

        pass

    async def generate_code(self, spare_part_type_id : int):
        qSymbol = await self.db.execute(
            select(SparePartType.symbol).where(SparePartType.id == spare_part_type_id)
        )
        symbol : str | None = qSymbol.scalar_one_or_none()

        if symbol is None:
            raise ValueError(f"SparePart type {spare_part_type_id} not found")

        qMaxCode = await self.db.execute(
            select(func.max(SparePart.code)).where(SparePart.spare_part_type_id == spare_part_type_id).max()
        )
        max_code : str | None = qMaxCode.scalar_one_or_none()

        if max_code is None:
             return f'SP-{symbol}-0001'

        lastCode = int(max_code.split('-')[-1]) + 1

        return f'SP-{symbol}-{lastCode:04d}'










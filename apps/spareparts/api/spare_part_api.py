from fastapi import APIRouter, Depends

from apps.spareparts.buisness_logic_layer.spare_part.spare_part_bll import SparePartBLL
from apps.spareparts.buisness_logic_layer.spare_part.spare_part_schema import SparePartCreate, SparePartRead, \
    SparePartUpdate, SparePartDeleteRead
from apps.spareparts.data.repository.spare_part_repository import SparePartRepository
from apps.spareparts.di.bll_dependencies import BLL_DI

from apps.spareparts.di.repository_dependencies import RepositoryDI

spare_part_router = APIRouter(prefix="/sparepart", tags=["SpareParts"])



@spare_part_router.post("/create", response_model=SparePartRead)
async def create_spare_part(
    spare_part: SparePartCreate,
    repo: SparePartRepository = Depends(RepositoryDI.spare_part_repository),
    sparePartsBLL : SparePartBLL = Depends(BLL_DI.spare_part_bll)
):

    code = await sparePartsBLL.generate_code(spare_part.sparepart_type_id)
    spare_part = await sparePartsBLL.validate_properties(spare_part.sparepart_type_id, spare_part.properties)


    return spare_part.to_sparepart(code)


@spare_part_router.get("/read_many", response_model=list[SparePartRead])
async def read_spare_parts(
    repo: SparePartRepository = Depends(RepositoryDI.spare_part_repository),
):
    return await repo.read_many()


@spare_part_router.get("/read_one", response_model=SparePartRead)
async def read_spare_part(
    id: int,
    repo: SparePartRepository = Depends(RepositoryDI.spare_part_repository),
):
    return await repo.read_one(id)


@spare_part_router.put("/update", response_model=SparePartRead)
async def update_spare_part(
    spare_part: SparePartUpdate,
    repo: SparePartRepository = Depends(RepositoryDI.spare_part_repository),
):
    return await repo.update(**spare_part.model_dump())


@spare_part_router.delete("/delete", response_model=SparePartDeleteRead)
async def delete_spare_part(
    id: int,
    repo: SparePartRepository = Depends(RepositoryDI.spare_part_repository),
):
    await repo.delete(id)
    return SparePartDeleteRead(id=id)

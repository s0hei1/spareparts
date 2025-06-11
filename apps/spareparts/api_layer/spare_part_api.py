from fastapi import APIRouter, Depends

from apps.spareparts.business_logic_layer.spare_part.spare_part_bll import SparePartBLL
from apps.spareparts.business_logic_layer.spare_part.spare_part_schema import SparePartCreate, SparePartRead, \
    SparePartUpdate, SparePartDeleteRead, SparePartPropertyValueRead, SparePartPropertyValueCreate
from apps.spareparts.data_layer.repository.spare_part_property_value import SparePartPropertyValueRepository
from apps.spareparts.data_layer.repository.spare_part_repository import SparePartRepository
from apps.spareparts.di.bll_dependencies import BLL_DI

from apps.spareparts.di.repository_dependencies import RepositoryDI

spare_part_router = APIRouter(prefix="/sparepart", tags=["Spare Parts"])



@spare_part_router.post("/create", response_model=SparePartRead)
async def create_spare_part(
    spare_part: SparePartCreate,
    sparepart_repo: SparePartRepository = Depends(RepositoryDI.spare_part_repository),
    sparePartsBLL : SparePartBLL = Depends(BLL_DI.spare_part_bll)
):

    code = await sparePartsBLL.generate_code(spare_part.sparepart_type_id)

    obj = spare_part.to_sparepart(code)

    result = await sparepart_repo.create(obj)

    return result


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

@spare_part_router.post('/add_spare_part_property_value', response_model=SparePartPropertyValueRead)
async def add_spare_part_property_value(
        create_model : SparePartPropertyValueCreate,
        spare_part_property_value_repo : SparePartPropertyValueRepository =  Depends(RepositoryDI.spare_part_property_value_repository),
        sparePartsBLL: SparePartBLL = Depends(BLL_DI.spare_part_bll)
):
    create_model = await sparePartsBLL.validate_spare_part_property_value(create_model)

    result = await spare_part_property_value_repo.create(create_model.to_spare_part_property_value())

    return result




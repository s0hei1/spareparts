from fastapi import APIRouter, Depends

from apps.spareparts.buisness_logic_layer.sparepart_type.sparepart_type_schema import SparePartTypeCreate, \
    SparePartTypeUpdate, SparePartTypeRead, SparePartTypeDeleteRead, SparePartTypeCreationRead
from apps.spareparts.data.models.sparepart import SparePartType
from apps.spareparts.data.repository.property_repository import PropertyRepository
from apps.spareparts.data.repository.spare_part_type_repository import SparePartTypeRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

sparepart_type_router = APIRouter(prefix="/spare_part_types", tags=["Spare Part Types"])


@sparepart_type_router.post("/add", response_model=SparePartTypeCreationRead)
async def create_sparepart_type(
    sparepart_type_create: SparePartTypeCreate,
    sparepart_type_repo: SparePartTypeRepository = Depends(RepositoryDI.sparepart_type),
    property_repo: PropertyRepository = Depends(RepositoryDI.property_repository),
):

    result = await sparepart_type_repo.create(sparepart_type_create.to_sparepart_type())

    # TODO : add validation for sparepart property IDs
    for propertyId in sparepart_type_create.properties:
        await sparepart_type_repo.create_sparepart_type_property(result.id, propertyId)

    return result


@sparepart_type_router.get("/read_one", response_model=SparePartTypeRead)
async def read_sparepart_type(
    id: int,
    repo: SparePartTypeRepository = Depends(RepositoryDI.sparepart_type),
):
    return await repo.read_one(id)


@sparepart_type_router.get("read_many", response_model=list[SparePartTypeRead])
async def read_many_sparepart_types(
    repo: SparePartTypeRepository = Depends(RepositoryDI.sparepart_type),
):
    return await repo.read_many()


@sparepart_type_router.put("/update", response_model=SparePartTypeRead)
async def update_sparepart_type(
    dto: SparePartTypeUpdate,
    repo: SparePartTypeRepository = Depends(RepositoryDI.sparepart_type),
):
    return await repo.update(**dto.model_dump())


@sparepart_type_router.delete("/delete", response_model=SparePartTypeDeleteRead)
async def delete_spare_part_type(
    id: int,
    repo: SparePartTypeRepository = Depends(RepositoryDI.sparepart_type),
):
    await repo.delete(id)
    return SparePartTypeDeleteRead(id=id)

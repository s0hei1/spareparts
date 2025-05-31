from fastapi import APIRouter, Depends

from apps.spareparts.buisness_logic_layer.property.property_schema import PropertyRead, PropertyCreate, PropertyUpdate, \
    PropertyDeleteRead
from apps.spareparts.data.models.sparepart import Property
from apps.spareparts.data.repository.property_repository import PropertyRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

property_router = APIRouter(prefix="/properties", tags=["Properties"])


@property_router.post("", response_model=PropertyRead)
async def create_property(
    property: PropertyCreate,
    repo: PropertyRepository = Depends(RepositoryDI.property_repository),
):
    return await repo.create(property.to_property())


@property_router.get("read_one", response_model=PropertyRead)
async def read_one_property(
    id: int,
    repo: PropertyRepository = Depends(RepositoryDI.property_repository),
):
    return await repo.read_one(id)


@property_router.get("read_many", response_model=list[PropertyRead])
async def read_many_properties(
    repo: PropertyRepository = Depends(RepositoryDI.property_repository),
):
    return await repo.read_many()


@property_router.put("/update", response_model=PropertyRead)
async def update_property(
    property: PropertyUpdate,
    repo: PropertyRepository = Depends(RepositoryDI.property_repository),
):
    return await repo.update(**property.model_dump())


@property_router.delete("/delete", response_model=PropertyDeleteRead)
async def delete_property(
    id: int,
    repo: PropertyRepository = Depends(RepositoryDI.property_repository),
):
    await repo.delete(id)
    return PropertyDeleteRead(id=id)

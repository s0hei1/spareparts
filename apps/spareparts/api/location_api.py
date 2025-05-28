from fastapi import APIRouter, Depends, Path

from apps.spareparts.buisness_logic_layer.location.location_schema import LocationRead, LocationCreate, LocationUpdate, \
    LocationDeleteRead
from apps.spareparts.data.repository.location_repository import LocationRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

location_router = APIRouter(prefix="/locations", tags=["Locations"])


@location_router.post("/create", response_model=LocationRead)
async def create_location(
    location_create: LocationCreate,
    repo: LocationRepository = Depends(RepositoryDI.location_repository),
):
    return await repo.create(location_create.to_location())


@location_router.get("/read_one", response_model=LocationRead)
async def read_location(
    id: int = Path(..., description="The ID of the location to retrieve"),
    repo: LocationRepository = Depends(RepositoryDI.location_repository),
):
    return await repo.read_one(id)


@location_router.get("/read_many", response_model=list[LocationRead])
async def read_many_locations(
    repo: LocationRepository = Depends(RepositoryDI.location_repository),
):
    return await repo.read_many()


@location_router.put("/update", response_model=LocationRead)
async def update_location(
    location_update: LocationUpdate,
    repo: LocationRepository = Depends(RepositoryDI.location_repository),
):
    return await repo.update(**location_update.model_dump())


@location_router.delete("/delete", response_model=LocationDeleteRead)
async def delete_location(
    id: int,
    repo: LocationRepository = Depends(RepositoryDI.location_repository),
):
    return await repo.delete(id)

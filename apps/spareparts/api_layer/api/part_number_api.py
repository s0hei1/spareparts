from fastapi import APIRouter, Depends
from apps.spareparts.business_logic_layer.machine_catalogs.machine_catalog_schema import MachineCatalogCreate
from apps.spareparts.business_logic_layer.part_number.part_number_schema import PartNumberRead, PartNumberCreate, \
    PartNumberUpdate, PartNumberDelete
from apps.spareparts.data_layer.repository.part_number_repository import PartNumberRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

part_number_router = APIRouter(prefix= '/part_number', tags=["Part Number"])


@part_number_router.post('/create', response_model=PartNumberRead)
async def create_part_number(
        machine_catalog_create : PartNumberCreate,
        part_number_repository : PartNumberRepository = Depends(RepositoryDI.part_number_repository)
):
    obj = await part_number_repository.create(machine_catalog_create.to_part_number())

    return obj

@part_number_router.get('/read_one', response_model=PartNumberRead)
async def read_pne_part_number(
        id : int,
        part_number_repository : PartNumberRepository = Depends(RepositoryDI.part_number_repository)
):
    obj = await part_number_repository.read_one(id)
    return obj

@part_number_router.get('/read_many', response_model=list[PartNumberRead])
async def read_pne_part_number(
        part_number_repository : PartNumberRepository = Depends(RepositoryDI.part_number_repository)
):
    objs = await part_number_repository.read_many()
    return objs

@part_number_router.put('/update', response_model=PartNumberRead)
async def update_part_number(
        part_number : PartNumberUpdate,
        part_number_repository: PartNumberRepository = Depends(RepositoryDI.part_number_repository)
):
    obj = await part_number_repository.update(**part_number.model_dump())
    return obj

@part_number_router.delete('/delete', response_model=PartNumberDelete)
async def delete_part_number(
        id : int,
        part_number_repository: PartNumberRepository = Depends(RepositoryDI.part_number_repository)
):
    obj = await part_number_repository.delete(id)

    return obj

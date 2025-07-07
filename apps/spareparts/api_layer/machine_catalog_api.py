from fastapi import APIRouter, Depends

from apps.spareparts.business_logic_layer.machine_catalogs.machine_catalog_schema import MachineCatalogRead, \
    MachineCatalogCreate, MachineCatalogUpdate, MachineCatalogDeleteRead
from apps.spareparts.data_layer.models.sparepart import MachineCatalog
from apps.spareparts.data_layer.repository import machine_catalog_repository
from apps.spareparts.data_layer.repository.machine_catalog_repository import MachineCatalogRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

machine_catalog_router = APIRouter(prefix='/machine-catalog', tags=['Machine Catalogs'])



@machine_catalog_router.post('/create', response_model=MachineCatalogRead)
async def add_machine_catalog(
        machine_catalog_create : MachineCatalogCreate,
        machine_catalog_repository : MachineCatalogRepository = Depends(RepositoryDI.machine_catalog_repository),
):
    return await machine_catalog_repository.create(machine_catalog_create.to_machine_catalog())

@machine_catalog_router.get('/read_machine_catalog', response_model=MachineCatalogRead)
async def get_machine_catalogs(
        id : int,
        machine_catalog_repository: MachineCatalogRepository = Depends(RepositoryDI.machine_catalog_repository),
):
    return await machine_catalog_repository.read_one(id)

@machine_catalog_router.get('/read_many_machine_catalogs', response_model=list[MachineCatalogRead])
async def get_machine_catalog(
        machine_catalog_repository: MachineCatalogRepository = Depends(RepositoryDI.machine_catalog_repository),
):
    return await machine_catalog_repository.read_many()

@machine_catalog_router.put('/update_machine_catalog', response_model=MachineCatalogRead)
async def update_machine_catalog(
        machine_catalog_update : MachineCatalogUpdate,
        machine_catalog_repository: MachineCatalogRepository = Depends(RepositoryDI.machine_catalog_repository),
):
    return await machine_catalog_repository.update(**machine_catalog_update.model_dump())

@machine_catalog_router.delete('/delete_machine_catalog', response_model=MachineCatalogDeleteRead)
async def delete_machine_catalog(
        id : int,
        machine_catalog_repository: MachineCatalogRepository = Depends(RepositoryDI.machine_catalog_repository),
):
    return await machine_catalog_repository.delete(id)

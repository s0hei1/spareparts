from fastapi import APIRouter, Depends

from apps.spareparts.business_logic_layer.machine_catalog_spare_part.machine_catalog_spare_part_schema import \
    MachineCatalogSparePartCreate, MachineCatalogSparePartRead, MachineCatalogSparePartUpdate, \
    MachineCatalogSparePartDelete
from apps.spareparts.data_layer.repository.machine_catalog_spare_part import MachineCatalogSparePartRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

machine_catalog_spare_part_router = APIRouter(prefix='/machine-catalog-spare-part', tags=['Machine Catalog Spare Part'])

@machine_catalog_spare_part_router.post('/create', response_model=MachineCatalogSparePartRead)
async def create_machine_catalog_spare_part(
    create_model : MachineCatalogSparePartCreate,
    mc_sp_repository : MachineCatalogSparePartRepository = Depends(RepositoryDI.machine_catalog_spare_part_repository)
):
    return await mc_sp_repository.create(create_model.to_machine_catalog_spare_part())


@machine_catalog_spare_part_router.get('/read_one', response_model=MachineCatalogSparePartRead)
async def read_one_machine_catalog_spare_part(
        id : int,
        mc_sp_repository: MachineCatalogSparePartRepository = Depends(
            RepositoryDI.machine_catalog_spare_part_repository)
):
    obj = await mc_sp_repository.read_one(id)
    return obj

@machine_catalog_spare_part_router.get('/read_many', response_model=list[MachineCatalogSparePartRead])
async def read_one_machine_catalog_spare_part(
        mc_sp_repository: MachineCatalogSparePartRepository = Depends(
            RepositoryDI.machine_catalog_spare_part_repository)
):
    obj = await mc_sp_repository.read_many()
    return obj

@machine_catalog_spare_part_router.put('/update', response_model=MachineCatalogSparePartRead)
async def update_machine_catalog_spare_part(
        update_model : MachineCatalogSparePartUpdate,
        mc_sp_repository: MachineCatalogSparePartRepository = Depends(
            RepositoryDI.machine_catalog_spare_part_repository)
):
    return await mc_sp_repository.update(**update_model.model_dump())

@machine_catalog_spare_part_router.delete('/delete', response_model=MachineCatalogSparePartDelete)
async def delete_machine_catalog_spare_part(
        id : int,
        mc_sp_repository: MachineCatalogSparePartRepository = Depends(
            RepositoryDI.machine_catalog_spare_part_repository)
):
    return await mc_sp_repository.delete(id)
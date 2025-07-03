from fastapi import APIRouter, Depends

from apps.spareparts.business_logic_layer.machine_catalog_spare_part.machine_catalog_spare_part_schema import \
    MachineCatalogSparePartCreate, MachineCatalogSparePartRead
from apps.spareparts.data_layer.repository.machine_catalog_spare_part import MachineCatalogSparePartRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

machine_catalog_spare_part_router = APIRouter(prefix='/machine-catalog-spare-part', tags=['Machine Catalog Spare Part'])

@machine_catalog_spare_part_router.post('/create', response_model=MachineCatalogSparePartRead)
async def machine_catalog_spare_part(
    create_model : MachineCatalogSparePartCreate,
    mc_sp_repository : MachineCatalogSparePartRepository = Depends(RepositoryDI.machine_catalog_spare_part_repository)
):
    return mc_sp_repository.create(create_model.to_machine_catalog_spare_part())
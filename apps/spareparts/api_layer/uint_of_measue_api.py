from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import Sequence
from sqlalchemy.util import await_only
from apps.spareparts.business_logic_layer.uom.unit_of_measure_bll import UnitOfMeasureBLL
from apps.spareparts.business_logic_layer.uom.uom_schema import UnitOfMeasureRead, UnitOfMeasureCreate, \
    UnitOfMeasureUpdate, UnitOfMeasureGroupCreate
from apps.spareparts.data_layer.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data_layer.repository.unit_of_measure_repository import UnitOfMeasureRepository
from apps.spareparts.di.bll_dependencies import BLL_DI
from apps.spareparts.di.repository_dependencies import RepositoryDI

uom_router = APIRouter(prefix ='/uom', tags=['Unit of Measure'])

@uom_router.get('/read_one', response_model=list[UnitOfMeasureRead])
async def read_one_uom(
        uom_repo: UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
):
    return await uom_repo.read_many()

@uom_router.get('/read_many', response_model=list[UnitOfMeasureRead])
async def read_many_uom(
        id : int,
        uom_repo: UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
):
    return await uom_repo.read_one(id=id)

@uom_router.post('/add', response_model= UnitOfMeasureRead )
async def add_uom(uom_create : UnitOfMeasureCreate,
                  uom_repo : UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
                  ):
    return await uom_repo.create(uom_create.to_unit_of_measure())

@uom_router.put('/update', response_model= UnitOfMeasureRead )
async def add_uom(uom_update : UnitOfMeasureUpdate,
                  uom_repo : UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
                  ):
    return await uom_repo.update(**uom_update.model_dump())

@uom_router.delete('/delete', response_model= UnitOfMeasureRead )
async def add_uom(id: int,
                  uom_repo : UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
                  ):
    return await uom_repo.delete(id= id)

@uom_router.get('/read_many_groups', response_model=list[UnitOfMeasureRead])
async def read_many(
        uom_group_repo: UnitOfMeasureGroupRepository = Depends(RepositoryDI.unit_of_measure_group_repository)
):
    return await uom_group_repo.read_many()

@uom_router.post('/add_group', response_model= UnitOfMeasureRead )
async def add_uom(uom_create : UnitOfMeasureGroupCreate,
                  uom_group_repo: UnitOfMeasureGroupRepository = Depends(RepositoryDI.unit_of_measure_group_repository)
                  ):
    return await uom_group_repo.create(uom_create.to_unit_of_measure_group())
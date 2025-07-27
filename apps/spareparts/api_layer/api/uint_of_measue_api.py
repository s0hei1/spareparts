from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import Sequence
from sqlalchemy.util import await_only
from apps.spareparts.business_logic_layer.uom.unit_of_measure_bll import UnitOfMeasureBLL
from apps.spareparts.business_logic_layer.uom.uom_schema import UnitOfMeasureRead, UnitOfMeasureCreate, \
    UnitOfMeasureUpdate, UnitOfMeasureGroupCreate, UnitOfMeasureGroupRead, UnitOfMeasureGroupDelete
from apps.spareparts.data_layer.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data_layer.repository.unit_of_measure_repository import UnitOfMeasureRepository
from apps.spareparts.di.bll_dependencies import BLL_DI
from apps.spareparts.di.repository_dependencies import RepositoryDI

uom_router = APIRouter(prefix='/uom', tags=['Unit of Measure'])


@uom_router.get('/read_many', response_model=list[UnitOfMeasureRead])
async def read_many(
        uom_repo: UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
):
    objs = await uom_repo.read_many()
    return UnitOfMeasureRead.from_unit_of_measures(objs)


@uom_router.get('/read_one', response_model=UnitOfMeasureRead)
async def read_one(
        id: int,
        uom_repo: UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
):
    obj = await uom_repo.read_one(id=id)
    return UnitOfMeasureRead.from_unit_of_measure(obj)


@uom_router.post('/add', response_model=UnitOfMeasureRead)
async def add_uom(uom_create: UnitOfMeasureCreate,
                  uom_repo: UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
                  ):
    obj = await uom_repo.create(uom_create.to_unit_of_measure())
    return UnitOfMeasureRead.from_unit_of_measure(obj)


@uom_router.put('/update', response_model=UnitOfMeasureRead)
async def update_uom(uom_update: UnitOfMeasureUpdate,
                     uom_repo: UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
                     ):
    return await uom_repo.update(**uom_update.model_dump())


@uom_router.delete('/delete', response_model=UnitOfMeasureRead)
async def delete_uom(id: int,
                     uom_repo: UnitOfMeasureRepository = Depends(RepositoryDI.unit_of_measure_repository)
                     ):
    return await uom_repo.delete(id=id)


@uom_router.get('/read_many_groups', response_model=list[UnitOfMeasureGroupRead])
async def read_many_groups(
        uom_group_repo: UnitOfMeasureGroupRepository = Depends(RepositoryDI.unit_of_measure_group_repository)
):
    return await uom_group_repo.read_many()


@uom_router.post('/add_group', response_model=UnitOfMeasureGroupRead)
async def add_uom_group(uom_create: UnitOfMeasureGroupCreate,
                        uom_group_repo: UnitOfMeasureGroupRepository = Depends(
                            RepositoryDI.unit_of_measure_group_repository)
                        ):
    return await uom_group_repo.create(uom_create.to_unit_of_measure_group())


@uom_router.post('/create_many', response_model=list[UnitOfMeasureGroupRead])
async def create_many(uom_create: list[UnitOfMeasureGroupCreate],
                      uom_group_repo: UnitOfMeasureGroupRepository = Depends(
                             RepositoryDI.unit_of_measure_group_repository)
                      ):

    return await uom_group_repo.create_many([i.to_unit_of_measure_group() for i in uom_create])


@uom_router.delete('/delete_group', response_model=UnitOfMeasureGroupDelete)
async def delete_uom_group(id: int,
                           uom_group_repo: UnitOfMeasureGroupRepository = Depends(
                               RepositoryDI.unit_of_measure_group_repository)
                           ):
    return await uom_group_repo.delete(id)

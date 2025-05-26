from fastapi import APIRouter
from fastapi import Depends
from apps.spareparts.buisness_logic_layer.factory_parts.factory_parts_schema import FactoryPartCreate, FactoryPartRead, \
    FactoryPartUpdate, FactoryPartDelete
from apps.spareparts.data.repository.factory_parts_repository import FactoryPartsRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

factory_parts_router = APIRouter(prefix='/factory_part')

@factory_parts_router.post('/add_factory_part', response_model=FactoryPartRead)
async def add_factory_part(
        factoryPartCreate: FactoryPartCreate,
        factoryPartRepo: FactoryPartsRepository = Depends(RepositoryDI.factory_part_repository)
):
    obj = factoryPartCreate.to_factory_part()

    return await factoryPartRepo.create(obj)


@factory_parts_router.get('/get_factory_parts', response_model=list[FactoryPartRead])
async def get_factory_parts(
        factoryPartRepo: FactoryPartsRepository = Depends(RepositoryDI.factory_part_repository)
):
    return await factoryPartRepo.read_many()


@factory_parts_router.put('/update_factory_part', response_model=FactoryPartRead)
async def update_factory_part(
        factoryPartUpdate: FactoryPartUpdate,
        factoryPartRepo: FactoryPartsRepository = Depends(RepositoryDI.factory_part_repository
                                                          )):
    obj = await factoryPartRepo.update(
        id=factoryPartUpdate.id,
        name=factoryPartUpdate.name,
        description=factoryPartUpdate.description,
        parentId=factoryPartUpdate.parentId,
    )

    return obj

@factory_parts_router.delete('/delete_factory_part', response_model=FactoryPartDelete)
async def delete_factory_part(
        id: int,
        factoryPartRepo: FactoryPartsRepository = Depends(RepositoryDI.factory_part_repository)):
    obj = await factoryPartRepo.delete(id=id)
    return obj

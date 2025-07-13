from fastapi import APIRouter, Depends

from apps.spareparts.business_logic_layer.auth.auth_bll import AuthBLL
from apps.spareparts.business_logic_layer.user.user_schema import UserCreate, UserRead
from apps.spareparts.data_layer.repository.user_repository import UserRepository
from apps.spareparts.di.bll_dependencies import BLL_DI
from apps.spareparts.di.repository_dependencies import RepositoryDI

user_router = APIRouter(prefix='/user', tags=['User'])

@user_router.post('/create', response_model=UserRead)
async def create(
        user_create : UserCreate,
        user_repository : UserRepository = Depends(RepositoryDI.user_repository),
        auth_bll : AuthBLL = Depends(BLL_DI.auth_bll),
):

    user_create.password = await auth_bll.verify_password(user_create.password)
    user_create.password = await auth_bll.hash_password(user_create.password)
    user_create.user_name = await auth_bll.verify_user_name(user_create.user_name)

    user = await user_repository.create(user_create.to_user())

    return user

@user_router.get('/read_one', response_model=UserRead)
async def read_one(
        id : int,
        user_repository: UserRepository = Depends(RepositoryDI.user_repository),
):
    user = await user_repository.read_one(id)
    return user


@user_router.get('/read_many', response_model=list[UserRead])
async def read_many(
        user_repository: UserRepository = Depends(RepositoryDI.user_repository),
):
    users = await user_repository.read_many()
    return users
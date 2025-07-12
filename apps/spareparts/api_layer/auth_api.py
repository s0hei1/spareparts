from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from apps.spareparts.business_logic_layer.auth.auth_bll import AuthBLL
from apps.spareparts.business_logic_layer.auth.auth_schema import LoginSchema, Token

from apps.spareparts.business_logic_layer.user.user_schema import UserRead
from apps.spareparts.di.bll_dependencies import BLL_DI
from apps.spareparts.di.general_dependencies import GeneralDI
from apps.spareparts.security.jwt_helpers import JWT

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login", response_model=Token)
async def login(
        login_schema: LoginSchema,
        auth_bll : AuthBLL = Depends(BLL_DI.auth_bll),
        jwt : JWT = Depends(GeneralDI.jwt),
):
    await auth_bll.verify_user_name(login_schema.user_name)
    await auth_bll.verify_password(login_schema.password)
    user = await auth_bll.login(login_schema.user_name, login_schema.password)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,)

    token = await auth_bll.generate_token(user)

    return Token(
        token = token,
    )

@auth_router.get("/current_user", response_model=UserRead)
async def current_user(
    token : str,
    auth_bll: AuthBLL = Depends(BLL_DI.auth_bll),
):
    user = await auth_bll.current_user(token)

    return user

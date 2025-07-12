from sqlalchemy import select
from apps.spareparts.business_logic_layer.exceptions import ValidationException
from apps.spareparts.data_layer.core.read_only_async_session import ReadOnlyAsyncSession
from hashlib import sha256
import re
from apps.spareparts.data_layer.models.sparepart import User
from apps.spareparts.security.jwt_helpers import JWT


class AuthBLL:

    def __init__(self, db: ReadOnlyAsyncSession, jwt : JWT) -> None:
        self.db = db
        self._jwt = jwt

    async def hash_password(self, password: str) -> str:
        password = sha256(password.encode()).hexdigest()
        return password

    async def verify_password(self, password: str) -> str:
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        flag = re.fullmatch(pattern, password) is not None
        if not flag:
            raise ValidationException('Password must contain at least 8 characters and a mix of characters and numbers')

        return password

    async def verify_user_name(self, username: str) -> str:

        pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$'
        flag = re.fullmatch(pattern, username) is not None
        if not flag:
            raise ValidationException(f"Username '{username}' is invalid")

        return username

    async def login(self, username: str, password: str) -> User:
        await self.verify_user_name(username)
        await self.verify_password(password)
        hashed_password = await self.hash_password(password)

        q = select(User).where(User.user_name == username)
        query_result = await self.db.execute(q)

        user = query_result.scalar_one_or_none()

        if user is None:
            raise ValidationException(f"Username or password is invalid")

        if user.password != hashed_password:
            raise ValidationException(f"Username or password is invalid")

        return user

    async def current_user(self, token : str) -> User:

        payload = self._jwt.decode_access_token(token)
        user_name = payload["sub"]
        q = select(User).where(User.user_name == user_name)
        query_result = await self.db.execute(q)
        user = query_result.scalar_one_or_none()

        if user is None:
            raise ValidationException(f"User name is invalid")

        return user



    async def generate_token(self, user : User) -> str:
        token = self._jwt.create_access_token(data = {"sub": user.user_name})
        return token
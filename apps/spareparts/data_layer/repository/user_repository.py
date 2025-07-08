from typing import List
from sqlalchemy import select, Sequence
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from apps.spareparts.data_layer.enums.user_type import UserType
from apps.spareparts.data_layer.models.sparepart import User

class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user : User):

        if user.user_type == UserType.SuperAdmin:
            raise Exception("You can not create user with super admin type")

        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def read_one(self, user_id : int) -> User :
        q = select(User).where(User.id == user_id)
        query_result = await self.db.execute(q)
        obj = query_result.scalar_one_or_none()

        if obj is None:
            raise NoResultFound(f"User with id: {user_id} does not exist")

        return obj

    async def read_many(self) -> Sequence[User]:
        q = select(User).order_by(User.id)
        query_result = await self.db.execute(q)
        objs = query_result.scalars().all()
        return objs

    async def change_password(self, user_id: int, password: str) -> User:

        user = await self.read_one(user_id)
        user.password = password
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def de_active_user(self, user_id: int) -> User:
        user = await self.read_one(user_id)
        user.is_active = False
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def activate_user(self, user_id : int) -> User:
        user = await self.read_one(user_id)
        user.is_active = True
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def change_user_type(self, user_id: int, user_type: UserType) -> User:
        if user_type == UserType.SuperAdmin:
            raise Exception("You can not change user type to super admin")
        user = await self.read_one(user_id)
        user.user_type = user_type
        await self.db.commit()
        await self.db.refresh(user)
        return user


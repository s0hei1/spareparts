from pydantic import BaseModel

from apps.spareparts.data_layer.enums.user_type import UserType
from apps.spareparts.data_layer.models.sparepart import User


class UserCreate(BaseModel):
    user_name: str
    password: str
    user_type: UserType
    is_active: bool = True
    personal_id: int | None = None

    def to_user(self):
        return User(
            user_name=self.user_name,
            password=self.password,
            user_type=self.user_type,
            is_active=self.is_active,
            personal_id=self.personal_id,
        )


class UserRead(BaseModel):
    id : int
    user_name: str
    is_active: bool

    class Config:
        from_attributes = True

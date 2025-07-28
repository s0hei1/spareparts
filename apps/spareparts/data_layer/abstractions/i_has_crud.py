from abc import ABC, abstractmethod

from typing_extensions import TypeVar, Generic

from apps.spareparts.business_logic_layer.tag.tag_schema import TagCreate

T = TypeVar('T')

class IHasCrud(ABC, Generic(T)):

    @abstractmethod
    async def create(self, model: T) -> T:
        pass

    @abstractmethod
    async def read_one(self, id : int) -> T:
        pass

    @abstractmethod
    async def update(self, model: T) -> T:
        pass




from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from apps.spareparts.data_layer.models.documents import GoodsTrustDocument


async def init_mongo_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.my_app_database, document_models=[GoodsTrustDocument])

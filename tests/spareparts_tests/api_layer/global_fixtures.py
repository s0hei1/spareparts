import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport

from apps.spareparts.api_layer.comapny_api import company_router
from apps.spareparts.api_layer.tag_api import tag_router
from apps.spareparts.data_layer.core.spare_parts_db import get_db


@pytest.fixture
def app():
    app = FastAPI()
    app.include_router(company_router)
    app.include_router(tag_router)
    # app.include_router(part_number)
    return app

@pytest_asyncio.fixture
async def async_client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test/"
    ) as client:
        yield client


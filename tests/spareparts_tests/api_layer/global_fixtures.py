import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport

from apps.spareparts.api_layer.comapny_api import company_router
from apps.spareparts.api_layer.machine_catalog_api import machine_catalog_router
from apps.spareparts.api_layer.machine_catalog_spare_part_api import machine_catalog_spare_part_router
from apps.spareparts.api_layer.part_number_api import part_number_router
from apps.spareparts.api_layer.spare_part_api import spare_part_router
from apps.spareparts.api_layer.sparepart_type_api import sparepart_type_router
from apps.spareparts.api_layer.tag_api import tag_router
from apps.spareparts.data_layer.core.spare_parts_db import get_db



@pytest.fixture
def app():
    app = FastAPI()
    app.include_router(company_router)
    app.include_router(tag_router)
    app.include_router(sparepart_type_router)
    app.include_router(part_number_router)
    app.include_router(machine_catalog_router)
    app.include_router(spare_part_router)
    app.include_router(machine_catalog_spare_part_router)
    return app

@pytest_asyncio.fixture
async def async_client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test/"
    ) as client:
        yield client


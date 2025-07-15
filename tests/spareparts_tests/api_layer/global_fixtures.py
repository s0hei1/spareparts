import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport
from apps.spareparts.api_layer.api.auth_api import auth_router
from apps.spareparts.api_layer.api.comapny_api import company_router
from apps.spareparts.api_layer.api.machine_catalog_api import machine_catalog_router
from apps.spareparts.api_layer.api.machine_catalog_spare_part_api import machine_catalog_spare_part_router
from apps.spareparts.api_layer.api.part_number_api import part_number_router
from apps.spareparts.api_layer.api.spare_part_api import spare_part_router
from apps.spareparts.api_layer.api.sparepart_type_api import sparepart_type_router
from apps.spareparts.api_layer.api.tag_api import tag_router
from apps.spareparts.api_layer.api.trust_document_api import trust_document_router
from apps.spareparts.api_layer.api.user_api import user_router
from apps.spareparts.api_layer.middleware.performance_middleware import PerformanceMiddleware
from apps.spareparts.data_layer.core.spare_parts_db import get_db
from apps.spareparts.main import app as applications

@pytest.fixture
def app():
    return applications

@pytest_asyncio.fixture
async def async_client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test/"
    ) as client:
        yield client


import pytest
from httpx import AsyncClient
from fastapi import FastAPI

from apps.spareparts.data_layer.models.sparepart import MachineCatalog
from global_fixtures import app,async_client


@pytest.fixture
def fake_machine_catalog() -> dict:
    return {
        "machine_name": "Test Machine",
        "model_name": "Zero",
        "is_tool": False,
    }

@pytest.mark.asyncio
async def test_create_machine_catalog(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog):

    response = await async_client.post("/machine-catalog/create", json=fake_machine_catalog)
    response.raise_for_status()
    result = response.json()

    assert "id" in result
    assert result["machine_name"] == fake_machine_catalog["machine_name"]
    assert result["model_name"] == fake_machine_catalog["model_name"]
    assert result["is_tool"] == fake_machine_catalog["is_tool"]

import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app, async_client


@pytest.fixture
def fake_spare_part_type() -> dict:
    return {
        "name": "Test Type",
        "symbol": "TS"
    }

@pytest.mark.asyncio
async def test_create_spare_part_type(
        app: FastAPI,
        async_client: AsyncClient,
        fake_spare_part_type : dict
):
    response = await async_client.post("/spare-part-types/create", json=fake_spare_part_type)
    response.raise_for_status()


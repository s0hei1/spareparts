import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app, async_client
from more_itertools import first


@pytest.fixture
def fake_spare_part() -> dict:
    return {
        "name": "TestPart",
        "alias_name": "Test Part Alias",
        "spare_part_type_id": 1
    }


@pytest.mark.asyncio
async def test_create_spare_part(
        app: FastAPI,
        async_client: AsyncClient,
        fake_spare_part: dict
):
    response = await async_client.post(url="/spare-part/create", json=fake_spare_part)
    response.raise_for_status()


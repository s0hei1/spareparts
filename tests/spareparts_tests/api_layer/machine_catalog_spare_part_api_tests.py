import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app,async_client

@pytest.fixture
def fake_machine_catalog_spare_part() -> dict:
    return {
        "spare_part_id": 1,
        "machine_catalog_id": 1,
        "usage_ration": 100
    }

@pytest.fixture
def fake_wrong_machine_catalog_spare_part() -> dict:
    return {
        "spare_part_id": 99999,
        "machine_catalog_id": 99999,
        "usage_ration": 100
    }


@pytest.mark.asyncio
async def test_create_machine_catalog_spare_part(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog_spare_part: dict
):
    response = await async_client.post("/machine-catalog-spare-part/create", json=fake_machine_catalog_spare_part)
    response.raise_for_status()
    result = response.json()

    assert "id" in result
    assert result["spare_part_id"] == fake_machine_catalog_spare_part["spare_part_id"]
    assert result["machine_catalog_id"] == fake_machine_catalog_spare_part["machine_catalog_id"]
    assert result["usage_ration"] == fake_machine_catalog_spare_part["usage_ration"]


@pytest.mark.asyncio
async def test_read_one_machine_catalog_spare_part(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog_spare_part: dict
):
    # First create
    create_response = await async_client.post("/machine_catalog_spare_part/create",
                                              json=fake_machine_catalog_spare_part)
    create_response.raise_for_status()
    part_id = create_response.json()["id"]

    # Then read
    read_response = await async_client.get("/machine_catalog_spare_part/read_one", params={"id": part_id})
    read_response.raise_for_status()
    result = read_response.json()

    assert result["id"] == part_id
    assert result["usage_ration"] == fake_machine_catalog_spare_part["usage_ration"]


@pytest.mark.asyncio
async def test_read_many_machine_catalog_spare_parts(
    app: FastAPI,
    async_client: AsyncClient,
):

    read_response = await async_client.get("/machine_catalog_spare_part/read_many")
    read_response.raise_for_status()

    parts = read_response.json()

    assert isinstance(parts, list)


@pytest.mark.asyncio
async def test_update_machine_catalog_spare_part(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog_spare_part: dict
):
    create_response = await async_client.post("/machine_catalog_spare_part/create",
                                              json=fake_machine_catalog_spare_part)
    create_response.raise_for_status()
    part = create_response.json()

    update_payload = {
        "id": part["id"],
        "usage_ration": 200  # New value
    }

    update_response = await async_client.put("/machine_catalog_spare_part/update", json=update_payload)
    update_response.raise_for_status()
    updated = update_response.json()

    assert updated["id"] == part["id"]
    assert updated["usage_ration"] == 200


@pytest.mark.asyncio
async def test_delete_machine_catalog_spare_part(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog_spare_part: dict
):
    create_response = await async_client.post("/machine_catalog_spare_part/create",
                                              json=fake_machine_catalog_spare_part)
    create_response.raise_for_status()
    part_id = create_response.json()["id"]

    delete_response = await async_client.delete("/machine_catalog_spare_part/delete", params={"id": part_id})
    delete_response.raise_for_status()
    result = delete_response.json()

    assert result["id"] == part_id
    assert result["message"] == "MachineCatalogSparePart deleted successfully"

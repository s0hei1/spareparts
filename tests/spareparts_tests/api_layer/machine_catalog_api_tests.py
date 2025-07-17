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

async def create_machine_catalog(async_client: AsyncClient,fake_machine_catalog: dict) -> dict:
    response = await async_client.post("/machine-catalog/create", json=fake_machine_catalog)
    response.raise_for_status()
    return response.json()

async def read_machine_catalog(async_client: AsyncClient, id : int) -> dict:
    response = await async_client.get(f"/machine-catalog/read", params={"id": id})
    response.raise_for_status()
    return response.json()

async def read_many_machine_catalogs(async_client: AsyncClient) -> list[dict]:
    response = await async_client.get(f"/machine-catalog/read_many")
    response.raise_for_status()
    return response.json()

@pytest.mark.asyncio
async def test_create_machine_catalog(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog):

    machine_catalog_json = await create_machine_catalog(async_client, fake_machine_catalog)

    assert "id" in machine_catalog_json
    assert machine_catalog_json["machine_name"] == fake_machine_catalog["machine_name"]
    assert machine_catalog_json["model_name"] == fake_machine_catalog["model_name"]
    assert machine_catalog_json["is_tool"] == fake_machine_catalog["is_tool"]

@pytest.mark.asyncio
async def test_read_machine_catalog(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog
):
    machine_catalog_json = await create_machine_catalog(async_client, fake_machine_catalog)
    machine_catalog_read_json = await read_machine_catalog(async_client, machine_catalog_json["id"])

    assert "id" in machine_catalog_read_json
    assert machine_catalog_read_json["machine_name"] == fake_machine_catalog["machine_name"]
    assert machine_catalog_read_json["model_name"] == fake_machine_catalog["model_name"]
    assert machine_catalog_read_json["is_tool"] == fake_machine_catalog["is_tool"]

@pytest.mark.asyncio
async def test_read_many_machine_catalogs(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog
):
    create_model = await create_machine_catalog(async_client, fake_machine_catalog)
    machine_catalogs = await read_many_machine_catalogs(async_client)

    assert isinstance(machine_catalogs, list)
    assert create_model in machine_catalogs

@pytest.mark.asyncio
async def test_update_machine_catalog(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog
):
    create_model = await create_machine_catalog(async_client, fake_machine_catalog)

    newName = "Test Machine Updated"

    create_model['machine_name'] = newName
    response = await async_client.put("/machine-catalog/update", json=create_model)
    response.raise_for_status()

    updated_model = response.json()

    assert "id" in updated_model
    assert updated_model["id"] == create_model["id"]
    assert updated_model["machine_name"] == newName


@pytest.mark.asyncio
async def test_delete_machine_catalog(
        app: FastAPI,
        async_client: AsyncClient,
        fake_machine_catalog
):
    create_model = await create_machine_catalog(async_client, fake_machine_catalog)
    response = await async_client.delete("/machine-catalog/delete", params={'id': create_model["id"]})
    response.raise_for_status()

    assert response.json().get("id") == create_model["id"]


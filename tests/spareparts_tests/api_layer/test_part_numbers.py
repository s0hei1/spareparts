import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app,async_client
from more_itertools import first

@pytest.fixture
def fake_part_number(
        spare_part_id = 1,
        company_id = 1
) -> dict :
    return {
        "spare_part_id" : spare_part_id,
        "company_id" : company_id,
        "part_number" : "270.465.648"
    }

@pytest.mark.asyncio
async def test_create_part_number(
        app: FastAPI,
        async_client: AsyncClient,
        fake_part_number : dict
):
    response = await async_client.post("/part_number/create", json=fake_part_number)
    response.raise_for_status()

    assert response.json().get("id") != None

@pytest.mark.asyncio
async def test_read_part_number(
        app: FastAPI,
        async_client: AsyncClient,
        id : int = 1):
    response = await async_client.get("/part_number/read_one", params={"id": id})
    response.raise_for_status()
    assert response.json().get("id") != None
    assert response.json().get("part_number") != None
    assert response.json().get("spare_part_id") != None
    assert response.json().get("company_id") != None
    response.json().get("something_else")


@pytest.mark.asyncio
async def test_read_part_numbers(
        app: FastAPI,
        async_client: AsyncClient):
    response = await async_client.get("/part_number/read_many")
    response.raise_for_status()
    assert type(response.json().get("data")) == list

@pytest.mark.asyncio
async def test_update_part_number(
        app: FastAPI,
        async_client: AsyncClient):
    part_numbers_response = await async_client.put("/part_number/update")
    part_number = first(part_numbers_response.json())
    response = await async_client.put("/part_number/update", json={
        "id" : part_number["id"],
        "part_number" : "SO_KO_1656"
    })
    response.raise_for_status()

@pytest.mark.asyncio
async def test_delete_part_number(
        app: FastAPI,
        async_client: AsyncClient):
    part_numbers_response = await async_client.put("/part_number/delete")
    part_number = first(part_numbers_response.json())

    response = await async_client.delete("/part_number/delete", params={"id": part_number["id"]})
    response.raise_for_status()
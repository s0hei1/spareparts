import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app,async_client


@pytest.fixture
def fake_create_company_json() -> dict:
    return {
        "name": "Git Company",
        "location": "Germany-Berlin",
        "description": "its a fake company for test APIs",
        "website": "https://Github.com",
        "contact_email": "khosroshahisoheil1999@gmail.com"
    }


@pytest.fixture
def fake_company_read_json(fake_create_company_json : dict) -> dict:
    return {
        "id" : 0,
        "name": fake_create_company_json["name"],
        "location": fake_create_company_json["location"],
        "description": fake_create_company_json["description"],
        "website": fake_create_company_json["website"],
        "contact_email": fake_create_company_json["contact_email"],
    }




@pytest.mark.asyncio
async def test_create_company(
        app: FastAPI,
        async_client: AsyncClient,
        fake_create_company_json: dict,
        fake_company_read_json : dict):

    response = await async_client.post("/company/create", json=fake_create_company_json)

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_read_many_companies(
        app: FastAPI,
        async_client: AsyncClient,
):
    response = await async_client.get("/company/read_many")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_read_company(
        app: FastAPI,
        async_client: AsyncClient,
):
    response = await async_client.get(url = "/company/read_one", params= {"id" : 1})
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_company(
        app: FastAPI,
        async_client: AsyncClient,
        fake_create_company_json : dict
):
    company = await async_client.post(url = "/company/create", json = fake_create_company_json)

    company.raise_for_status()
    id = company.json()["id"]

    response = await async_client.delete(url = "/company/delete", params = {"id" : id})
    response.raise_for_status()
    assert response.json() == {
        "id" : id,
        "message" : "Company deleted successfully",
    }

@pytest.mark.asyncio
async def test_update_company(
        app: FastAPI,
        async_client: AsyncClient,
        fake_create_company_json: dict
):
    company = await async_client.post(url = "/company/create", json = fake_create_company_json)
    company.raise_for_status()
    company_dict = company.json()

    newName = "Any Co"
    newLocation = "Russia Moscow"

    request = {
        'id' : company_dict['id'],
        'name' : newName,
        'location' : newLocation,
    }

    response = await async_client.put(url = "/company/update", json = request)
    response.raise_for_status()

    updated_company=response.json()

    assert updated_company['name'] == newName
    assert updated_company['location'] == newLocation





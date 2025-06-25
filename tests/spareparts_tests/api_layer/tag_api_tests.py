import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app,async_client
from more_itertools import first

@pytest.fixture
def fake_tag_json() -> dict:
    return {
        "title" : "TestTag"
    }

@pytest.mark.asyncio
async def test_create_tag(
        app : FastAPI,
        async_client: AsyncClient,
        fake_tag_json: dict,
):
    response = await async_client.post("/tag/create", json=fake_tag_json)

    assert response.status_code == 200
    assert response.json().get("title") == fake_tag_json['title']

@pytest.mark.asyncio
async def test_read_tag(
        app: FastAPI,
        async_client: AsyncClient,
        id : int = 1
):
    response = await async_client.get("/tag/read_one", params={"id" : id})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_read_tags(
        app: FastAPI,
        async_client: AsyncClient,
):
    response = await async_client.get("/tag/read_many/")
    assert response.status_code == 200
    assert type(response.json()) == list

@pytest.mark.asyncio
async def test_tag_delete(
        app: FastAPI,
        async_client: AsyncClient,
        fake_tag_json: dict,
):
    create_response = await async_client.post("/tag/create", json=fake_tag_json)
    create_response.raise_for_status()
    id = create_response.json().get("id")

    response = await async_client.delete("/tag/delete", params={"id" : id})
    response.raise_for_status()

@pytest.mark.asyncio
async def test_tag_update(
        app: FastAPI,
        async_client: AsyncClient,
        fake_tag_json: dict,
):
    tags_reponse = await async_client.get("/tag/read_many/")

    first_tag = first(tags_reponse.json())

    newTitle = "Updated Title"
    id = first_tag.get("id")

    request = {
        "id" : id,
        "title" : newTitle,
    }

    response = await async_client.put("/tag/update", json=request)
    response.raise_for_status()

    assert response.json().get("title") == newTitle
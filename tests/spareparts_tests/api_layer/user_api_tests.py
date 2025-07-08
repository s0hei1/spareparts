import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app,async_client
from more_itertools import first
from random import randint


@pytest.fixture
def fake_user_json() -> dict:
    any_number = randint(1, 100)

    return {
        "user_name" : f"maryamm{any_number}",
        "password" : "maryam1377",
        "user_type" : 1,
    }

@pytest.fixture
def fake_wrong_user_jason() -> dict:
    return {
        "user_name" : "maryam hastam",
        "password" : "Test",
        "user_type" : 1,
    }



@pytest.mark.asyncio
async def test_create_user(
        app : FastAPI,
        async_client : AsyncClient,
        fake_user_json: dict):

    response = await async_client.post(url= '/user/create', json=fake_user_json)

    response.raise_for_status()
    assert "id" in response.json()
    assert "user_name" in response.json()
    assert "password" not in response.json()


@pytest.mark.asyncio
async def test_read_one_user(
        app: FastAPI,
        async_client: AsyncClient,
        fake_user_json : dict,
):
    create_user_response = await async_client.post(url= '/user/create', json = fake_user_json)
    create_user_response.raise_for_status()
    user = create_user_response.json()

    response = await async_client.get(url= '/user/read_one', params={'id': user['id']})
    response.raise_for_status()

    assert response.json().get('user_name') == user['user_name']

@pytest.mark.asyncio
async def test_read_many_users(
        app: FastAPI,
        async_client: AsyncClient,
):
    response = await async_client.get(url= '/user/read_many')
    response.raise_for_status()

    assert isinstance(response.json(), list)

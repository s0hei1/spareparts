import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app,async_client
from more_itertools import first


@pytest.fixture
def fake_login_json() -> dict:
    return {
        'user_name' : 'maryam',
        "password": "test_password",
    }

@pytest.fixture
def fake_wrong_login_json() -> dict:
    return {
        'user_name': 'maryam',
        "password": "test_password_wrong",
    }

@pytest.fixture
def fake_change_password_json() -> dict:
    return {
        'current_password' : 'test_password',
        'new_password' : 'test_password_new',
    }

@pytest.fixture
def fake_wrong_change_password_json() -> dict:
    return {
        'current_password' : 'test_password_wrong',
        'new_password' : 'test_password_new',
    }

@pytest.mark.asyncio
async def test_login_success(
        app : FastAPI,
        async_client : AsyncClient,
):
    response = await async_client.post(url= '/user/login', json=fake_login_json)
    response.raise_for_status()

    assert "token" in response.json()

async def test_wrong_login(
        app : FastAPI,
        async_client: AsyncClient,
        fake_wrong_login_json: dict,

):
    response = await async_client.post(url= '/user/login', json=fake_wrong_login_json)
    assert response.status_code == 401
    assert response.json() == {"message": "User name or password is incorrect"}

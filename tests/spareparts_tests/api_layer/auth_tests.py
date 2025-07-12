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
        "user_name" : f"maryammmm{any_number}",
        "password" : "maryam1377",
        "user_type" : 1
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
        fake_user_json : dict,
):
    await async_client.post(url= '/user/create', json=fake_user_json)

    response = await async_client.post(url= '/auth/login', json={
        "user_name" : fake_user_json["user_name"],
        "password" : fake_user_json["password"],
    })
    response.raise_for_status()

    assert "token" in response.json()

@pytest.mark.asyncio
async def test_wrong_login(
        app : FastAPI,
        async_client: AsyncClient,
        fake_wrong_login_json: dict,

):
    response = await async_client.post(url= '/auth/login', json=fake_wrong_login_json)
    assert response.status_code == 401
    # assert response.json() == {"message": "User name or password is incorrect"}

@pytest.mark.asyncio
async def test_get_current_user(
        app : FastAPI,
        async_client: AsyncClient,
        fake_user_json: dict,
):
    create_user = await async_client.post(url='/user/create', json=fake_user_json)
    create_user.raise_for_status()

    login = await async_client.post(url='/auth/login', json={
        "user_name": fake_user_json["user_name"],
        "password": fake_user_json["password"],
    })
    login.raise_for_status()

    token = login.json().get('token')
    response = await async_client.get(url='/auth/current_user',params={'token': token})

    response.raise_for_status()

    assert response.json().get('id') == create_user.json().get('id')
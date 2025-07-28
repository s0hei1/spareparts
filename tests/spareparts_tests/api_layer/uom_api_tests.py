import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from global_fixtures import app, async_client
from more_itertools import first


@pytest.fixture()
def fake_uom_groups():
    return [
        {
            "name": "Test Group 1",
            "alias_name": "Test Group Alias Name",
            "description": "this is a test",
        },
        {
            "name": "Test Group 2",
            "alias_name": "Test Group Alias Name",
            "description": "this is a test",
        },
        {
            "name": "Test Group 3",
            "alias_name": "Test Group Alias Name",
            "description": "this is a test",
        },
    ]

@pytest.mark.asyncio
async def test_create_uom_groups(
        app : FastAPI,
        async_client : AsyncClient,
        fake_uom_groups):
    response = await async_client.post('/uom/create_many', json=fake_uom_groups)
    response.raise_for_status()
    assert isinstance(response.json(), list)
    assert len(response.json()) == len(fake_uom_groups)
    assert first(response.json()).get('id')


import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from global_fixtures import app,async_client
from more_itertools import first

@pytest.fixture
def fake_trust_document_json() -> dict:
    return {
    "delivery_date" : "2025-01-01",
    "return_date" : "2025-01-02",
    "description" : "Something",
    "personal_name" : "Soheil H",
    }

@pytest.mark.asyncio
async def test_create_trust_document(
    app: FastAPI,
    async_client: AsyncClient,
    fake_trust_document_json: dict
):
    response = await async_client.post("/trust-document/create", json=fake_trust_document_json)

    assert response.status_code == 200
    data = response.json()
    assert data["description"] == fake_trust_document_json["description"]
    assert data["personal_name"] == fake_trust_document_json["personal_name"]


@pytest.mark.asyncio
async def test_read_trust_document(
    app: FastAPI,
    async_client: AsyncClient,
    fake_trust_document_json: dict
):

    create_response = await async_client.post("/trust-document/create", json=fake_trust_document_json)
    doc_id = create_response.json()["id"]

    response = await async_client.get("/trust-document/read_one", params={"id": doc_id})
    assert response.status_code == 200
    assert response.json()["id"] == doc_id


@pytest.mark.asyncio
async def test_read_many_trust_documents(
    app: FastAPI,
    async_client: AsyncClient
):
    response = await async_client.get("/trust-document/read_many")
    response.raise_for_status()
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_trust_document(
    app: FastAPI,
    async_client: AsyncClient,
    fake_trust_document_json: dict
):
    # Create a document
    create_response = await async_client.post("/trust-document/create", json=fake_trust_document_json)
    doc = create_response.json()
    doc_id = doc["id"]

    # Update it
    updated_description = "Updated description"
    update_payload = {
        "id": doc_id,
        "delivery_date": doc["delivery_date"],
        "return_date": doc["return_date"],
        "description": updated_description,
        "personal_name": doc["personal_name"]
    }

    update_response = await async_client.put("/trust-document/update", json=update_payload)
    assert update_response.status_code == 200
    assert update_response.json()["description"] == updated_description


@pytest.mark.asyncio
async def test_delete_trust_document(
    app: FastAPI,
    async_client: AsyncClient,
    fake_trust_document_json: dict
):
    # Create a document
    create_response = await async_client.post("/trust-document/create", json=fake_trust_document_json)
    doc_id = create_response.json()["id"]

    # Delete it
    delete_response = await async_client.delete("/trust-document/delete", params={"id": doc_id})
    assert delete_response.status_code == 200
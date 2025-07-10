from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import defer

from apps.spareparts.business_logic_layer.trust_document.trust_document_schema import TrustDocumentCreate, \
    TrustDocumentRead, TrustDocumentUpdate
from apps.spareparts.business_logic_layer.utils.response import DeleteResponse
from apps.spareparts.data_layer.models.sparepart import TrustDocument
from apps.spareparts.data_layer.repository.trust_document_repository import TrustDocumentRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

trust_document_router = APIRouter(prefix="/trust-document", tags=["Trust Document"])


@trust_document_router.post("/create", response_model=TrustDocumentRead)
async def create(
        create_model: TrustDocumentCreate,
        trust_doc_repo: TrustDocumentRepository = Depends(RepositoryDI.trust_document_repository)
):
    return await trust_doc_repo.create(create_model.to_trust_document())


@trust_document_router.get("/read_many", response_model=list[TrustDocumentRead])
async def read_many(
        trust_doc_repo: TrustDocumentRepository = Depends(RepositoryDI.trust_document_repository)
):
    return await trust_doc_repo.read_many()

@trust_document_router.get("/read_one", response_model=TrustDocumentRead)
async def read_one(
        id : int,
        trust_doc_repo: TrustDocumentRepository = Depends(RepositoryDI.trust_document_repository)
):
    return await trust_doc_repo.read_one(id)

@trust_document_router.put("/update", response_model=TrustDocumentRead)
async def update(
        update_model: TrustDocumentUpdate,
        trust_doc_repo: TrustDocumentRepository = Depends(RepositoryDI.trust_document_repository)
):
    return await trust_doc_repo.update(**update_model.model_dump())

@trust_document_router.delete("/delete", response_model=DeleteResponse)
async def delete(
        id : int,
        trust_doc_repo: TrustDocumentRepository = Depends(RepositoryDI.trust_document_repository)
):
    return await trust_doc_repo.delete(id)
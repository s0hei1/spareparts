from fastapi import APIRouter, Depends
from sqlalchemy.util import await_only

from apps.spareparts.business_logic_layer.tag.tag_schema import TagRead, TagCreate, TagUpdate
from apps.spareparts.business_logic_layer.utils.response import DeleteResponse
from apps.spareparts.data_layer.models.sparepart import Tag
from apps.spareparts.data_layer.repository.tag_repository import TagRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

tag_router = APIRouter(prefix="/tag", tags=["Tag"])


@tag_router.post("/create", response_model=TagRead)
async def create_tag(
    tag_create: TagCreate,
    repo: TagRepository = Depends(RepositoryDI.tag_repository),
):

    return await repo.create(tag_create.to_tag())

@tag_router.post("/create_many", response_model=list[TagRead])
async def create_many_tags(
        tags_create: list[TagCreate],
        repo: TagRepository = Depends(RepositoryDI.tag_repository),
):
    return await repo.create_or_read_many([tag.to_tag() for tag in tags_create])

@tag_router.get("/read_one", response_model=TagRead)
async def read_one_tag(
    id: int,
    repo: TagRepository = Depends(RepositoryDI.tag_repository),
):
    return await repo.read_one(id)


@tag_router.get("/read_many/", response_model=list[TagRead])
async def read_many_tags(
    repo: TagRepository = Depends(RepositoryDI.tag_repository),
):
    return await repo.read_many()


@tag_router.put("/update", response_model=TagRead)
async def update_tag(
    tag_update: TagUpdate,
    repo: TagRepository = Depends(RepositoryDI.tag_repository),
):
    return await repo.update(**tag_update.model_dump())


@tag_router.delete("/delete", response_model=DeleteResponse)
async def delete_tag(
    id: int,
    repo: TagRepository = Depends(RepositoryDI.tag_repository),
):
    return await repo.delete(id)

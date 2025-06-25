from fastapi import APIRouter, Depends

from apps.spareparts.business_logic_layer.tag.tag_schema import TagRead, TagCreate, TagUpdate, TagDeleteRead
from apps.spareparts.data_layer.models.sparepart import Tag
from apps.spareparts.data_layer.repository.tag_repository import TagRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

tag_router = APIRouter(prefix="/tag", tags=["Tag"])


@tag_router.post("/create", response_model=TagRead)
async def create_tag(
    tag_create: TagCreate,
    repo: TagRepository = Depends(RepositoryDI.tag_repository),
):
    tag = Tag(**tag_create.dict())
    return await repo.create(tag)


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


@tag_router.delete("/delete", response_model=TagDeleteRead)
async def delete_tag(
    id: int,
    repo: TagRepository = Depends(RepositoryDI.tag_repository),
):
    return await repo.delete(id)


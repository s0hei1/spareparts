from fastapi import APIRouter, Depends

from apps.spareparts.buisness_logic_layer.company.company_schema import CompanyRead, CompanyCreate, CompanyUpdate
from apps.spareparts.data.repository.company_repository import CompanyRepository
from apps.spareparts.di.repository_dependencies import RepositoryDI

company_router = APIRouter(prefix='/company')


@company_router.get('/read_company', response_model=CompanyRead)
async def read_company(
        id: int,
        companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository)):
    return await companyRepo.read_one(id)


@company_router.get('/read_companies', response_model=list[CompanyRead])
async def read_companies(
        companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository)):
    return await companyRepo.read_many()


@company_router.post('/add_company', response_model=CompanyRead)
async def add_company(company: CompanyCreate,
                      companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository)):
    result = await companyRepo.create(company.to_company())

    return result


@company_router.put('/update_company', response_model=CompanyRead)
async def add_company(company: CompanyUpdate,
                      companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository)):
    result = await companyRepo.update(**company.model_dump())

    return result


@company_router.delete('/delete_company', response_model=CompanyRead)
async def delete_company(id: int, companyRepo=Depends(RepositoryDI.company_repository)):
    result = await companyRepo.delete(id)
    return result

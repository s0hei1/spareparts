from fastapi import APIRouter, Depends

from apps.spareparts.business_logic_layer.company.company_bll import CompanyBLL
from apps.spareparts.business_logic_layer.company.company_schema import CompanyRead, CompanyCreate, CompanyUpdate, \
    CompanyDelete
from apps.spareparts.data_layer.repository.company_repository import CompanyRepository
from apps.spareparts.di.bll_dependencies import BLL_DI
from apps.spareparts.di.repository_dependencies import RepositoryDI

company_router = APIRouter(prefix='/company', tags=['Company'])


@company_router.get('/read_one', response_model=CompanyRead)
async def read_company(
        id: int,
        companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository)):
    return await companyRepo.read_one(id)


@company_router.get('/read_many', response_model=list[CompanyRead])
async def read_companies(
        companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository)):
    return await companyRepo.read_many()


@company_router.post('/create', response_model=CompanyRead)
async def add_company(company: CompanyCreate,
                      companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository),
                      company_bll : CompanyBLL = Depends(BLL_DI.company_bll)
                      ):
    company = await company_bll.company_validation(company)

    result = await companyRepo.create(company.to_company())

    return result


@company_router.put('/update', response_model=CompanyRead)
async def update_company(company: CompanyUpdate,
                      companyRepo: CompanyRepository = Depends(RepositoryDI.company_repository),):
    result = await companyRepo.update(**company.model_dump())

    return result


@company_router.delete('/delete', response_model=CompanyDelete)
async def delete_company(id: int, companyRepo=Depends(RepositoryDI.company_repository)):
    result = await companyRepo.delete(id)
    return result


from apps.spareparts.business_logic_layer.company.company_schema import CompanyCreate


class CompanyBLL:

    async def company_validation(self, company_create : CompanyCreate) -> CompanyCreate:
        return company_create
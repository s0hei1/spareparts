from fastapi import FastAPI

from apps.spareparts.api.comapny_api import company_router
from apps.spareparts.api.facory_parts_api import factory_parts_router
from apps.spareparts.api.location_api import location_router
from apps.spareparts.api.machine_catalog_api import machine_catalog_router
# from apps.spareparts.api.spareparts import sparePartsRouter
from apps.spareparts.api.uint_of_measue_api import uom_router
from dotenv import load_dotenv

app = FastAPI()
# app.include_router(sparePartsRouter)
app.include_router(uom_router)
app.include_router(factory_parts_router)
app.include_router(company_router)
app.include_router(machine_catalog_router)
app.include_router(location_router)

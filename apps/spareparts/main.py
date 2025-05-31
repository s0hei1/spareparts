from fastapi import FastAPI
from apps.spareparts.api.comapny_api import company_router
from apps.spareparts.api.facory_parts_api import factory_parts_router
from apps.spareparts.api.location_api import location_router
from apps.spareparts.api.machine_catalog_api import machine_catalog_router
from apps.spareparts.api.property_api import property_router
from apps.spareparts.api.sparepart_type_api import sparepart_type_router
from apps.spareparts.api.tag_api import tag_router
from apps.spareparts.api.uint_of_measue_api import uom_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Tomato"}
app.include_router(uom_router)
app.include_router(factory_parts_router)
app.include_router(company_router)
app.include_router(machine_catalog_router)
app.include_router(location_router)
app.include_router(tag_router)
app.include_router(sparepart_type_router)
app.include_router(property_router)


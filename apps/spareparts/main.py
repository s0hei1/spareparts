from fastapi import FastAPI

from apps.spareparts.api.facory_parts_api import factory_parts_router
# from apps.spareparts.api.spareparts import sparePartsRouter
from apps.spareparts.api.uint_of_measue_api import uom_router
from dotenv import load_dotenv



app = FastAPI()
# app.include_router(sparePartsRouter)
app.include_router(uom_router)
app.include_router(factory_parts_router)

from fastapi import FastAPI

from apps.spareparts.admin.admin import config_admin
from apps.spareparts.api_layer.auth_api import auth_router
from apps.spareparts.api_layer.comapny_api import company_router
from apps.spareparts.api_layer.facory_parts_api import factory_parts_router
from apps.spareparts.api_layer.location_api import location_router
from apps.spareparts.api_layer.machine_catalog_api import machine_catalog_router
from apps.spareparts.api_layer.machine_catalog_spare_part_api import machine_catalog_spare_part_router
from apps.spareparts.api_layer.part_number_api import part_number_router
from apps.spareparts.api_layer.property_api import property_router
from apps.spareparts.api_layer.spare_part_api import spare_part_router
from apps.spareparts.api_layer.sparepart_type_api import sparepart_type_router
from apps.spareparts.api_layer.tag_api import tag_router
from apps.spareparts.api_layer.uint_of_measue_api import uom_router
from sqladmin import Admin

from apps.spareparts.api_layer.user_api import user_router
from apps.spareparts.data_layer.core.spare_parts_db import get_db, get_engine

app = FastAPI()

app.include_router(uom_router)
app.include_router(factory_parts_router)
app.include_router(company_router)
app.include_router(machine_catalog_router)
app.include_router(location_router)
app.include_router(tag_router)
app.include_router(sparepart_type_router)
app.include_router(property_router)
app.include_router(spare_part_router)
app.include_router(part_number_router)
app.include_router(machine_catalog_spare_part_router)
app.include_router(user_router)
app.include_router(auth_router)

config_admin(app)





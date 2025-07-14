from fastapi import FastAPI
from apps.spareparts.admin.admin import config_admin
from apps.spareparts.api_layer.api.auth_api import auth_router
from apps.spareparts.api_layer.api.comapny_api import company_router
from apps.spareparts.api_layer.api.facory_parts_api import factory_parts_router
from apps.spareparts.api_layer.api.location_api import location_router
from apps.spareparts.api_layer.api.machine_catalog_api import machine_catalog_router
from apps.spareparts.api_layer.api.machine_catalog_spare_part_api import machine_catalog_spare_part_router
from apps.spareparts.api_layer.api.part_number_api import part_number_router
from apps.spareparts.api_layer.api.property_api import property_router
from apps.spareparts.api_layer.api.spare_part_api import spare_part_router
from apps.spareparts.api_layer.api.sparepart_type_api import sparepart_type_router
from apps.spareparts.api_layer.api.tag_api import tag_router
from apps.spareparts.api_layer.api.uint_of_measue_api import uom_router
from apps.spareparts.api_layer.api.user_api import user_router
from apps.spareparts.api_layer.exception_handler.bll_exceptions_handler import validation_exception_handler, \
    business_logic_exception_handler
from apps.spareparts.api_layer.middleware.performance_middleware import PerformanceMiddleware
from apps.spareparts.business_logic_layer.exceptions import BusinessLogicException, ValidationException

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

app.add_middleware(PerformanceMiddleware)
app.add_exception_handler(BusinessLogicException, business_logic_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)

from fastapi import FastAPI, Depends
from sqladmin import Admin
from sqlalchemy.ext.asyncio import AsyncEngine
from apps.spareparts.admin.admin_models import (
    PropertyAdmin,
    SparePartTypeAdmin,
    SparePartTypePropertiesAdmin,
    SparePartAdmin,
    FactoryPartAdmin,
    MachineCatalogAdmin,
    UnitOfMeasureGroupAdmin,
    UnitOfMeasureAdmin,
    CompanyAdmin,
    LocationAdmin,
    TagAdmin,
)
from apps.spareparts.data_layer.core.spare_parts_db import get_engine


def config_admin(app: FastAPI, async_engine: AsyncEngine | None = None) -> None:
    if async_engine is None:
        async_engine = get_engine()

    admin = Admin(app=app, engine=async_engine)

    admin.add_view(PropertyAdmin)
    admin.add_view(SparePartTypeAdmin)
    admin.add_view(SparePartTypePropertiesAdmin)
    admin.add_view(SparePartAdmin)
    admin.add_view(FactoryPartAdmin)
    admin.add_view(MachineCatalogAdmin)
    admin.add_view(UnitOfMeasureGroupAdmin)
    admin.add_view(UnitOfMeasureAdmin)
    admin.add_view(CompanyAdmin)
    admin.add_view(LocationAdmin)
    admin.add_view(TagAdmin)
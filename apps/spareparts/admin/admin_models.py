from sqladmin import ModelView

from apps.spareparts.data_layer.models.sparepart import (
    Property,
    SparePartType,
    SparePartTypeProperties,
    SparePart,
    FactoryPart,
    MachineCatalog,
    UnitOfMeasureGroup,
    UnitOfMeasure,
    Company,
    Location,
    Tag
)


class PropertyAdmin(ModelView, model=Property):
    column_list = [Property.id, Property.name, Property.value_type, Property.unit_of_measure_id]


class SparePartTypeAdmin(ModelView, model=SparePartType):
    column_list = [SparePartType.id, SparePartType.name, SparePartType.symbol]


class SparePartTypePropertiesAdmin(ModelView, model=SparePartTypeProperties):
    column_list = [SparePartTypeProperties.id, SparePartTypeProperties.spare_part_type_id, SparePartTypeProperties.property_id]


class SparePartAdmin(ModelView, model=SparePart):
    column_list = [SparePart.id, SparePart.name, SparePart.code, SparePart.alias_name, SparePart.spare_part_type_id, SparePart.is_active]


class FactoryPartAdmin(ModelView, model=FactoryPart):
    column_list = [FactoryPart.id, FactoryPart.name, FactoryPart.parentId, FactoryPart.description]


class MachineCatalogAdmin(ModelView, model=MachineCatalog):
    column_list = [MachineCatalog.id, MachineCatalog.machine_name, MachineCatalog.model_name, MachineCatalog.factory_part_id, MachineCatalog.is_tool]


class UnitOfMeasureGroupAdmin(ModelView, model=UnitOfMeasureGroup):
    column_list = [UnitOfMeasureGroup.id, UnitOfMeasureGroup.name]


class UnitOfMeasureAdmin(ModelView, model=UnitOfMeasure):
    column_list = [UnitOfMeasure.id, UnitOfMeasure.name, UnitOfMeasure.group_id, UnitOfMeasure.unit_in_group]


class CompanyAdmin(ModelView, model=Company):
    column_list = [Company.id, Company.name, Company.location, Company.website, Company.contactEmail]


class LocationAdmin(ModelView, model=Location):
    column_list = [Location.id, Location.shelf, Location.column, Location.row, Location.floor]


class TagAdmin(ModelView, model=Tag):
    column_list = [Tag.id, Tag.title]


from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Float,Boolean
from sqlalchemy.orm import relationship

from apps.spareparts.data_layer.enums.property_value_type import PropertyValueType
from sqlalchemy.ext.declarative import declarative_base

SQLAlchemyModel = declarative_base()

class Property(SQLAlchemyModel):
    __tablename__ = 'property'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    value_type = Column(Enum(PropertyValueType))
    unit_of_measure_id = Column(Integer, ForeignKey('unit_of_measure.id'), nullable=False)

    unit_of_measure = relationship("UnitOfMeasure")

class SparePartType(SQLAlchemyModel):
    __tablename__ = 'spare_part_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    symbol = Column(String(4))

    properties = relationship("SparePartTypeProperties", back_populates="spare_part_type")
    spare_parts = relationship("SparePart", back_populates="spare_part_type")

class SparePartTypeProperties(SQLAlchemyModel):
    __tablename__ = 'spare_part_properties'
    id = Column(Integer, primary_key=True)
    spare_part_type_id = Column(Integer, ForeignKey('spare_part_type.id'), nullable=False)
    property_id = Column(Integer, ForeignKey('property.id'), nullable=False)

    spare_part_type = relationship("SparePartType", back_populates="properties")
    property = relationship("Property")
    spare_part_type_property_values = relationship("SparePartPropertyValue")

class SparePart(SQLAlchemyModel):
    __tablename__ = 'spare_part'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    alias_name = Column(String(255), nullable=True)
    spare_part_type_id = Column(Integer, ForeignKey('spare_part_type.id'), nullable=False)
    code = Column(String(16), nullable=False, unique=True)
    is_active = Column(Boolean, default=False)

    spare_part_type = relationship("SparePartType", back_populates="spare_parts")

# class WhoCanUseSparePart(SparePart):
#     __tablename__ = 'who_can_use_spare_part'
#
#     id = Column(Integer, primary_key=True)
#     spare_part_id = Column(Integer, ForeignKey('spare_part.id'), nullable=False)
#     machine_catalog_id = Column(Integer, ForeignKey('machine_catalog.id'), nullable=False)
#     usage_ration = Column(Float, nullable=True)
#
#     spare_part = relationship("SparePart", back_populates="who_can_use_spare_part")
#     machine_catalog = relationship("MachineCatalog")

class SparePartPropertyValue(SQLAlchemyModel):
    __tablename__ = 'spare_part_property_value'

    id = Column(Integer, primary_key=True)
    spare_part_type_property_id = Column(Integer, ForeignKey('spare_part_properties.id'), nullable=False)
    spare_part_id = Column(Integer, ForeignKey('spare_part.id'), nullable=False)
    value = Column(String(255), nullable=True)

    spare_part_type_property = relationship("SparePartTypeProperties")
    spare_part = relationship("SparePart")

class FactoryPart(SQLAlchemyModel):
    __tablename__ = 'factory_part'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    parentId = Column(Integer, ForeignKey('factory_part.id'), nullable=True)
    description = Column(String(1024), nullable=True)

    parent = relationship('FactoryParts')

class MachineCatalog(SQLAlchemyModel):
    __tablename__ = 'machine_catalogs'
    id = Column(Integer, primary_key=True)
    machine_name = Column(String(256), nullable= False)
    location_in_factory  = Column(String(256), nullable= True)
    factory_part_id  = Column(Integer, ForeignKey('factory_part.id'), nullable= True)
    description = Column(String(1024), nullable= True)
    model_name = Column(String(256), nullable= False)
    is_tool = Column(Boolean, nullable= False, default= False)

    factory_part = relationship('FactoryPart')

class UnitOfMeasureGroup(SQLAlchemyModel):
    __tablename__ = 'unit_of_measure_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)

class UnitOfMeasure(SQLAlchemyModel):
    __tablename__ = 'unit_of_measure'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    group_id = Column(Integer, ForeignKey('unit_of_measure_group.id'), nullable=False)
    unit_in_group = Column(Float(precision=53), nullable=True, doc= """
    For example on Weight Unit of Measures 'Gram' will be '1' and 'Kilogram' will be '1000'
    I hope you will understand :D
    """)

    group = relationship(UnitOfMeasureGroup)

class Company(SQLAlchemyModel):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=False)
    website = Column(String(255), nullable=True)
    contactEmail = Column(String(255), nullable=True)


class Location(SQLAlchemyModel):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    shelf = Column(String(8))
    column = Column(Integer)
    row = Column(Integer)
    floor = Column(Integer, nullable=True)

class Tag(SQLAlchemyModel):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)


from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Float,Boolean
from sqlalchemy.orm import relationship

from apps.spareparts.data_layer.enums.property_value_type import PropertyValueType
from sqlalchemy.ext.declarative import declarative_base

SQLAlchemyModel = declarative_base()

#
# class Warehouse(SQLAlchemyModel):
#     __tablename__ = 'warehouse'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#

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

class SparePartPropertyValue(SQLAlchemyModel):
    __tablename__ = 'spare_part_property_value'

    id = Column(Integer, primary_key=True)
    spare_part_type_property_id = Column(Integer, ForeignKey('spare_part_properties.id'), nullable=False)
    spare_part_id = Column(Integer, ForeignKey('spare_part.id'), nullable=False)
    value = Column(String(255), nullable=True)

    spare_part_type_property = relationship("SparePartTypeProperties")
    spare_part = relationship("SparePart")


class FactoryParts(SQLAlchemyModel):
    __tablename__ = 'factory_parts'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    parentId = Column(Integer, ForeignKey('factory_parts.id'), nullable=True)
    description = Column(String(1024), nullable=True)

    parent = relationship('FactoryParts')

class MachineCatalog(SQLAlchemyModel):
    __tablename__ = 'machine_catalogs'
    id = Column(Integer, primary_key=True)
    machine_name = Column(String(256), nullable= False)
    location_in_factory  = Column(String(256), nullable= True)
    factory_parts_id  = Column(Integer, ForeignKey('factory_parts.id'), nullable= True)
    description = Column(String(1024), nullable= True)
    model_name = Column(String(256), nullable= False)
    is_tool = Column(Boolean, nullable= False, default= False)

    factory_part = relationship('FactoryParts')


# class MachinesSpareParts(SQLAlchemyModel):
#     __tablename__ = 'machines_spare_parts'
#     id = Column(Integer, primary_key=True)

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
    x = Column(String(15))
    y = Column(String(15))
    z = Column(String(15))
    floor = Column(Integer, nullable=True)

class Tag(SQLAlchemyModel):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
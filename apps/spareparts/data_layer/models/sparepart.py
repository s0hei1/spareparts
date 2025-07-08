from datetime import datetime

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Float, Boolean,Date
from sqlalchemy.orm import relationship

from apps.spareparts.data_layer.enums.property_value_type import PropertyValueType
from sqlalchemy.ext.declarative import declarative_base

from apps.spareparts.data_layer.enums.user_type import UserType

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
    machine_catalogs = relationship('MachineCatalogSparePart')

class MachineCatalogSparePart(SQLAlchemyModel):
    __tablename__ = 'machine_catalog_spare_part'

    id = Column(Integer, primary_key=True)
    spare_part_id = Column(Integer, ForeignKey('spare_part.id'), nullable=False)
    machine_catalog_id = Column(Integer, ForeignKey('machine_catalog.id'), nullable=False)
    usage_ration = Column(Float, nullable=True)

    spare_part = relationship("SparePart", back_populates="machine_catalogs")
    machine_catalog = relationship("MachineCatalog", back_populates="spare_parts",)

    # __table_args__ = (
    #     UniqueConstraint("name", "code", name="uq_spare_part_name_code"),
    # )

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

    parent = relationship('FactoryPart')

class MachineCatalog(SQLAlchemyModel):
    __tablename__ = 'machine_catalog'
    id = Column(Integer, primary_key=True)
    machine_name = Column(String(256), nullable= False)
    location_in_factory  = Column(String(256), nullable= True)
    factory_part_id  = Column(Integer, ForeignKey('factory_part.id'), nullable= True)
    description = Column(String(1024), nullable= True)
    model_name = Column(String(256), nullable= False)
    is_tool = Column(Boolean, nullable= False, default= False)

    factory_part = relationship('FactoryPart')
    spare_parts = relationship("MachineCatalogSparePart")

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

class PartNumber(SQLAlchemyModel):
    __tablename__ = 'part_number'
    id = Column(Integer, primary_key=True)
    part_number = Column(String(255), nullable=False)
    spare_part_id = Column(Integer, ForeignKey('spare_part.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)

    spare_part = relationship("SparePart")
    company = relationship("Company")

class User(SQLAlchemyModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    personal_id = Column(Integer, ForeignKey('personal.id'), nullable=True)

    personal = relationship("Personal", backref="user")

class Personal(SQLAlchemyModel):
    __tablename__ = 'personal'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)

class TrustDocument(SQLAlchemyModel):
    __tablename__ = 'trust_document'
    id = Column(Integer, primary_key=True)
    delivery_date = Column(Date, nullable=False, default= datetime.today())
    return_date = Column(Date, nullable=False)
    description = Column(String(1024), nullable=False)
    personal_name = Column(String(255), nullable=False)



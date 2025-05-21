
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship

from apps.spareparts.data.enums.property_value_type import PropertyValueType
from apps.spareparts.data.models.base import SQLAlchemyModel


#
# class Warehouse(SQLAlchemyModel):
#     __tablename__ = 'warehouse'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#
# class Properties(SQLAlchemyModel):
#     __tablename__ = 'properties'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     value_type = Column(Enum(PropertyValueType))
#
# class SparePartType(SQLAlchemyModel):
#     __tablename__ = 'spare_part_type'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     properties =
#
# class SparePart(SQLAlchemyModel):
#     __tablename__ = 'spare_part'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     sparePartType =
#
# class SparePartPropertyValue(SQLAlchemyModel):
#     __tablename__ = 'spare_part_value'
#     id = Column(Integer, primary_key=True)
#     property = Column()
#     sparePart = Column(ForeignKey('spare_part.id'))
#     value = Column(String(255)
#
# class FactoryParts(SQLAlchemyModel):
#     __tablename__ = 'factory_parts'
#     id = Column(Integer, primary_key=True)
#
# class MachineCatalogs(SQLAlchemyModel):
#     __tablename__ = 'machine_catalogs'
#     id = Column(Integer, primary_key=True)
#
# class MachinesSpareParts(SQLAlchemyModel):
#     __tablename__ = 'machines_spare_parts'
#     id = Column(Integer, primary_key=True)

class UnitOfMeasureGroup (SQLAlchemyModel):
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

# class Locations(SQLAlchemyModel):
#     __tablename__ = 'locations'
#     x = Column(String(15))
#     y = Column(String(15))
#     z = Column(String(15))
#     floor = Column(Integer, nullable=True)

from typing import Sequence

from fastapi import HTTPException

from apps.spareparts.business_logic_layer.exceptions.http_exceptions import HttpBadRequest
from apps.spareparts.business_logic_layer.uom.uom_schema import UnitOfMeasureCreate, UnitOfMeasureRead
from apps.spareparts.data_layer.models.sparepart import UnitOfMeasureGroup, UnitOfMeasure
from apps.spareparts.data_layer.repository.unit_of_measure_group_repository import UnitOfMeasureGroupRepository
from apps.spareparts.data_layer.repository.unit_of_measure_repository import UnitOfMeasureRepository


class UnitOfMeasureBLL:
    pass
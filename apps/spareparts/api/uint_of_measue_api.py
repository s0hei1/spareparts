from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import Sequence
from sqlalchemy.util import await_only

from apps.spareparts.buisness_logic_layer.uom.unit_of_measure_bll import UnitOfMeasureBLL
from apps.spareparts.buisness_logic_layer.uom.uom_schema import UnitOfMeasureRead, UnitOfMeasureCreate
from apps.spareparts.di.bll_dependencies import BLL_DI

uom_router = APIRouter(prefix ='/uom')


@uom_router.get('/read_unit_of_measures', response_model=list[UnitOfMeasureRead])
async def read_unit_of_measures(uomBLL : UnitOfMeasureBLL = Depends(BLL_DI.unit_of_measure_bll)):
    return await uomBLL.read_uoms()

@uom_router.post('/add_uom', response_model= UnitOfMeasureRead )
async def add_uom(unitOfMeasureCreate : UnitOfMeasureCreate ,
                  uomBLL : UnitOfMeasureBLL = Depends(BLL_DI.unit_of_measure_bll)):
    return await uomBLL.add_uom(unitOfMeasureCreate)
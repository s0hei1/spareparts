from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import Sequence
from sqlalchemy.util import await_only

from apps.spareparts.buisness_logic_layer.uom.unit_of_measure_bll import UnitOfMeasureBLL
from apps.spareparts.buisness_logic_layer.uom.uom_schema import UnitOfMeasureRead
from apps.spareparts.di.bll_dependencies import BLL_DI

uom = APIRouter(prefix = '/uom')


@uom.get('/read_unit_of_measures', response_model=Sequence[UnitOfMeasureRead])
async def read_unit_of_measures(uomBLL : UnitOfMeasureBLL = Depends(BLL_DI.unit_of_measure_bll)):
    return await uomBLL.read_uoms()

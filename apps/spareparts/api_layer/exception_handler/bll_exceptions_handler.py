from fastapi import  Request
from fastapi.responses import JSONResponse
from apps.spareparts.business_logic_layer.exceptions import BusinessLogicException
from apps.spareparts.business_logic_layer.exceptions import ValidationException

async def validation_exception_handler(request : Request, e : ValidationException) -> JSONResponse:
    return JSONResponse (
        status_code=400,
        content={
            "message" : e.message,
        }
    )

async def business_logic_exception_handler(request : Request, e : BusinessLogicException) -> JSONResponse:
    return JSONResponse (
        status_code=400,
        content={
            "message" : e.message,
        }
    )

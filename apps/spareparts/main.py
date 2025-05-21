from fastapi import FastAPI

from apps.spareparts.api.spareparts import sparePartsRouter
from apps.spareparts.api.uint_of_measue_api import uom

app = FastAPI()

app.include_router(sparePartsRouter)
app.include_router(uom)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

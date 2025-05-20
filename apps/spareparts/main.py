from fastapi import FastAPI

from apps.spareparts.api.spareparts import sparePartsRouter

app = FastAPI()

app.include_router(sparePartsRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

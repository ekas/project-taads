from fastapi import APIRouter, Body, HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from schema.cuisine import CuisineModel

cuisines_router = APIRouter()


@cuisines_router.get("/", status_code=200, response_description="List All Cuisines",)
async def list_cuisines(request: Request):
    cuisines = []
    for doc in await request.app.mongodb["cuisines"].find().to_list(length=100):
        cuisines.append(doc)

    print(cuisines)
    return cuisines


@cuisines_router.delete("/{id}", status_code=204, response_description="Delete cuisine")
async def delete_cuisine(request: Request, id=str):
    delete_result = await request.app.mongodb["cuisines"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Cuisine {id} not found")

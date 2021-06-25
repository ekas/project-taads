from fastapi import APIRouter, Body, HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List, Optional
from pydantic import BaseModel

from schema.cuisine import CuisineModel

cuisines_router = APIRouter()


class Params(BaseModel):
    spicy: str
    vegetarian: bool
    vegan: bool
    cuisine_name: str


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


@cuisines_router.get("/search", status_code=200, response_description="Search cuisines")
async def search_cuisine(request: Request, params: Params = Body(...)):

    # params: List[str]

    # spicy: Optional[str] = None, ingredients: Optional[str] = None,
    # vegetarian: Optional[bool] = None, vegan: Optional[bool] = None

    # cuisinesQuery = {"cuisine_name": params.cuisine_name, "spicy": params.spicy,
    #                  "vegetarian": params.vegetarian, "vegan": params.vegan}

    spicyQuery = {"spicy": params.spicy}
    vegetarianQuery = {"vegetarian": params.vegetarian}
    veganQuery = {"vegan": params.vegan}
    nameQuery = {"cuisine_name": params.cuisine_name}

    request1 = request.app.mongodb["cuisines"].find(spicyQuery).to_list(length=100)
    # request2 = request.app.mongodb["cuisines"].find(vegetarianQuery).to_list(length=100)
    # request3 = request.app.mongodb["cuisines"].find(veganQuery).to_list(length=100)
    # request4 = request.app.mongodb["cuisines"].find(nameQuery).to_list(length=100)

    spices = []
    vegetarians = []
    vegans = []
    cuisines = []
    # for doc in await request4 in await request3 in await request2 in await request1:
    for doc in await request1:
        spices.append(doc)

    for spice in spices:
        if spice['vegetarian'] == params.vegetarian:
            vegetarians.append(spice)

    for vegetarian in vegetarians:
        if vegetarian['vegan'] == params.vegan:
            vegans.append(vegetarian)

    for vegan in vegans:
        if vegan['cuisine_name'] == params.cuisine_name or params.cuisine_name == "":
            cuisines.append(vegan)

    return cuisines

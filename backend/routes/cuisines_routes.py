from fastapi import APIRouter, Body, HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List, Optional
from pydantic import BaseModel
import re

from schema.cuisine import CuisineModel, CuisineSearchModel

cuisines_router = APIRouter()


@cuisines_router.get(
    "/",
    status_code=200,
    response_description="List All Cuisines",
)
async def list_cuisines(request: Request):
    cuisines = []
    for doc in await request.app.mongodb["cuisines"].find().to_list(length=100):
        cuisines.append(doc)

    return cuisines


@cuisines_router.delete("/{id}", status_code=204, response_description="Delete cuisine")
async def delete_cuisine(request: Request, id=str):
    delete_result = await request.app.mongodb["cuisines"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Cuisine {id} not found")


@cuisines_router.post(
    "/search", status_code=200, response_description="Search cuisines"
)
async def search_cuisine(request: Request, params: CuisineSearchModel = Body(...)):

    spicy = int(params.spicy)
    if spicy == 0:
        request1 = request.app.mongodb["cuisines"].find().to_list(length=100)
    elif 0 < spicy <= 3:
        spicyQuery = {"spicy": params.spicy}
        request1 = request.app.mongodb["cuisines"].find(spicyQuery).to_list(length=100)

    spices = []
    vegetarians = []
    vegans = []
    cuisines = []
    cuisinesWithIngredients = []

    for doc in await request1:
        spices.append(doc)

    if not params.vegetarian:
        vegetarians = spices
    elif params.vegetarian:
        for spice in spices:
            if spice["vegetarian"] == params.vegetarian:
                vegetarians.append(spice)

    if not params.vegan:
        vegans = vegetarians
    elif params.vegan:
        for vegetarian in vegetarians:
            if vegetarian["vegan"] == params.vegan:
                vegans.append(vegetarian)

    cuisineNameMatch = re.compile(params.cuisine_name, flags=re.IGNORECASE)
    for vegan in vegans:
        if cuisineNameMatch.findall(vegan["cuisine_name"]):
            cuisines.append(vegan)

    for cuisine in cuisines:
        i = 0
        if len(params.ingredients) == 0:
            cuisinesWithIngredients = cuisines
            break
        if len(params.ingredients) == 1:
            for j in range(len(cuisine["ingredients"])):
                if i > 0 and j > len(params.ingredients):
                    break
                if re.compile(params.ingredients[i], flags=re.IGNORECASE).\
                        findall((cuisine["ingredients"][j]["name"]).lower()):
                    i += 1
        if len(params.ingredients) > 1:
            for k in range(len(params.ingredients)):
                for j in range(len(cuisine["ingredients"])):
                    if re.compile(params.ingredients[k], flags=re.IGNORECASE).\
                            findall((cuisine["ingredients"][j]["name"]).lower()):
                        i += 1
        if i > 0:
            cuisinesWithIngredients.append(cuisine)

    return cuisinesWithIngredients

import string
import random

from fastapi import APIRouter, Body, HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from auth.config import AuthHandler
from schema.users import UserModel, UpdateUserModel, LoginUserModel
from schema.news import NewsModel
from logic.news_logic import add_news

from ingredient_parser import parse_ingredient


user_router = APIRouter()

auth_handler = AuthHandler()


@user_router.get(
    "/list",
    status_code=200,
    response_description="List All Users",
    response_model=List[UserModel],
    response_model_exclude={"password"},
)
async def list_users(request: Request, id=Depends(auth_handler.auth_wrapper)):
    users = []
    for doc in await request.app.mongodb["users"].find().to_list(length=100):
        users.append(doc)
    return users


@user_router.get(
    "/",
    status_code=200,
    response_description="Get a single user",
    response_model=UserModel,
    response_model_exclude={"password"},
)
async def show_user(request: Request, id=Depends(auth_handler.auth_wrapper)):
    user = await request.app.mongodb["users"].find_one({"_id": id})
    if user is not None:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@user_router.put(
    "/",
    status_code=200,
    response_description="Update User with Cuisine Data",
    response_model=UpdateUserModel,
    response_model_exclude={"password"},
)
async def update_user(
    request: Request,
    user: UpdateUserModel = Body(...),
    id=Depends(auth_handler.auth_wrapper),
):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = await request.app.mongodb["users"].update_one(
            {"_id": id}, {"$set": user}
        )

        updated_user = await request.app.mongodb["users"].find_one({"_id": id})
        if updated_user is not None:
            extracted_ingredients = []
            for ingredient in updated_user["ingredients"]:
                extracted_ingredients.append(parse_ingredient(ingredient))

            extracted_ingredients = jsonable_encoder(extracted_ingredients)
            new_cuisine = await request.app.mongodb["cuisines"].insert_one(
                {
                    "_id": id,
                    "cuisine_name": updated_user["cuisine_name"],
                    "country_cuisine": updated_user["country_cuisine"],
                    "ingredients": jsonable_encoder(extracted_ingredients),
                    "spicy": updated_user["spicy"],
                    "vegetarian": updated_user["vegetarian"],
                    "vegan": updated_user["vegan"],
                    "time_to_cook": updated_user["time_to_cook"],
                    "cuisine_image": updated_user["cuisine_image"],
                    "cuisine_type": updated_user["cuisine_type"],
                }
            )

            # Add news record for cuisine
            news = NewsModel
            news.news_type = "cuisine"
            cuisine_countries = ""
            if len(updated_user["country_cuisine"]) == 1:
                cuisine_countries += updated_user["country_cuisine"][0]
            elif len(updated_user["country_cuisine"]) > 1:
                for i in range(len(updated_user["country_cuisine"])):
                    if i == len(updated_user["country_cuisine"]) - 1:
                        cuisine_countries += updated_user["country_cuisine"][i]
                        break
                    cuisine_countries += updated_user["country_cuisine"][i] + ", "

            news.title = (
                "New Cuisine "
                + updated_user["cuisine_name"]
                + " Added from "
                + cuisine_countries
            )

            # Generate new id for cuisine news(only last 8 characters are modified)
            characters = string.ascii_letters + string.digits
            new_id = "".join(random.choice(characters) for i in range(12))
            news_id = id[0:24] + new_id

            await add_news(request, news, news_id)

            return updated_user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@user_router.delete("/", status_code=204, response_description="Delete a User")
async def delete_user(request: Request, id=Depends(auth_handler.auth_wrapper)):
    delete_result = await request.app.mongodb["users"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User {id} not found")

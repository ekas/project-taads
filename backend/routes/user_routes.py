from fastapi import APIRouter, Body, HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from auth.config import AuthHandler
from schema.users import UserModel, UpdateUserModel, LoginUserModel

user_router = APIRouter()

auth_handler = AuthHandler()


@user_router.get("/list", status_code=200, response_description="List All Users", response_model=List[UserModel], response_model_exclude={'password'})
async def list_users(request: Request, id=Depends(auth_handler.auth_wrapper)):
    users = []
    for doc in await request.app.mongodb["users"].find().to_list(length=100):
        users.append(doc)
    return users


@user_router.get("/", status_code=200, response_description="Get a single user", response_model=UserModel, response_model_exclude={'password'})
async def show_user(request: Request, id=Depends(auth_handler.auth_wrapper)):
    user = await request.app.mongodb["users"].find_one({"_id": id})
    if user is not None:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@user_router.put("/", status_code=200, response_description="Update User with Cuisine Data", response_model=UpdateUserModel, response_model_exclude={'password'})
async def update_user(request: Request, user: UpdateUserModel = Body(...), id=Depends(auth_handler.auth_wrapper)):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = await request.app.mongodb["users"].update_one(
            {"_id": id}, {"$set": user}
        )

        if update_result.modified_count == 1:
            updated_user = await request.app.mongodb["users"].find_one({"_id": id})
            if updated_user is not None:
                return updated_user

    existing_user = await request.app.mongodb["users"].find_one({"_id": id})
    if existing_user is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@user_router.delete("/", status_code=204, response_description="Delete a User")
async def delete_user(request: Request, id=Depends(auth_handler.auth_wrapper)):
    delete_result = await request.app.mongodb["users"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User {id} not found")
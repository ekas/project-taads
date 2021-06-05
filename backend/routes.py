from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models import UserModel, UpdateUserModel

router = APIRouter()


@router.post("/register", response_description="Add New User")
async def register(request: Request, user: UserModel = Body(...)):
    user = jsonable_encoder(user)
    new_user = await request.app.mongodb["users"].insert_one(user)
    created_user = await request.app.mongodb["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.get("/", response_description="List All Users")
async def list_users(request: Request):
    users = []
    for doc in await request.app.mongodb["users"].find().to_list(length=100):
        users.append(doc)
    return users


@router.get("/{id}", response_description="Get a single user")
async def show_user(id: str, request: Request):
    user = await request.app.mongodb["users"].find_one({"_id": id})
    if user is not None:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@router.put("/{id}", response_description="Update User with Cuisine Data")
async def update_user(id: str, request: Request, user: UpdateUserModel = Body(...)):
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


@router.delete("/{id}", response_description="Delete a User")
async def delete_user(id: str, request: Request):
    delete_result = await request.app.mongodb["users"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User {id} not found")

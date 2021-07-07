import string
import random

from fastapi import APIRouter, Body, HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from auth.config import AuthHandler
from schema.users import UserModel, UpdateUserModel, LoginUserModel
from schema.news import NewsModel
from logic.news_logic import add_news


auth_router = APIRouter()

auth_handler = AuthHandler()


@auth_router.post("/register", status_code=201, response_description="Add New User", response_model=UserModel, response_model_include=['email'])
async def register(request: Request, user: UserModel = Body(...)):
    user = jsonable_encoder(user)
    existing_user = await request.app.mongodb["users"].find_one(
        {"email": user['email']}
    )
    if existing_user is not None:
        raise HTTPException(
            status_code=401, detail=f"User {user['email']} already exists")

    hashed_password = auth_handler.get_password_hash(user['password'])
    user['password'] = hashed_password
    new_user = await request.app.mongodb["users"].insert_one(user)
    created_user = await request.app.mongodb["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    # Add user news record
    news = NewsModel
    news.news_type = "user"
    news.title = "New user " + user["name"] + " is with us now \u2764"

    # Generate new id for cuisine news(only last 8 characters are modified)
    characters = string.ascii_letters + string.digits
    new_id = ''.join(random.choice(characters) for i in range(12))
    news_id = id[0:24] + new_id

    await add_news(request, news, news_id)

    return created_user


@auth_router.post("/login", response_description="Login User")
async def login(request: Request, user: LoginUserModel = Body(...)):
    user = jsonable_encoder(user)
    found_user = await request.app.mongodb["users"].find_one(
        {"email": user['email']}
    )
    if (found_user is None):
        raise HTTPException(
            status_code=401, detail='No user found')

    if not auth_handler.verify_password(user['password'], found_user['password']):
        raise HTTPException(
            status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(found_user['_id'])
    return {'token': token}

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017/")
db = client.taads


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
            }
        }


class UserRecipeDataModel(BaseModel):
    country_origin: str = Field(...)
    recipe_name: str = Field(...)
    recipe_data: list[str] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "country_origin": "India",
                "recipe_data": ["1 tbsp olive oil", "2 rashers smoked streaky bacon", "1 onion , finely chopped", "1 celery stick, finely chopped", "1 medium carrot , grated", "2 garlic cloves , finely chopped", "500g beef mince", "1 tbsp tomato purée", "2 x 400g cans chopped tomatoes"],
                "grecipe_name": "Nachos",
            }
        }


@app.post("/user", response_description="Add new user")
async def create_user(user: UserModel = Body(...)):
    user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    print(created_user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "User added successfully"})


@app.get(
    "/users", response_description="List all users", response_model=List[UserModel]
)
async def list_users():
    users = await db["users"].find().to_list(1000)
    return JSONResponse(status_code=status.HTTP_200_OK, content=users)


@app.get(
    "/users/{id}", response_description="Get a single user", response_model=UserModel
)
async def show_user(id: str):
    if (user := await db["users"].find_one({"_id": id})) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)

    raise HTTPException(status_code=404, detail=f"User with {id} not found")


@app.put("/users/{id}", response_description="Update a user")
async def update_user(id: str, user: UserRecipeDataModel = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = await db["users"].update_one({"_id": id}, {"$set": user})

        if update_result.modified_count == 1:
            if (
                updated_user := await db["users"].find_one({"_id": id})
            ) is not None:
                return updated_user

    if (existing_user := await db["users"].find_one({"_id": id})) is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f"User with {id} not found")


@app.delete("/{id}", response_description="Delete a user")
async def delete_user(id: str):
    delete_result = await db["users"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User with {id} not found")

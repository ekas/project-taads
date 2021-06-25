import uuid
from typing import Optional, List

from pydantic import BaseModel, Field


class LoginUserModel(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "email": "ekaspreet93.singh@gmail.com",
                "password": "ekas@Something",
            }
        }


class UserModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Ekas Preet Singh",
                "email": "ekaspreet93.singh@gmail.com",
                "password": "ekas@Something",
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    confirm_password: Optional[str]
    avatar: str = Field(...)
    country_origin: str = Field(...)
    cuisine_name: str = Field(...)
    ingredients: List[str] = []
    country_cuisine: List[str] = []
    spicy: str = Field(...)
    vegetarian: bool = Field(...)
    vegan: bool = Field(...)
    time_to_cook: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "avatar": "https://placekitten.com/300/300",
                "country_origin": "Germany",
                "cuisine_name": "Chicken Platter",
                "ingredients": ["1 tbsp olive oil", "2 rashers smoked streaky bacon", "1 onion , finely chopped", "1 celery stick, finely chopped", "1 medium carrot , grated", "2 garlic cloves , finely chopped", "500g beef mince", "1 tbsp tomato purée", "2 x 400g cans chopped tomatoes"],
                "country_cuisine": ["Germany", "France"],
                "spicy": "0",
                "vegetarian": "true",
                "vegan": "false",
                "time_to_cook": "20-30",
            }
        }

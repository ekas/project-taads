import uuid
from typing import Optional, List

from pydantic import BaseModel, Field


class CuisineIngredientModel(BaseModel):
    name: str = Field(...)
    quantity: int = Field(...)
    unit: str = Field(...)
    comment: str = Field(...)
    original_string: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "",
                "quantity": "",
                "unit": "",
                "comment": "",
                "original_string": "",
            }
        }


class CuisineModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    cuisine_name: str = Field(...)
    ingredients: List[CuisineIngredientModel] = []
    country_cuisine: List[str] = []
    spicy: str = Field(...)
    vegetarian: bool = Field(...)
    vegan: bool = Field(...)
    time_to_cook: str = Field(...)
    cuisine_image: str = Field(...)
    cuisine_type: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "cuisine_name": "Chicken Platter",
                "country_cuisine": ["Germany", "France"],
                "spicy": "0",
                "vegetarian": "true",
                "vegan": "false",
                "time_to_cook": "20-30",
                "cuisine_image": "https://placekitten.com/300/300",
                "cuisine_type": "Dinner",
            }
        }


class CuisineSearchModel(BaseModel):
    cuisine_name: str = Field(...)
    ingredients: List[str] = []
    spicy: str = Field(...)
    vegetarian: bool = Field(...)
    vegan: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "cuisine_name": "Chicken Platter",
                "spicy": "0",
                "vegetarian": "false",
                "vegan": "false",
                "ingredients": ["Chicken", "Onion", "Pepper", "Vegetable oil"],
            }
        }

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
                "original_string": ""
            }
        }


class CuisineModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    cuisine_name: str = Field(...)
    ingredients: [CuisineIngredientModel] = []
    country_cuisine: List[str] = []
    time_to_cook: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "cuisine_name": "Chicken Platter",
                "country_cuisine": ["Germany", "France"],
                "time_to_cook": "20-30",
            }
        }

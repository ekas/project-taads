import uuid
from typing import Optional, List

from pydantic import BaseModel, Field


class NewsModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    news_type: str = Field(...)
    title: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "news_type": "cuisine",
                "title": "New Cuisine Chicken Platter Added from India",
            }
        }

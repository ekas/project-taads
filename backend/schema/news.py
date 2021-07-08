import uuid
from typing import Optional, List
from datetime import datetime, time, timedelta

from pydantic import BaseModel, Field
from fastapi import Body


class NewsModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    news_type: str = Field(...)
    title: str = Field(...)
    created: datetime = Body(None)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "news_type": "cuisine",
                "title": "New Cuisine Chicken Platter Added from India",
            }
        }

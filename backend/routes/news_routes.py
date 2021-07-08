from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from schema.news import NewsModel

news_router = APIRouter()


@news_router.get(
    "/",
    status_code=200,
    response_description="List All News",
    response_model=List[NewsModel],
)
async def list_news(request: Request):
    news = []
    for doc in await request.app.mongodb["news"].find().to_list(length=100):
        news.append(doc)

    news = news[-5:]
    news.reverse()

    return news


@news_router.delete("/{id}", status_code=204, response_description="Delete news")
async def delete_news(request: Request, id=str):
    delete_result = await request.app.mongodb["news"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"News {id} not found")

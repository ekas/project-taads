from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from schema.news import NewsModel

news_router = APIRouter()


@news_router.get("/", status_code=200, response_description="List All News", response_model=List[NewsModel])
async def list_news(request: Request):
    news = []
    for doc in await request.app.mongodb["news"].find().to_list(length=100):
        news.append(doc)
    return news


@news_router.post("/", status_code=201, response_description="Add New News", response_model=NewsModel)
async def add_news(request: Request, news: NewsModel = Body(...)):
    news = jsonable_encoder(news)

    new_news = await request.app.mongodb["news"].insert_one(news)
    created_news = await request.app.mongodb["news"].find_one(
        {"_id": new_news.inserted_id}
    )

    return created_news


@news_router.delete("/{id}", status_code=204, response_description="Delete news")
async def delete_news(request: Request, id=str):
    delete_result = await request.app.mongodb["news"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"News {id} not found")


@news_router.get("/last_news", status_code=200, response_description="List Last News", response_model=List[NewsModel])
async def list_last_news(request: Request):
    news = []

    # direct sort from the db could have been useful if we had proper ids(i.e 1,2,3...)
    # for doc in await request.app.mongodb["news"].find().sort([("_id", pymongo.DESCENDING)]).limit(5).to_list(length=5):

    for doc in await request.app.mongodb["news"].find().to_list(length=100):
        news.append(doc)

    # Get last N news from the list and revert it to get latest first
    news = news[-5:]
    news.reverse()

    return news

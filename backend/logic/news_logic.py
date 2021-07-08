from fastapi import Request

from schema.news import NewsModel
import datetime


async def add_news(request: Request, news: [NewsModel], news_id=str):
    await request.app.mongodb["news"].insert_one(
        {
            "_id": news_id,
            "news_type": news.news_type,
            "title": news.title,
            "created": datetime.datetime.now(),
        }
    )

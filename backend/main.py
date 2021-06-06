import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from routes.user_routes import user_router
from routes.auth_routes import auth_router
from routes.news_routes import news_router
from routes.cuisines_routes import cuisines_router


from config import settings

app = FastAPI()

app.include_router(auth_router, tags=["Auth"])
app.include_router(user_router, tags=["Users"], prefix="/users")
app.include_router(news_router, tags=["News"], prefix="/news")
app.include_router(cuisines_router, tags=["Cuisines"], prefix="/cuisines")


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )

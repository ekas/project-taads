from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "TAADS backemd"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 3000


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb+srv://admin:61Nwtgiq6XZXhhiA@cluster0.am1dg.mongodb.net/test"
    DB_NAME: str = "taads"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()

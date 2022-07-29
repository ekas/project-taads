from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "TAADS backemd"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 4000


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb+srv://admin:241293%40Ekas@taads.18ujb.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-va2i39-shard-0&w=majority&readPreference=primary&retryWrites=true&ssl=true"
    DB_NAME: str = "taads"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()

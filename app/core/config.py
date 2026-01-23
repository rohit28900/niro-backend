from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_URL: str
    REDIS_URL: str

    API_PREFIX: str
    APP_NAME: str
    APP_VERSION: str

    class Config:
        env_file = ".env"


settings = Settings()

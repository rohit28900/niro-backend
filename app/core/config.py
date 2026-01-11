from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "Nirro"
    VERSION: str = "1.0.0"

    DATABASE_URL: str = Field(..., description="Database connection string")

    SQL_ECHO: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"   # 🔥 THIS FIXES YOUR ERROR


settings = Settings()

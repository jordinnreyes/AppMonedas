import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CURRENCY_API_KEY: str
    CURRENCY_API_URL: str = "https://api.freecurrencyapi.com/v1/latest"

    class Config:
        env_file = ".env"

settings = Settings()

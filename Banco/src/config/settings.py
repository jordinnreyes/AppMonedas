# src/settings.py del servicio banco

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    USUARIOS_SERVICE_URL: str = "http://usuarios:8000"  # nombre del contenedor + puerto interno

    class Config:
        env_file = ".env"

settings = Settings()

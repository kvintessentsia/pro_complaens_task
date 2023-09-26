# core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'работа с csv файлом'
    database_url: str

    class Config:
        env_file = '.env'

settings = Settings() 
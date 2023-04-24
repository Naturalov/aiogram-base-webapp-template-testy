from typing import Optional

from pydantic import BaseSettings, SecretStr, validator, BaseModel


class Settings(BaseSettings):
    bot_token: str

    base_url: str

    database_dns: Optional[str] = "sqlite://db.sqlite"



    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


config = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url : str

    class Config:
        env_file = ".env"

settings = Settings(database_url = 'sqlite+aiosqlite:///./spareparts/development_db.db')

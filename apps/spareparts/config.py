from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    appName : str = 'spareparts'
    debug : bool = False
    database_url : str = ''

    class Config:
        env_file = r"C:\Users\m.rahimi\PycharmProjects\spareparts\apps\spareparts\.env"

settings = Settings()


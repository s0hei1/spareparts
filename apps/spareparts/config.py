from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    appName : str = 'spareparts'
    debug : bool = False
    database_url : str = ''
    jwt_secret_key : str = ''
    jwt_algorithm: str = ''
    jwt_access_token_expire_minutes : int = 3600


    class Config:
        env_file = r"C:\Users\m.rahimi\PycharmProjects\spareparts\apps\spareparts\.env"

settings = Settings()


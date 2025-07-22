from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    appName : str = 'spareparts'
    debug : bool = False
    jwt_secret_key : str = ''
    jwt_algorithm: str = ''
    jwt_access_token_expire_minutes : int = 3600

    development_database_url : str = ''
    production_database_url : str = ''

    @property
    def database_url(self):
        db_url = self.development_database_url if self.debug else self.production_database_url

        return db_url





    class Config:
        env_file = r"C:\Users\m.rahimi\PycharmProjects\spareparts\apps\spareparts\.env"

settings = Settings()




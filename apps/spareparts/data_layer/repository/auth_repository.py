from sqlalchemy.ext.asyncio import AsyncSession


class AuthRepository():

    def __init__(self, db : AsyncSession):
        self.db = db


    
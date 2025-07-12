from datetime import datetime,timedelta, UTC
import jwt


class JWT:

    SECRET_KEY = "your-secret-key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 1440

    def create_access_token(self, data : dict, expires_delta : timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
        to_encode = data.copy()
        expire = datetime.now(UTC) + expires_delta
        to_encode['exp'] = expire
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)



    def decode_access_token(self, token : str):
        return jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])


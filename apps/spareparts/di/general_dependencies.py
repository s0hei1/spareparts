from apps.spareparts.security.jwt_helpers import JWT


class GeneralDI():

    @classmethod
    def jwt(cls) -> JWT:
        return JWT()

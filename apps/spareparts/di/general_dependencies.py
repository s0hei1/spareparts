from apps.spareparts.api_layer.api_security.jwt_helpers import JWT


class GeneralDI():

    @classmethod
    def jwt(cls) -> JWT:
        return JWT()

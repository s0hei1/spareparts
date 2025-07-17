from typing import ClassVar

from starlette.middleware.cors import CORSMiddleware

from apps.spareparts.config import settings


class CORS:

    _development_cors_settings : ClassVar[dict] = {
        'middleware_class': CORSMiddleware,
        'allow_origins': ['*'],
        'allow_credentials': False,
        'allow_methods': ["*"],
        'allow_headers': ["*"],
    }

    # TODO fix it in production mode, note: get allow origins from env file
    _production_cors_settings : ClassVar[dict] = {
        'middleware_class': CORSMiddleware,
        'allow_origins': ['*'],
        'allow_credentials': False,
        'allow_methods': ["*"],
        'allow_headers': ["*"],
    }

    @classmethod
    def get_cors_middle_ware_params(cls) -> dict:

        if settings.debug:
            return cls._development_cors_settings
        else:
            return cls._production_cors_settings


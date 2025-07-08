from apps.spareparts.business_logic_layer.exceptions import ValidationException
from apps.spareparts.data_layer.core.read_only_async_session import ReadOnlyAsyncSession
from hashlib import sha256

import re

class UserBLL:

    def __init__(self, db: ReadOnlyAsyncSession):
        self.db = db

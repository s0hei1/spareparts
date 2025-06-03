from enum import Enum


class PropertyValueType(Enum):
    INTEGER = 1
    STRING = 2
    BOOLEAN = 3
    FLOAT = 4

    def get_type(self):
        if self == PropertyValueType.INTEGER:
            return int
        if self == PropertyValueType.STRING:
            return str
        if self == PropertyValueType.BOOLEAN:
            return bool
        if self == PropertyValueType.FLOAT:
            return float

        raise ValueError('there is a mistake in PropertyValueType.getType()')



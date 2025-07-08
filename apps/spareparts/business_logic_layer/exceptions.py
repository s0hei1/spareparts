

class BusinessLogicException(Exception):

    def __init__(self, message : str):
        self.message = message

class ValidationException(BusinessLogicException):
    def __init__(self, message : str):
        self.message = message



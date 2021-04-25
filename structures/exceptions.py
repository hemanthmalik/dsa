class CustomException(Exception):
    pass

class QueueOverflowError(CustomException):
    pass

class QueueUnderflowError(CustomException):
    pass
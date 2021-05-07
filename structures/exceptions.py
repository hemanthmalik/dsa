class CustomException(Exception):
    pass

class QueueOverflowError(CustomException):
    pass

class QueueUnderflowError(CustomException):
    pass

class EmptyLinkedListError(CustomException):
    pass

class IndexOutOfRangeError(CustomException):
    pass
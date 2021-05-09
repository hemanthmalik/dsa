class CustomException(Exception):
    pass


# queue custom exceptions starts here
class QueueOverflowError(CustomException):
    pass

class QueueUnderflowError(CustomException):
    pass


# linkedlist custom exceptions starts here
class EmptyLinkedListError(CustomException):
    pass

class IndexOutOfRangeError(CustomException):
    pass

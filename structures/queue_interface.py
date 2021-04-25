from abc import ABC, abstractclassmethod

class AbstractQueue(ABC):
    @abstractclassmethod
    def enqueue(self):
        pass

    @abstractclassmethod
    def dequeue(self):
        pass

    @abstractclassmethod
    def is_empty(self):
        pass

    @abstractclassmethod
    def front(self):
        pass

    @abstractclassmethod
    def rear(self):
        pass

    @abstractclassmethod
    def display(self):
        pass
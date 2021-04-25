from queue_interface import AbstractQueue
from exceptions import QueueOverflowError, QueueUnderflowError

class CircularQueue(AbstractQueue):
    def __init__(self, size):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.first = self.last = -1

    def enqueue(self, item):
        if (self.last+1)%self.size == self.first:
            raise QueueOverflowError('Queue is full.')
        elif self.first == -1:
            self.first = self.last = 0
        else:
            self.last = (self.last+1)%self.size
        self.queue[self.last] = item

    def dequeue(self):
        if self.first == -1:
            raise QueueUnderflowError('Queue is empty.')
        elif (self.first == self.last):
            temp = self.queue[self.first]
            self.first = self.last = -1
        else:
            temp = self.queue[self.first]
            self.first = (self.first+1)%self.size
        return temp
    
    def display(self):
        if self.first == -1:
            print('Queue is empty')
        elif self.last >= self.first:
            print(*self.queue[self.first: self.last+1])
        else:
            print(*self.queue[self.first: self.size], end=" ")
            print(*self.queue[0: self.last+1])
        if (self.last+1)%self.size == self.first:
            print('Queue is full')

    def front(self):
        pass

    def rear(self):
        pass


q1 = CircularQueue(6)
q1.display()
q1.enqueue(5)
q1.enqueue(15)
q1.display()
q1.enqueue(3)
q1.enqueue(25)
q1.enqueue(115)
q1.enqueue(4000)
q1.display()
q1.dequeue()
q1.dequeue()
q1.enqueue(24)
q1.enqueue(14)
q1.dequeue()
q1.display()
q1.dequeue()
q1.display()
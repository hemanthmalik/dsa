from queue_interface import AbstractQueue
from exceptions import QueueOverflowError, QueueUnderflowError

class Queue(AbstractQueue): # queue implementation using list
    def __init__(self, size):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.last = -1
    
    def enqueue(self, item):
        if self.last + 1 == self.size:
            raise QueueOverflowError('Queue is full')
        if self.last == -1:
            self.queue[0] = item
        else:
            self.queue[self.last+1] = item
        self.last += 1
    
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError('Queue is empty')
        temp = self.queue[self.last]
        self.queue[self.last] = None
        self.last -= 1
        return temp

    def is_empty(self):
        return self.last == -1
    
    def front(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            return self.queue[0]
    
    def rear(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            return self.queue[self.last]

    def display(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            print(*self.queue[:self.last+1])

    # following two methods are used in double_ended-queue
    def inverted_enqueue(self, item):
        if self.is_empty():
            self.enqueue(item)
        elif self.last+1 == self.size:
            raise QueueOverflowError('Queue is full')
        else:
            self.queue.insert(0, item)
            self.queue = self.queue[:-2]
            self.last += 1


    def inverted_dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError('Queue is empty')
        else:
            temp = self.queue[self.last]
            self.queue[self.last] = None
            self.last -= 1
            return temp


q1 = Queue(6)
q1.enqueue(5)
q1.inverted_enqueue(9)
q1.enqueue(3)
# q1.inverted_enqueue(6)
# q1.inverted_dequeue()
q1.display()
q1.enqueue(7)
q1.enqueue(7)
q1.dequeue()
q1.display()
print(q1.is_empty())
q1.dequeue()
q1.inverted_enqueue(9)
q1.display()


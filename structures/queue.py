from queue_interface import AbstractQueue

class Queue(AbstractQueue): # queue implementation using list
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        if self.is_empty():
            return 'UnderFlow'
        item = self.queue.pop()
        return item
    
    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
    
    def rear(self):
        if len(self.queue) > 0:
            return self.queue[-1]

    # following four methods are used in double_ended-queue
    # def inverted_enqueue(self, item):
    #     self.queue.append(item)

    # def inverted_dequeue(self):
    #     item = self.queue.pop(0)
    #     return item
    
    # def inverted_front(self):
    #     return self.rear()
    
    # def inverted_rear(self):
    #     return self.front()
    
    def __str__(self):
        return " ".join(map(str, self.queue))

# q1 = Queue()
# q1.enqueue(5)
# q1.enqueue(3)
# # q1.inverted_enqueue(6)
# # q1.inverted_dequeue()
# print(q1)
# q1.enqueue(7)
# q1.dequeue()
# print(q1)
# print(q1.is_empty())
# q1.dequeue()
# print(q1)


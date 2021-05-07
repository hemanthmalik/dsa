class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        active_item = self.head
        count = 0
        if active_item != None:
            while active_item != None:
                count += 1
                active_item = active_item.next
        return count

    def append(self, data):
        new_node = Node(data)
        if self.length() == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        return self.tail

    def traverse(self):
        active_item = self.head
        while active_item != None:
            print(active_item.data, end=" -> ")
            active_item = active_item.next
        print('None')

mylist = LinkedList()
mylist.append(5)
mylist.append(10)
mylist.append(45)
mylist.append(234)
mylist.traverse()
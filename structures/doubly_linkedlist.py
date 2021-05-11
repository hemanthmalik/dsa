class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return self.tail

    def forward_traverse(self):
        list_items = []
        cur_node = self.head
        while cur_node != None:
            list_items.append(cur_node.data)
            cur_node = cur_node.next
        return list_items

    def reverse_traverse(self):
        list_items = []
        cur_node = self.tail
        while cur_node != None:
            list_items.append(cur_node.data)
            cur_node = cur_node.prev
        return list_items

    def print_items(self, reverse=False):
        print(*(self.reverse_traverse() if reverse else self.forward_traverse()))

dlist = DoublyLinkedList()
dlist.append(5)
dlist.append(14)
dlist.append(3)
dlist.append(55)
dlist.print_items()
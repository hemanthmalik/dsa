from exceptions import EmptyLinkedListError, IndexOutOfRangeError

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    # needs further optimization
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

    def push(self, data, item_index=-1):
        new_node = Node(data)
        list_len = self.length()
        item_index += 0 if item_index >= 0 else (list_len+1)
        if (item_index > list_len) or (item_index < 0):
            raise IndexOutOfRangeError("List index out of range")
        elif item_index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
            return new_node
        else:
            active_item = self.head
            cur_index = 0
            while (cur_index + 1) < item_index:
                active_item = active_item.next
                cur_index += 1
            new_node.next = active_item.next
            active_item.next = new_node
            if item_index == 0:
                self.head = new_node
            elif item_index == self.length():
                self.tail = new_node
            return new_node

    def pop(self, item_index = -1):
        list_len = self.length()
        item_index += 0 if item_index >= 0 else list_len
        if list_len == 0:
            raise EmptyLinkedListError("Can't pop element from an empty list.")
        if (item_index >= list_len) or (item_index < 0):
            raise IndexOutOfRangeError("List index out of range")
        else:
            if item_index == 0:
                popped_item = self.head
                self.head = popped_item.next
            else:
                cur_index = 0
                active_item =self.head
                while (cur_index + 1) < item_index:
                    active_item = active_item.next
                    cur_index += 1
                popped_item = active_item.next
                active_item.next = popped_item.next
                self.tail = active_item
        return popped_item

    def clear_list(self):
        self.head = None
        self.tail = None


    def print_list(self):
        active_item = self.head
        while active_item != None:
            print(active_item, end=" -> ")
            active_item = active_item.next
        print('None')

mylist = LinkedList()
mylist.push(5)
mylist.push(10)
print(mylist.pop())
mylist.push(45, -2)
mylist.push(234)
print(mylist.pop(-2))
print(mylist.pop(1))
print(mylist.length())
mylist.print_list()
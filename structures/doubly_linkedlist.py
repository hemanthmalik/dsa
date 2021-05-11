from exceptions import EmptyLinkedListError, IndexOutOfRangeError

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.total_items = 0

    def is_empty(self):
        return self.head == None

    # def length(self):
    #     cur_item = self.head
    #     items_count = 0
    #     while cur_item != None:
    #         cur_item = cur_item.next
    #         items_count += 1
    #     return items_count

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
        self.total_items += 1
        return self.tail

    def pop(self):
        popped_item = self.tail
        if self.total_items <= 1:
            self.head = None
            self.tail = None
            self.total_items = 0
        else:
            second_last_item = self.tail.prev
            second_last_item.next = None
            self.tail = second_last_item
            self.total_items -= 1
        return popped_item

    def insert(self, insert_index, data):
        new_node = Node(data)
        if insert_index > self.total_items or (insert_index < 0 and (abs(insert_index) > self.total_items)):
            raise IndexOutOfRangeError(f"Index {insert_index} out of range.")
        if insert_index == self.total_items:
            self.append(data)
            return new_node
        if insert_index < 0:
            insert_index += self.total_items
        cur_node = self.head
        insert_index_distance = insert_index
        while insert_index_distance != 0:
            cur_node = cur_node.next
            insert_index_distance -= 1
        prev_node = cur_node.prev
        if prev_node:
            new_node.prev = prev_node
            prev_node.next = new_node
        else:
            self.head = new_node
        new_node.next = cur_node
        cur_node.prev = new_node
        self.total_items += 1
        return new_node

    def delete(self, target_index):
        if (target_index > self.total_items-1) or (target_index < 0 and (abs(target_index) > self.total_items)):
            raise IndexOutOfRangeError(f'Index {target_index} out of range.')
        if target_index == self.total_items-1:
            return self.pop()
        if target_index < 0:
            target_index += self.total_items
        cur_node = self.head
        target_index_distance = target_index
        while target_index_distance != 0:
            cur_node = cur_node.next
            target_index_distance -= 1
        prev_node = cur_node.prev
        next_node = cur_node.next
        if prev_node:
            prev_node.next = cur_node.next
            next_node.prev = cur_node.prev
        else:
            self.head = cur_node.next
            next_node.prev = prev_node
        self.total_items -= 1
        return cur_node        

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
dlist.pop()
dlist.insert(1, 34)
dlist.insert(4, 29)
dlist.insert(3, 123)
dlist.delete(2)
dlist.delete(3)
dlist.delete(1)
print(dlist.total_items)
dlist.print_items()
dlist.print_items(reverse=True)
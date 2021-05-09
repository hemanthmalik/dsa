class Node:
    def __init__(self, data=None):
        self.data = data
        if self.data == None:
            self.left = None
            self.right = None
        else:
            self.left = Node()
            self.right = Node()

    def isEmpty(self):
        return self.data == None

    def __str__(self):
        return 'value: {0}'.format(self.data)


class Tree:
    def __init__(self, data=None):
        self.root = Node()

    def append(self, data):
        new_node = Node(data)
        if self.root.isEmpty():
            self.root = new_node
        else:
            active_node = self.root
            while active_node.data != None:
                if data < active_node.data:
                    if active_node.left.data == None:
                        active_node.left = new_node
                        return new_node
                    active_node = active_node.left
                elif data > active_node.data:
                    if active_node.right.data == None:
                        active_node.right = new_node
                        return new_node
                    active_node = active_node.right
                else:
                    return new_node

    def print_tree(self, root=None):
        if root == None:
            root = self.root
        if root.isEmpty():
            return []
        else:
            return (self.print_tree(root.left)+[root]+self.print_tree(root.right))
            
tree = Tree()
tree.append(5)
tree.append(10)
tree.append(15)
tree.append(2)
tree.append(3)
tree.append(15)
print([i.data for i in tree.print_tree()])
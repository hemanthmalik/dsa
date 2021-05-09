class Tree:
    def __init__(self, data=None):
        """
        initialized left and right terminals a trees when its not empty
        """
        self.data = data
        if data == None:
            self.left = None
            self.right = None
        else:
            self.left = Tree()
            self.right = Tree()

    def is_empty(self):
        """
        checks if the tree is empty
        """
        return self.data == None

    def minval(self):
        if self.left.data == None:
            return self.data
        return self.left.minval()

    def maxval(self):
        if self.right.data == None:
            return self.data
        return self.right.maxval()

    def insert(self, data):
        """
        inserts a new node in the tree at appropriate position
        """
        if self.is_empty():
            self.data = data
            self.left = Tree()
            self.right = Tree()
        else:
            if data < self.data:
                self.left.insert(data)
            elif data > self.data:
                self.right.insert(data)
        return self

    def find(self, value):
        """
        finds a node in tree having the data equals to value
        """
        if self.data == None:
            return False
        elif value < self.data:
            return self.left.find(value)
        elif value > self.data:
            return self.right.find(value)
        return True

    def delete(self, value): # needs refactoring
        """
        deletes a node from tree with value provided in argument.
        """
        if self.is_empty():
            return False
        else:
            if value == self.data:
                if self.right.data == self.left.data == None:
                    self.data = None
                    self.left = Tree()
                    self.right = Tree()
                elif self.left.data == None:
                    self.data = self.right.data
                    self.right = self.right.right
                elif self.right.data == None:
                    self.data = self.left.data
                    self.left = self.left.left
                elif (self.right.data != None) and (self.left.data != None):
                    self.data = self.left.maxval()
                    self.left.delete(self.data)                    
                return True
            elif value < self.data:
                return self.left.delete(value)
            elif value > self.data:
                return self.right.delete(value)
            return False

    def inorder(self):
        """
        return a data list following inorder traversal i.e left -> root -> right, it will always return sorted list of data nodes
        """
        if self.data == None:
            return []
        else:
            return self.left.inorder() + [self.data] + self.right.inorder()


tree = Tree()
tree.insert(3)
tree.insert(5)
tree.insert(1)
tree.insert(55)
tree.insert(2)
tree.insert(4)
print(tree.find(3))
tree.delete(5)
print(tree.inorder())

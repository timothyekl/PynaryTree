import weakref

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if isinstance(data, TreeNode):
            return self.insert(data.data)

        if data == self.data:
            return False
        elif data < self.data:
            if self.left == None:
                self.left = TreeNode(data)
                self.left.parent = weakref.ref(self)
                return True
            else:
                return self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = TreeNode(data)
                self.right.parent = weakref.ref(self)
                return True
            else:
                return self.right.insert(data)
        else:
            return False
    
    def remove(self, data):
        pass

    def __str__(self):
        # In-order
        s = ""
        if not self.left == None:
            s += str(self.left)
        s += str(self.data)
        if not self.right == None:
            s += str(self.right)
        return s

import weakref

class TreeNode:
    """It's a BST! In Python!"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """
        Insert the given data into this tree.
        """
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
        """
        Remove the given data from this tree. Return the
        removed data if it was found, or None if nothing was
        removed.
        """
        if self.data == data:
            return self._delete()
        elif data < self.data:
            if not self.left == None:
                return self.left.remove(data)
            else:
                return None
        elif data > self.data:
            if not self.right == None:
                return self.right.remove(data)
            else:
                return None
        else:
            return None

    def _delete(self):
        """Actually perform the removal algorithm on this node."""

        if self.left == None and self.right == None:
            if self.parent().left == self:
                self.parent().left = None
            else:
                self.parent().right = None
            return self.data

        elif self.left == None or self.right == None:
            if self.left == None:
                child = self.right
            else:
                child = self.left

            if self.parent().left == self:
                self.parent().left = child
            else:
                self.parent().right = child
            child.parent = self.parent
            return self.data

        else:
            succ = self._successor()
            self.data = succ.data
            succ._delete()

    def _successor(self):
        """Find the in-order successor of this node. Return a node."""

        if self.right == None:
            return None
        
        node = self.right
        while not node.left == None:
            node = node.left

        return node

    def __str__(self):
        # In-order
        s = ""
        if not self.left == None:
            s += str(self.left)
        s += str(self.data)
        if not self.right == None:
            s += str(self.right)
        return s

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.data)
        if self.right is not None:
            self.right.inorder_traversal()
root = TreeNode(27)
root.insert(140)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.inorder_traversal()


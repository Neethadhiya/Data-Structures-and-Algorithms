class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if data<self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
    def preorder_traversal(self):
        print(self.data)
        if self.left is not None:
            self.left.preorder_traversal()
        if self.right is not None:
            self.right.preorder_traversal()
root = TreeNode(10)
root.insert(122)
root.insert(11)
root.insert(14)
root.insert(17)
root.insert(19)
root.insert(15)
root.preorder_traversal()



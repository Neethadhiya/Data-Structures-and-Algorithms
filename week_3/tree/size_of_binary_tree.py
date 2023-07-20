class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def size(self,node):
        if node is None:
            return 0
        else:
            return self.size(node.left)+1+self.size(node.right)
root=Tree(78)
root.left=Tree(2)
root.right=Tree(8)
root.left.left=Tree(67)
root.left.right=Tree(89)
print("size=",root.size(root))
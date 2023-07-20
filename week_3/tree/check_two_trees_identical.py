class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def is_identical(self, a, b):
        if a is None and b is None:
            return True

        if a is not None and b is not None:
            return (
                a.data == b.data
                and self.is_identical(a.left, b.left)
                and self.is_identical(a.right, b.right)
            )

        return False
root1 = Tree(12)
root2 = Tree(12)
root1.left = Tree(12)
root1.right = Tree(15)
root1.left.left = Tree(44)
root1.left.right = Tree(56)
root2.left = Tree(12)
root2.right = Tree(15)
root2.left.left = Tree(44)
root2.left.right = Tree(56)
if root1.is_identical(root1, root2):
    print("The trees are identical.")
else:
    print("The trees are not identical.")

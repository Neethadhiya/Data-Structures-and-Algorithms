class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
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

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.data)

    def delete(self, data):
        if data < self.data:
            if self.left is not None:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right is not None:
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.find_minimum()
                self.data = min_val
                self.right = self.right.delete(min_val)
        return self

    def find_minimum(self):
        if self.left is None:
            return self.data
        return self.left.find_minimum()


# Example usage
root = TreeNode(10)
root.insert(22)
root.insert(21)
root.insert(27)
root.insert(29)
root.insert(21)
root.insert(150)

print("Before deletion:")
root.postorder()

root = root.delete(22)

print("\nAfter deletion:")
root.postorder()

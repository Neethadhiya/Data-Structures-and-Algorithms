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
    def closest(self,num):
        closest_value = None
        current = self
        while current:
            if closest_value is None or abs(num-current.data)<abs(num-closest_value):
                closest_value = current.data
            if num<current.data:
                current = current.left
            elif num>current.data:
                current = current.right
            else:
                break
        return closest_value
      
# Create the tree
root = TreeNode(90)
root.insert(57)
root.insert(78)
root.insert(79)
root.insert(24)
root.insert(57)
root.insert(68)

# Get the number from the user
num = int(input("Enter the number: "))

# Find the closest value
closest_value = root.closest(num)
print("Closest value to", num, "is", closest_value)

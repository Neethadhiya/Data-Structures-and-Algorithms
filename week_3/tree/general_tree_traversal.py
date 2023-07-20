class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
    def insert(self,data):
        new_node=TreeNode(data)
        self.children.append(new_node)
    def display(self,data):
        for child in self.children:
            child.self.display()
        print(self.data)
    def traversal(self):
        res = []
        res.append(self.data)
        for child in self.children:
            res.extend(child.traversal())
        return res

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.children[0].insert(10)
root.children[0].insert(19)
root.children[1].insert(31)
root.children[1].insert(42)

# Perform general tree traversal
print(root.traversal())






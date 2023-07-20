# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.data != right.data:
            return False
        return (
            self.checkSymmetry(left.left, right.right)
            and self.checkSymmetry(left.right, right.left)
        )


# Test the program
# Example 1:
# Symmetric tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

solution = Solution()
print(solution.isSymmetric(root1))  # Output: True

# Example 2:
# Asymmetric tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(solution.isSymmetric(root2))  # Output: False

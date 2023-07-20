# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        print(right_depth)
        return max(left_depth, right_depth) + 1


# Test the program
# Example 1:
# Binary tree with a depth of 3
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

solution = Solution()
print('hhooo',solution.maxDepth(root1))  # Output: 3

# Example 2:
# Empty binary tree (depth of 0)
root2 = None

print('hhh',solution.maxDepth(root2))  # Output: 0

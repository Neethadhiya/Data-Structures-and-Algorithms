class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


# Test the program
# Example 1:
nums1 = [-10, -3, 0, 5, 9]
solution = Solution()
root1 = solution.sortedArrayToBST(nums1)
# The resulting tree should look like this:
#       0
#      / \
#    -3   9
#   /    /
# -10   5

# Example 2:
nums2 = [1, 2, 3, 4, 5, 6, 7]
root2 = solution.sortedArrayToBST(nums2)
# The resulting tree should be a balanced binary search tree with the numbers 1 to 7.

# Printing the values in the resulting trees to verify the structure
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)

print("Inorder traversal of the first tree:")
inorder_traversal(root1)
print("Inorder traversal of the second tree:")
inorder_traversal(root2)

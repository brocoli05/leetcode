# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case
        if root is None:
            return 0
        
        # Initialize the sum
        sum_val = 0
        
        # if the current node's value is within the range
        if low <= root.val <= high:
            sum_val += root.val
        # Recursive: left subtree
        if root.val > low:
            sum_val += self.rangeSumBST(root.left, low, high)
        # Recursive: right subtree
        if root.val < high:
            sum_val += self.rangeSumBST(root.right, low, high)
            
        return sum_val
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, l, r):
        if l > r:
            return
        
        m = (l + r) // 2
        
        root = TreeNode(nums[m])
        root.left = self.helper(nums, l, m-1)
        root.right = self.helper(nums, m+1, r)
        
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # initialize the min diff and previous node value
        self.prev = float('inf')
        self.minDiff = float('inf')
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.minDiff = min(self.minDiff, abs(node.val - self.prev))
            self.prev = node.val
            dfs(node.right)
            
        dfs(root)
        return self.minDiff
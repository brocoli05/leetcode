# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal prev, ans
            if not node:
                return
            dfs(node.left)
            if prev is not None:
                ans = min(ans, node.val - prev)
            prev = node.val
            dfs(node.right)
        
        prev = None
        ans = float('inf') # initialize with a large value
        dfs(root) # update as the smallest value
        return ans
            
            
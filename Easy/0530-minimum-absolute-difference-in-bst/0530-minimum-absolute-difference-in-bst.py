# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ## Method 1)
        nums = []
        
        def dfs(node):

            if not node:
                return

            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
     
        dfs(root)

        answer = float('inf')
        
        for index in range(1, len(nums)):
            answer = min(answer, nums[index] - nums[index - 1])
        
        return answer
    
    ## Method 2)
#         # initialize the min diff and previous node value
#         self.prev = float('inf')
#         self.minDiff = float('inf')
        
#         def dfs(node):
#             if not node:
#                 return
            
#             dfs(node.left)
#             self.minDiff = min(self.minDiff, abs(node.val - self.prev))
#             self.prev = node.val
#             dfs(node.right)
            
#         dfs(root)
#         return self.minDiff
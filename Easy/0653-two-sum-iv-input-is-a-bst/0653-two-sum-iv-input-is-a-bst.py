# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set() # create an empty object
        return self.dfs(root, k, visited)
    
    def dfs(self, node, k, visited): #depth-first search
        if not node:
            return False
        
        i = k - node.val
        if i in visited:
            return True
        
        visited.add(node.val)
        
        return self.dfs(node.left, k, visited) or self.dfs(node.right, k, visited)
        
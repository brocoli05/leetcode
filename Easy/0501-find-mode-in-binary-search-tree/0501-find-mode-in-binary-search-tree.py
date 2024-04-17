# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = [] # list to store the modes
        self.pred = None # predecessor node (comes before)
        self.count = 0
        self.maxCount = 0
    
        def updateCount(root):
            if self.pred and self.pred.val == root.val:
                self.count += 1
            else:
                self.count = 1

            if self.count > self.maxCount:
                self.maxCount = self.count
                self.ans = [root.val] # resets the current value
            elif self.count == self.maxCount:
                self.ans.append(root.val)

            self.pred = root

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            updateCount(root)
            inorder(root.right)
        
        inorder(root)
        return self.ans
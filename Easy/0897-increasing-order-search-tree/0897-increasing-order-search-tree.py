# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # create dummy node to track the previous node
        dummy = TreeNode()
        self.prev = dummy
        # in-order traversal
        self.inorder(root)
        # return the right child of dummy node
        return dummy.right
        
    def inorder(self, node):
        # Base case
        if not node:
            return
        
        # traversal left subtree
        self.inorder(node.left)
        
        # link the node to the next node
        self.prev.right = node
        node.left = None
        self.prev = node
        
        # traversal right subtree
        self.inorder(node.right)
        
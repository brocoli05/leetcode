# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ## Method 1) 2 functions
        def inorder(node):
            # Base case
            if not node:
                return []
            
            values = [] # create empty list
            values.extend(inorder(node.left)) # add left subtree
            values.append(node.val)
            values.extend(inorder(node.right)) # add right subtree
            return values
            
        def formTree(node, i):
            # Base case
            if i == len(self.values):
                return 
            
            node.right = TreeNode(self.values[i])
            formTree(node.right, i + 1)
        
        self.values = inorder(root) # sorted list of node values
        self.node = TreeNode()
        formTree(self.node, 0)
        return self.node.right # return the right child of self.node
        
        ## Method 2)
#         # create dummy node to track the previous node
#         dummy = TreeNode()
#         self.prev = dummy
#         # in-order traversal
#         self.inorder(root)
#         # return the right child of dummy node
#         return dummy.right
        
#     def inorder(self, node):
#         # Base case
#         if not node:
#             return
        
#         # traversal left subtree
#         self.inorder(node.left)
        
#         # link the node to the next node
#         self.prev.right = node
#         node.left = None
#         self.prev = node
        
#         # traversal right subtree
#         self.inorder(node.right)
        
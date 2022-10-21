# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if root is None:
            return []
        self.helper(lst, root)
        return lst
    
    def helper(self, lst, node):     
        if node:
            lst.append(node.val)
            self.helper(lst, node.left)
            self.helper(lst, node.right)

            
            
            
            
    
    
        
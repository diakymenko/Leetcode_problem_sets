# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if root is None:
            return lst
        return self.helper(root, lst)
    
    def helper(self, current, lst):
        if current:
            self.helper(current.left, lst)
            lst.append(current.val)
            self.helper(current.right, lst)
        return lst
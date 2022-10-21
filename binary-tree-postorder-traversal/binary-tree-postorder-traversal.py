# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if root is None:
            return lst
        return self.helper(root, lst)
    
    def helper(self, current, lst):
        if current:
            self.helper(current.left, lst)
            self.helper(current.right, lst)
            lst.append(current.val)
        return lst
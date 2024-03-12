# Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            children = []
            children.append(self.maxDepth(root.left))
            children.append(self.maxDepth(root.right))
            
            return max(children) + 1
        else:
            return 0
        
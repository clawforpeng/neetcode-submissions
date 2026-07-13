# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        min = -math.inf
        max = math.inf

        return self.isValid(min, max, root)
        
    def isValid(self, min: float, max: float, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if root.val > min and root.val < max:
            return self.isValid(min, root.val, root.left) and self.isValid(root.val, max, root.right)
        return False
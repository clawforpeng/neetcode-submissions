# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        minimum = -1001
        sol = minimum

        def dfs(cur: Optional[TreeNode]) -> int:
            nonlocal sol
            if not cur:
                return minimum
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            result = cur.val + max(0, left, right)
            
            sol = max(sol, result, left + right + cur.val)

            return result
        
        dfs(root)

        return sol
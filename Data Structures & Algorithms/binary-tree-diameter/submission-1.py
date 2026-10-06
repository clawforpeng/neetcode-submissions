# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = 0
        if not root:
            return sol

        def dfs(node: TreeNode) -> int:
            nonlocal sol
            
            left = 0
            right = 0
            if node.left:
                left = dfs(node.left) + 1
            if node.right:
                right = dfs(node.right) + 1


            sol = max(sol, left + right)

            return max(left, right)

        dfs(root)
        return sol
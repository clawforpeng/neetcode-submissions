# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = 0

        def dfs(node: TreeNode | None, maxVal: int):
            nonlocal sol
            if not node:
                return
            val = node.val
            if val >= maxVal:
                sol += 1
                maxVal = val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)
        return sol
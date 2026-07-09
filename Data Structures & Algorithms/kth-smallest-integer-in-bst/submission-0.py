# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedList = self.dfs(root)

        return sortedList[k - 1]
    
    def dfs(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        ans = []
        ans.extend(self.dfs(root.left))
        ans.append(root.val)
        ans.extend(self.dfs(root.right))

        return ans
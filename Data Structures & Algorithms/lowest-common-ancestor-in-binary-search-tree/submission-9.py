# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        pPath = []

        while cur.val != p.val and cur:
            pPath.append(cur)
            if cur.val < p.val:
                cur = cur.right
            else:
                cur = cur.left

        if cur.val == p.val:
            pPath.append(cur)
        
        qPath = []
        cur = root

        while cur.val != q.val and cur:
            qPath.append(cur)
            if cur.val < q.val:
                cur = cur.right
            else:
                cur = cur.left

        if cur.val == q.val:
            qPath.append(cur)
        
        print(pPath, qPath)
        minLength = min(len(pPath), len(qPath))

        while minLength > 0:
            index = minLength - 1
            if pPath[index] == qPath[index]:
                return pPath[index]
            minLength -= 1
        
        return TreeNode()
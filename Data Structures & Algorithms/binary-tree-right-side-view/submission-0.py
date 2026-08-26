# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sols = []

        if not root:
            return sols
        
        q = deque()

        q.append(root)
        nodes = 1 # num of unvisited nodes per level
        sols.append(root.val)

        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

            nodes -= 1
            if nodes == 0:
                nodes = len(q)
                if nodes:
                    sols.append(q[-1].val)


        return sols
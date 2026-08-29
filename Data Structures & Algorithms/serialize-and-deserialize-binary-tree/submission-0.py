# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        sol = []

        def dfs(cur: Optional[TreeNode]):
            if not cur:
                sol.append("N")
                return
            sol.append(str(cur.val))

            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)

        return ",".join(sol)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = data.split(",")

        root = TreeNode()

        i = 0

        def rec(cur: TreeNode):
            nonlocal i
            if i == len(nodes):
                return
            
            cur.val = int(nodes[i])
            i += 1

            if nodes[i] != "N":
                left = TreeNode()
                cur.left = left
                rec(left)
            
            i += 1

            if nodes[i] != "N":
                right = TreeNode()
                cur.right = right
                rec(right)
        
        rec(root)

        return root


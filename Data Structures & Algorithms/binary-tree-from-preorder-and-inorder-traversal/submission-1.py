# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # key: val, value: index
        # inorderMap = defaultdict(int)

        # for index, val in enumerate(inorder):
        #     inorderMap[val] = index
        if len(preorder) == 0:
            return None

        root = preorder[0]
        node = TreeNode(root)
        index = inorder.index(root)

        left = inorder[:index]
        if len(left) > 0:
            node.left = self.buildTree(preorder[1 : index + 1], left)
        
        right = inorder[index + 1:]
        if len(right) > 0:
            node.right = self.buildTree(preorder[index + 1 : ], right)

        return node
        
    # def dfs(self, preorder: List[int])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        ans = self.traverse(root, subRoot)

        if ans:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            

    def traverse(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not tree2 and not tree1:
            return True

        if not tree2:
            return False
        
        if not tree1:
            return False
        
        if tree1.val != tree2.val:
            return False
        
        return self.traverse(tree1.left, tree2.left) and self.traverse(tree1.right, tree2.right)
        

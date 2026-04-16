# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        sameTree = self.isSameTree(root, subRoot)

        if sameTree:
            return True
        
        left, right = False, False

        if root.left:
            left = self.isSubtree(root.left, subRoot)
        
        if root.right:
            right = self.isSubtree(root.right, subRoot)
        
        if left or right:
            return True
            
        return False

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        left, right = False, False
        
        if p.val == q.val:
            left, right = self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)
            
        if left and right:
            return True
        
        return False
            
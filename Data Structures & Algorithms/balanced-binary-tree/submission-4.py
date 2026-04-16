# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftHeight, rightHeight = self.maxDepth(root.left), self.maxDepth(root.right)

        if abs(leftHeight - rightHeight) < 2:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True

        return False


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth, rightDepth = 0, 0
        
        if root.left:
            leftDepth += self.maxDepth(root.left)
        
        if root.right:
            rightDepth += self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)
    

        
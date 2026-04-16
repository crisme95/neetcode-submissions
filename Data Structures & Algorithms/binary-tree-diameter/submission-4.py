# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        diameter = leftDepth + rightDepth
        subtreeDiameter = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(diameter, subtreeDiameter)
        
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth, rightDepth = 0, 0
        
        if root.left:
            leftDepth += self.maxDepth(root.left)
        
        if root.right:
            rightDepth += self.maxDepth(root.right)
        
        return 1 + max(leftDepth, rightDepth)
        
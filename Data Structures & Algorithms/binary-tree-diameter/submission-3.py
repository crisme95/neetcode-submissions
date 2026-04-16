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
        
        rootDiameter, leftDiameter, rightDiameter = 0, 0, 0

        rootDiameter = self.maxDepth(root.left) + self.maxDepth(root.right)

        leftDiameter = self.maxDepth(root.left) - 1
        leftDiameter = max(self.diameterOfBinaryTree(root.left), leftDiameter)
        
        rightDiameter = self.maxDepth(root.right) - 1
        rightDiameter = max(self.diameterOfBinaryTree(root.right), rightDiameter)

        return max(rootDiameter, leftDiameter, rightDiameter)
        
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth, rightDepth = 0, 0
        
        if root.left:
            leftDepth += self.maxDepth(root.left)
        
        if root.right:
            rightDepth += self.maxDepth(root.right)
        
        return 1 + max(leftDepth, rightDepth)
        
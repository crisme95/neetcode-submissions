# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.withinBounds(float('-inf'), float('inf'), root)
    

    def withinBounds(self, node_min: int, node_max: int, node: 'TreeNode') -> bool:
        if not node:
            return True

        left, right = None, None

        if node.val > node_min and node.val < node_max:
            left = self.withinBounds(node_min, node.val, node.left)
            right = self.withinBounds(node.val, node_max, node.right)
        
        if left and right:
            return True
        
        return False
        
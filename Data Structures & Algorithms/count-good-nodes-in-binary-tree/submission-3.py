# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.good = 0
        self.dfs(root, root.val)

        return self.good
        
    def dfs(self, node: TreeNode, path_max: int) -> None:
        if not node:
            return

        if node.val >= path_max:
            self.good += 1
            path_max = node.val
        
        self.dfs(node.left, path_max)
        self.dfs(node.right, path_max)
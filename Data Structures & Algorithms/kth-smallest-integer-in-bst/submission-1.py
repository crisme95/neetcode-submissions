# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        self.count = k
        self.res = None

        self.inorder(root)

        return self.res


    def inorder(self, node: 'TreeNode') -> None:
        if not node or self.res is not None:
            return
        
        self.inorder(node.left)
        
        self.count -= 1

        if self.count == 0:
            self.res = node.val

        self.inorder(node.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,a):
        if root is not None:
            a.append(root.val)
            self.preorder(root.left,a)
            self.preorder(root.right,a)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return
        a = []
        self.preorder(root,a)
        
        d = {}
        for i in a:
            if (k - i) in d:
                return True
            else:
                d[i] = 1
        
        return False
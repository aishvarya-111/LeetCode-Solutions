# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a,b = p.val,q.val
        def ans(root,a,b):
            if a<root.val and b<root.val:
                return ans(root.left,a,b)
            if a>root.val and b>root.val:
                return ans(root.right,a,b)
            return root
        return ans(root,a,b)
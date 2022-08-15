# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(root,d):
            if not root:
                return 0
            l = height(root.left,d)
            r = height(root.right,d)
            d[0] = max(d[0],l+r)
            
            return 1+max(l,r)
        
        d = [0]
        height(root,d)
        return d[0]
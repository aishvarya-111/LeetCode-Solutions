# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path(root,maxi):
            if not root:
                return 0
            l = max(0,path(root.left,maxi))
            r = max(0,path(root.right,maxi))
            maxi[0] = max(maxi[0],l+r+root.val)
            
            return root.val + max(l,r)
        
        maxi = [-10**6]
        path(root,maxi)
        return maxi[0]
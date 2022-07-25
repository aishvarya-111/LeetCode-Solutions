# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,arr,val):
        if root.left==None and root.right==None:
            arr.append(val)
            return
        if root.left:
            self.check(root.left,arr,val+root.left.val)
        if root.right:
            self.check(root.right,arr,val+root.right.val)
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if root==None:
                return False
            arr = []
            self.check(root,arr,root.val)
            if targetSum in arr:
                return True
            return False
        
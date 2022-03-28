# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,d):
        if root is not None:
            self.inorder(root.left,d)
            if root.val in d:
                d[root.val]+=1
            else:
                d[root.val]=1   
            self.inorder(root.right,d)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        d={}
        self.inorder(root,d)
        m=0
        a=[]
        for k,v in d.items():
            if v>m:
                m=v
                a=[k]
            elif v==m:
                a.append(k)
        return a
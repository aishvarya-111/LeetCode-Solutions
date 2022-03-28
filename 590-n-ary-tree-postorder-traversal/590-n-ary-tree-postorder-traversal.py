"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def recurse(self,root,a):
        if root is not None:
            for i in root.children:
                self.recurse(i,a)
            a.append(root.val)
            
    def postorder(self, root: 'Node') -> List[int]:
        if root==None:
            return
        a=[]
        self.recurse(root,a)
        return a
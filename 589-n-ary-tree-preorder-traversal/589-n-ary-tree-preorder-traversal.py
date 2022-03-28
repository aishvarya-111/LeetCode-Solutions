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
            a.append(root.val)
            for i in root.children:
                self.recurse(i,a)
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return 
        a=[]
        self.recurse(root,a)
        return a
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1 
        l,r = 0,n 
        while(l<r):
            m = (l+r)//2 
            if isBadVersion(m):
                r = m 
            else:
                l = m+1 
        return r
            
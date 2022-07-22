class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l<=r:
            mid = (l+r)//2
            row = (mid*(mid+1))//2
            if row == n:
                return mid
            if row<n:
                l = mid+1
            else:
                r = mid-1
                
        return r
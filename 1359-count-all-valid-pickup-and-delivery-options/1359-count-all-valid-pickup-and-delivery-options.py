class Solution:
    def countOrders(self, n: int) -> int:
        f = 1
        for i in range(2,n+1):
            f*=i
        f = f%(10**9+7)
        s = 1
        for i in range(1,2*n,2):
            s*=i
        s = s%(10**9+7)
        return int((f*s)%(10**9+7))
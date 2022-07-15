class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n:
            m = n%10
            p*=m
            s+=m
            n = n//10
        return p-s
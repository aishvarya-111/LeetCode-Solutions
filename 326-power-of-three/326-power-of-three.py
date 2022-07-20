class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        ans = math.log(n) / math.log(3) 
        return 3**(math.ceil(ans))==n
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        x = math.log(n)/math.log(2)
        print(x)
        if 2**int(x)==n:
            return True
        return False
import math
class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for i in range(1,n):
            for j in range(i+1,n):
                d = math.sqrt(i*i + j*j)
                if int(d) == d and d<=n:
                    c+=2
        return c
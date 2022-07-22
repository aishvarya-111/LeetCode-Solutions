class Solution:
    def fib(self, n: int) -> int:
        f=[0,1]
        for i in range(n+1):
            if i>1:
                t =f[i-1]+f[i-2]
                f.append(t)
        return f[n]
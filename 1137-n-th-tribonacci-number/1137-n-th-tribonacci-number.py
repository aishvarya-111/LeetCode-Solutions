class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0,1,1]
        for i in range(3,n+1):
            ans.append(ans[-1]+ans[-2]+ans[-3])
        return ans[n]
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            s = (n>>i)&1
            ans = ans|(s<<(31-i))
        return ans
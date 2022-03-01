class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            s = list(bin(i)[2:])
            a = sum([int(j) for j in s])
            res.append(a)
        return res
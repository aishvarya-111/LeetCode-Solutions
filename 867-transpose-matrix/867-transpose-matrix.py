class Solution:
    def transpose(self, m: List[List[int]]) -> List[List[int]]:
        d = []
        for i in range(len(m[0])):
            t = []
            for j in range(len(m)):
                t.append(m[j][i])
            d.append(t)
        return d
                
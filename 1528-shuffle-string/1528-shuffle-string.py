class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = ""
        for i in range(len(indices)):
            idx = indices.index(i)
            r+=s[idx]
        return r
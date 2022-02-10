class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = True
        for i in range(len(s)):
            if s[i] in t:
                j = t.index(s[i])
                t = t[j+1:]
            else:
                ans = False
                break
        
        return ans
        
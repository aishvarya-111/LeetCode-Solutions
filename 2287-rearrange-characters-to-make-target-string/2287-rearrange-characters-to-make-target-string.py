import math
class Solution:
    def rearrangeCharacters(self, s: str, t: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        g = {}
        for i in t:
            if i not in g:
                g[i]=1 
            else:
                g[i]+=1
             
        ans = 10**6
        for i in t:
            if i in s:
                ans = min(ans,math.floor(d[i]/g[i]))
            else:
                ans = 0
                break
        return ans
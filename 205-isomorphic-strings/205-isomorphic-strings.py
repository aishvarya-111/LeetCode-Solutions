from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d ,e = defaultdict(),defaultdict()
        
        for i in range(len(s)):
            if s[i] in d and d[s[i]] != t[i]:
                return False
            if t[i] in e and e[t[i]] != s[i]:
                return False
            
            d[s[i]] = t[i]
            e[t[i]] = s[i]
        return True
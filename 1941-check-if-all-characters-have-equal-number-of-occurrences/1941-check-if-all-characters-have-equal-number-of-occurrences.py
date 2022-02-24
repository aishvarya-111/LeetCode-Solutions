class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        c = d[i]    
        for k,v in d.items():
            if v!=c:
                return False
        return True
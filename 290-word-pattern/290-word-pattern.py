class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        l = list(s.split())
        if len(l)!=len(p):
            return False
        d={}
        t = {}
        for i in range(len(p)):
            if p[i] not in d:
                d[p[i]]=l[i]
            else:
                if d[p[i]]!=l[i]:
                    return False 
                
            if l[i] not in t:
                t[l[i]]=p[i]
            else:
                if t[l[i]]!=p[i]:
                    return False
        return True
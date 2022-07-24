class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d, res, lp, ls = defaultdict(int), [], len(p), len(s)
        if lp>ls:
            return []
        for i in p:
            d[i]+=1 
        c =  defaultdict(int)
        for i in range(lp):
            c[s[i]]+=1
            
        if c==d:
                res.append(0)
            
        for i in range(1,ls-lp+1):
  
            c[s[i-1]]-=1
            if c[s[i-1]]==0:
                del c[s[i-1]]
               
            c[s[i+lp-1]]+=1
            if c==d:
                res.append(i)
     
        return res
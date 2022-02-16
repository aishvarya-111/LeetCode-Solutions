class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        c = 0 
        for h,v in d.items():
            if v==1:
                c+=1
            if c==k:
                return h
        return ""
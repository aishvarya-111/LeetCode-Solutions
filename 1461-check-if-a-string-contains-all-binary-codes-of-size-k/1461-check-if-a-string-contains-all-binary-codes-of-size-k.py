class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = set()
        n = len(s)
        for i in range(0,n-k+1):
            d.add(s[i:k+i])
       
        if(len(d)==2**k):
            return True 
        else:
            return False
class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        a = [0]*26
        for i in m:
            idx = ord(i)-ord('a')
            a[idx]+=1 
        
        for i in r:
            idx = ord(i)-ord('a')
            a[idx]-=1 
        for i in r:
            idx = ord(i)-ord('a')
            if a[idx]<0:
                return False
        return True
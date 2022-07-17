class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        b = [0]*26 
        
        for i in s:
            idx = ord(i)-ord('a')
            a[idx]+=1
        for i in t:
            idx = ord(i)-ord('a')
            b[idx]+=1
        
        return a==b
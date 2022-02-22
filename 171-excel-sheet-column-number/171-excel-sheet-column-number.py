class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = columnTitle[::-1]
        a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        c = ord(s[0])-64
        if(len(s)==1):
            return c
        
        for i in range(1,len(s)):
            b = ord(s[i]) - 64
            c = c + pow(26,i)*b
        return c
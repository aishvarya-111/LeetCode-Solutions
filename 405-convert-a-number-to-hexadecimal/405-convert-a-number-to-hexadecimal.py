class Solution:
    def toHex(self, num: int) -> str:
        d = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        res = ''
        if num==0:
            return '0'
        if num<0:
            num+=(2**32)
        while num>0:
            r = int(num%16)
            res=d[r]+res
            num//=16 
        return res
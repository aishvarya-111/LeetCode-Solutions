class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        t = ''
        for i in b:
            if i=='0':
                t+='1'
            else:
                t+='0'
        
        return int(t,2)
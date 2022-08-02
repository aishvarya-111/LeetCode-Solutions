class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        f = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
        t = 1
        n = 0
        m = 0
        for i in range(len(num1)-1,-1,-1):
            n += d[num1[i]]*t
            t*=10
        t = 1
        for i in range(len(num2)-1,-1,-1):
            m += d[num2[i]]*t
            t*=10
        nm = n*m
        ans = ""
        if nm==0:
            return '0'
        while nm:
            mod = nm%10
            nm = nm//10 
            ans+=f[mod]
        return ans[::-1]
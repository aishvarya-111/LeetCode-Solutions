class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1 
        flag = 1
        c = 0
        b = 0
        for k,v in d.items():
            if v%2==0:
                c+=v 
            elif v%2!=0 and v>1:
                c+=(v-1)
                b=1
        c+=b       
        if c%2==0:
            for k,v in d.items():
                if v==1:
                    c+=1
                    break
        return c
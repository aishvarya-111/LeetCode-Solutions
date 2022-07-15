class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        a=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                a.append(i)
                c+=1
            if c>2:
                return False 
        if c==0:
            return True
        if c==2 and s1[a[0]]==s2[a[1]] and s1[a[1]] == s2[a[0]]:
            return True
        return False
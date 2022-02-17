class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        poc,oc,pzc,zc=0,0,0,0
        for i in s:
            if i=="1":
                oc+=1
                pzc = max(pzc,zc)
                zc = 0
            else:
                zc+=1
                poc = max(poc,oc)
                oc=0
                
        return max(poc,oc) > max(pzc,zc)
                
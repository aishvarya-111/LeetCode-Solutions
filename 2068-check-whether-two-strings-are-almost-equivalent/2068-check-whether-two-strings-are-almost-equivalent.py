class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        for i in word1:
            if i in word2:
                word1 = word1.replace(i,"",1)
                word2 = word2.replace(i,"",1)
        
        d1 = {}
        d2 = {}
        for i in word1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in word2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        
        for k,v in d1.items():
            if k in d2 and abs(v-d2[k])>3:
                return False
            if k not in d2 and v>3:
                return False
        for k,v in d2.items():
            if k not in d1 and v>3:
                return False
        return True
                
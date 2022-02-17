class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        for i in words:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        c=0
        for k,v in d.items():
            if v%len(words)==0:
                c+=1
        return c==len(d)
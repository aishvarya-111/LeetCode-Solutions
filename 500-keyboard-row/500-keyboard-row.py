class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            aa,bb,cc,n = 0,0,0,len(i)
            for j in i:
                if j in i:
                    if j in "qwertyuiopQWERTYUIOP":
                        aa+=1
                    elif j in "asdfghjklASDFGHJKL":
                        bb+=1
                    else:
                        cc+=1
            if aa==n or bb==n or cc==n:
                res.append(i)
        return res
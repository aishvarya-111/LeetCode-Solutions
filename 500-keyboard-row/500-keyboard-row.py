class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = "qwertyuiopQWERTYUIOP"
        b = "asdfghjklASDFGHJKL"
        c = "zxcvbnmZXCVBNM"
        res = []
        for i in words:
            aa,bb,cc,n = 0,0,0,len(i)
            for j in i:
                if j in i:
                    if j in a:
                        aa+=1
                    elif j in b:
                        bb+=1
                    else:
                        cc+=1
            if aa==n or bb==n or cc==n:
                res.append(i)
        return res
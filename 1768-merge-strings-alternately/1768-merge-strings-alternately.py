class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        if len(word1)>len(word2):
            s=word1[len(word2):]
            word1 = word1[:len(word2)]
        elif len(word1)<len(word2):
            s = word2[len(word1):]
            word2 = word2[:len(word1)]
        
        w1 = list(word1)
        w2 = list(word2)
        
        ans=[None]*(len(w1)+len(w2))
        ans[::2]=w1
        ans[1::2]=w2
        
        ans = "".join(ans)+s
        return ans
        
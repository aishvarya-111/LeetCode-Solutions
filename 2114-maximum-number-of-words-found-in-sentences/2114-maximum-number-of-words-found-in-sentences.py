class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in sentences:
            s = list(i.split())
            n = len(s)
            if(n>m):
                m = n
        return m
        
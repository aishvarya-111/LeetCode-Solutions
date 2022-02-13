class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        n = len(words1)
        m = len(words2)
        count=0
        if(n<=m):
            for i in words1:
                if(words1.count(i)==1 and i in words2 and words2.count(i)==1):
                    count+=1
        else:
            for i in words2:
                if(words2.count(i)==1 and i in words1 and words1.count(i)==1):
                    count+=1
        return count
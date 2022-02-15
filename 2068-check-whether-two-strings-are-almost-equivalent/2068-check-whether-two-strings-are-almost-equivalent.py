class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        d1 = Counter(word1)
        d2 = Counter(word2)
        for k,v in d1.items():
            if abs(v-d2[k])>3:
                return False
        for k,v in d2.items():
            if abs(v-d1[k])>3:
                return False
        return True
                
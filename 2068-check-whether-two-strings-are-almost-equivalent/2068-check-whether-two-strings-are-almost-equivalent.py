class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        d1 = Counter(word1)
        d2 = Counter(word2)
        for k,v in d1.items():
            if k in d2 and abs(v-d2[k])>3:
                return False
            if k not in d2 and v>3:
                return False
        for k,v in d2.items():
            if k not in d1 and v>3:
                return False
        return True
                
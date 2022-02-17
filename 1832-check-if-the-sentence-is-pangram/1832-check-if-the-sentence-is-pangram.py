class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = []
        for i in sentence:
            a.append(ord(i)-96)
        return sorted(set(a)) == [*range(1,27)]
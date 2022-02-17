class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = []
        for i in sentence:
            a.append(ord(i))
        return sorted(set(a)) == [*range(97,123)]
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = [ord(i)-96 for i in sentence]
        return sorted(set(a)) == [*range(1,27)]
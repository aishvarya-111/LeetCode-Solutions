class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        l = [int(i) for i in s if i.isnumeric()]
        if len(l)>len(set(l)):
            return False
        return sorted(l)==l
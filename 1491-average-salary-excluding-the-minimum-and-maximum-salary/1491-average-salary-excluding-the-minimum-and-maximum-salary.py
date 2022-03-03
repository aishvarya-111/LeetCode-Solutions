class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        l = len(salary)-2
        s = sum(salary[1:l+1])/l
        return s
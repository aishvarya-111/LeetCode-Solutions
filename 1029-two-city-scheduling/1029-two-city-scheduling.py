class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = sum([i[0] for i in costs])
        d = [b-a for a,b in costs]
        d.sort()
        for i in range(len(costs)//2):
            s+=d[i]
        return s